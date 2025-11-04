import random
from typing import List, Tuple, Dict, Mapping
from loguru import logger

from antlr4 import *
from grampar.utils import store_output
from pyformlang.cfg import CFG

#from multiprocessing import Process, Queue
from multiprocessing import Pool

class CFGCoverage():
    def __init__(self, cfg: CFG, 
                 seeds: List[str],
                 mutation_pools: List[str],
                 Lexer, Parser, parser_root="s",
                 skip_rulenames=[],
                 no_mutate=[]
                 ):
        self.cfg = cfg
        self.lexer = Lexer
        self.parser = Parser

        # process_mutation_set
        self.input_parts = process_mutation_set(cfg, 
                     mutation_pools+seeds, 
                     Lexer, Parser, parser_root,
                     skip_rulenames,
                     no_mutate,
                     verbose=True)

        #for rulename, values in self.input_parts.items():
        #    print(f"-- {rulename}: {len(values)}")
        #    for v in values:
        #        print(f"\t {repr(v)}")

        # process seeds
        self.seeds = seeds
        self.tokenized_seeds = []
        for seed in seeds:
            try:
                t, rl = get_tokenize_n_rule_indices(seed, Lexer, Parser, parser_root)
            except Exception as e:
                logger.error(f"Failed to parse seed:\n{repr(seed)}")
                logger.error(f"Reason: {e}")
                t, rl = None, None
            if not t or not rl:
                logger.warning(f"Skip adding seed:\n{repr(seed)}")
                continue
            self.tokenized_seeds.append((t, rl))
            #for rulename, values in rl.items():
            #    value = "".join([t[1] for t in t[values[0][0]:values[0][1]+1]])
            #    print(f"-- {rulename}:\n {repr(value)}")
        # list of each seed with (toknized_seed, seed_indices)


        self.pend_input_parts = {}
        self.done_input_parts = {}

        #for rulename, values in self.input_parts.items():
        #    print("--", rulename, len(values))
        #    for v in values:
        #        print("\t " + repr(v))

        self.rule_diffs = {}
        # key: (rulename) 

    def is_interested(self, rulename, inp, diffs)-> bool | None:
        if all([v for v in diffs.values()]):
            logger.debug(f"-- No diff for {rulename}, skipping...")
            return None

        def diff_diffdicts(dict_a, dict_b):
            compared = []
            for k, v in dict_a.items():
                if k == "MUTATE":
                    continue
                if k not in dict_b:
                    raise ValueError(f"Key {k} not found in second dict")
                if v != dict_b[k]:
                    return True
                compared.append(k)
            for k in dict_b:
                if k == "MUTATE":
                    continue
                if k not in compared:
                    raise ValueError(f"Key {k} not found in first dict")
            return False

        if rulename not in self.rule_diffs:
            self.rule_diffs[rulename] = []
            self.rule_diffs[rulename].append((diffs, inp))
            return True
        for (prev_diff,_) in self.rule_diffs[rulename]:
            if not diff_diffdicts(prev_diff, diffs):
                logger.debug(f"-- Seen pattern for {rulename}, skipping...")
                return False
        self.rule_diffs[rulename].append((diffs, inp))
        return True


    def get_next_mutations(self)-> Dict[str, List[str]]:
        # TODO: have a feedback mechanism to prioritize certain rulename?
        # randomly pick a rulename
        rulename = random.choice(list(self.input_parts.keys())) if self.input_parts else None

        if not rulename:
            if self.pend_input_parts:
                return self.get_mutations_from_pending()
            return {}
        no_delete = False
        if rulename not in self.done_input_parts:
            self.done_input_parts[rulename] = set()
        else:
            no_delete = True
        if not self.input_parts[rulename]:
            del self.input_parts[rulename]
            return self.get_next_mutations()
        value = self.input_parts[rulename].pop()
        self.done_input_parts[rulename].add(value)
        logger.debug(f"{rulename}: {len(self.input_parts[rulename])} -> {len(self.done_input_parts[rulename])}")

        if no_delete:
            test_inputs = {f"{rulename}-R": [], f"{rulename}-A": []}
        else:
            test_inputs = {f"{rulename}-D": [], f"{rulename}-R": [], f"{rulename}-A": []}
        for seed in self.tokenized_seeds:
            toknized_seed, seed_indices = seed
            if rulename not in seed_indices:
                continue
            for start, end in seed_indices[rulename]:
                pre = "".join([t[1] for t in toknized_seed[:start]])
                mid = "".join([t[1] for t in toknized_seed[start:end+1]])
                post = "".join([t[1] for t in toknized_seed[end+1:]])
                if not no_delete:
                    # Delection
                    test_inputs[f"{rulename}-D"].append(pre + post)
                # Replacement 
                test_inputs[f"{rulename}-R"].append(pre + value + post)
                # Addition (behind)
                test_inputs[f"{rulename}-A"].append(pre + mid + value + post)
        return test_inputs

    def get_mutations_from_pending(self)-> Dict[str, List[str]]:
        rulename = random.choice(list(self.pend_input_parts.keys())) if self.pend_input_parts else None
        if not rulename:
            return {}
        if not self.pend_input_parts[rulename]:
            del self.pend_input_parts[rulename]
            return self.get_mutations_from_pending()
        logger.debug(f"{rulename} (p): {len(self.pend_input_parts[rulename]) - 1}")
        test_inputs = self.pend_input_parts[rulename].pop()
        return {rulename: test_inputs}


def get_cfg(cfg_f, verbose=False):
    with open(cfg_f, "r") as f:
        cfg = CFG.from_text(f.read())

    if verbose:
        print(cfg.to_text())

    return cfg


def get_tokenize_n_rule_indices(seed: str,
                                Lexer, Parser,
                                root_rule: str,
                                verbose=False
                                ) -> Tuple[List[Tuple[str, str]], 
                                           Dict[str, List[Tuple[int, int]]]]:
    """
    NOTE: try-catch this function in the caller
    """
    if verbose:
        #logger.debug(f"Tokenizing and parsing seed of size {len(seed)}...")
        logger.debug(f"Tokenizing and parsing seed ...\n{seed}")
    #logger.debug(f"Tokenizing and parsing seed of size {len(seed)}...")
    logger.debug(f"Tokenizing and parsing seed ...\n{seed}")

    input_stream = InputStream(seed)
    lexer = Lexer(input_stream)

    tokenized_input = []
    for token in lexer.getAllTokens():
        token_name = lexer.symbolicNames[token.type] or f"'{lexer.literalNames[token.type]}'"
        tokenized_input.append((token_name, token.text))

    # Get parse tree in ANTLR
    input_stream = InputStream(seed)
    lexer = Lexer(input_stream)

    stream = CommonTokenStream(lexer)
    parser = Parser(stream)

    # Turn off default error listener, don't return parse tree if error
    parser.removeErrorListeners()
    #tree = parser.mimeMessage()
    tree = getattr(parser, root_rule)()
    if parser.getNumberOfSyntaxErrors() > 0:
        return tokenized_input, dict()

    # Get index ranges for each rule in the parse tree
    def get_rule_indices(node, rule_indices):
        if isinstance(node, ParserRuleContext):
            rule_name = parser.ruleNames[node.getRuleIndex()].lower()
            start_index = node.start.tokenIndex
            end_index = node.stop.tokenIndex
            if rule_name not in rule_indices:
                rule_indices[rule_name] = []
            rule_indices[rule_name].append((start_index, end_index))
            for child in node.getChildren():
                get_rule_indices(child, rule_indices)
    rule_indices = dict()
    get_rule_indices(tree, rule_indices)

    return tokenized_input, rule_indices


def get_rulename_splits(cfg: CFG, 
                        seed: str, 
                        Lexer, Parser,
                        parser_root: str,
                        input_parts=dict(),
                        skip_rulenames=[],
                        no_mutate=[],
                        verbose=False
                        ) -> Dict[str, set]:
    """
    - Difference between skip_rulenames and no_mutate:
        + skip_rulenames: skip collecting values for these rulenames,
          won't even traverse into these areas when collecting chunks of rulenames
    """

    def _check_skip(rulename, skip_l):
        for skip in skip_l:
            if skip.lower() in rulename.lower():
                return True
        return False

    def _in_regions(start, end, regions):
        for r_start, r_end in regions:
            if start >= r_start and end <= r_end:
                return True
        return False

    try:
        tokenized_input, rule_indices = get_tokenize_n_rule_indices(seed, Lexer, Parser, parser_root, verbose)

        tokens_input = [t[0].lower() for t in tokenized_input]
        labels_input = [t[1] for t in tokenized_input]

        # Get rule sets based on CYK
        cyk_table = cfg.get_cyk_table(tokens_input)

    except Exception as e:
        logger.error(f"Failed to parse seed:\n{repr(seed)}")
        logger.error(f"Reason: {e}")
        return input_parts

    skip_regions = []
    if rule_indices:
        for key, v in rule_indices.items():
            if _check_skip(key, skip_rulenames):
                for start, end in v:
                    skip_regions.append((start, end))

    for k, v in cyk_table.items():
        if not v:
            continue
        for cyknode in v:
            rulename = cyknode.value.value # CYKNode -> Variable -> str
            if rulename == "S" or _check_skip(rulename, skip_rulenames) \
                    or _check_skip(rulename, no_mutate):
                continue

            # NOTE: hacky and not-sure way to skip sampling at certain areas
            # Check if it's fully within "skip_rulenames" ranges
            start, end = k
            if _in_regions(start, end, skip_regions):
                continue

            value = "".join(labels_input[start:end+1])
            rulename = rulename.lower()
            if rulename not in input_parts:
                input_parts[rulename] = set()
            input_parts[rulename].add(value)

    return input_parts


def process_mutation_set(cfg:CFG, 
                     seeds: List[str], 
                     Lexer, Parser, parser_root,
                     skip_rulenames=[],
                     no_mutate=[],
                     verbose=False):
    input_parts = dict()
    
    logger.info(f"Processing mutation seeds ({len(seeds)})...")
    for seed in seeds:
        logger.debug(f"Mutation seed of size {len(seed)}...")
        input_parts = get_rulename_splits(
                cfg, seed, Lexer, Parser, parser_root, input_parts, skip_rulenames, no_mutate,
                verbose)
    return input_parts


def _worker(servers, new_inp, test_method, verbose):
    return new_inp, test_method(servers, new_inp, verbose)

def fuzz_cfg(cfg_file: str, 
             full_count: int,
             Lexer,
             Parser,
             parser_root: str,
             seeds: List[str], 
             mutate_seeds: List[str], 
             skip_rulenames: List[str],
             no_mutate: List[str],
             servers: List[str], 
             output_dir: str, 
             query_id: int,
             test_method,
             multi_core_num: int=1,
             dry_run: bool=False,
             verbose: bool=False)-> Tuple[int, int, List[str]]:
    """
    * test_method: define customized hook to return differential test results
      args: 
        - targets: List[]    # list of target names
        - new_inp: str       # mutated input, the method should integrate it into requests
      returns:
        - (difftest_results: Mapping[str, Tuple[bool, str]], output: str)
            + difftest_results:  a dictionary of `target` -> (`accept?`, `output`)
            + output          :  full log to be stored 
    """
    cfg = get_cfg(cfg_file, verbose=False)

    cfg_cov = CFGCoverage(cfg,
                          seeds,
                          mutate_seeds,
                          Lexer, Parser, parser_root,
                          skip_rulenames,
                          no_mutate)

    # Send seed first
    for seed in seeds:
        full_count += 1
        diff, results, output = test_method(servers, seed, verbose)

        if (any([c for c,_ in results.values()]) and \
                not all([c for c,_ in results.values()])):
            diff["MUTATE"] = ("SEED", 0, 0, 0)
            query_id = store_output(output_dir, query_id, full_count, seed, diff, results, output)
    if dry_run:
        return query_id, []

    next_intersting = []
    def _post_process(query_id, full_count, rulename, inp, diff, results, output, verbose)-> Tuple[int, bool|None]:
        if not all([v for v in diff.values()]):
            logger.debug("++ DIFF!")
        interest = cfg_cov.is_interested(rulename, inp, diff)
        if interest: 
            logger.debug(f"++ Interesting mutation for rule {rulename}")
            if verbose:
                logger.debug(output)
            diff["MUTATE"] = (rulename, 0, 0, 0)
            output = f"{rulename}\n\n" + output
            return store_output(output_dir, query_id, full_count, inp, diff, results, output), True
        return query_id, interest

    while True:
        test_inputs = cfg_cov.get_next_mutations()
        if not test_inputs:
            break
        for rulename, mutated_inputs in test_inputs.items():
            logger.debug(f"++ Testing {rulename} mutations ({len(mutated_inputs)})...")
            if multi_core_num > 1:
                job_args = []
                for new_inp in mutated_inputs:
                    job_args.append((servers, new_inp, test_method, verbose))
                with Pool(processes=multi_core_num) as pool:
                    results = pool.starmap(_worker, job_args)
                for (new_inp, (diff, results, output)) in results:
                    full_count += 1
                    query_id,_ = _post_process(query_id, full_count, rulename, new_inp, diff, results, output, verbose)

            else:
                while mutated_inputs:
                    new_inp = mutated_inputs.pop()
                    diff, results, output = test_method(servers, new_inp, verbose)
                    full_count += 1
                    query_id, interest = _post_process(query_id, full_count, rulename, 
                                                          new_inp, diff, results, output, verbose)
                    # If not interesting (either no-diff or seen), pend others for later re-test
                    if (interest is None or not interest) and mutated_inputs:
                        if rulename not in cfg_cov.pend_input_parts:
                            cfg_cov.pend_input_parts[rulename] = []
                        cfg_cov.pend_input_parts[rulename].append(mutated_inputs)
                        logger.debug(f"Pending {rulename} for later re-test")
                        break
    return full_count, query_id, next_intersting

