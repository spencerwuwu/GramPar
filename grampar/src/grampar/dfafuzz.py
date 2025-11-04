
from loguru import logger
from typing import List, Tuple, Dict, Mapping

from grampar.pythondfa import PythonDFA, DFAArc, get_input_alts
from grampar.utils import store_output, pairwise_diff



class DDFACoverage():
    def __init__(self, mma: PythonDFA):
        self.mma = mma

        self.covered_trans = set()
        # key: (arc_src, arc_dst, alt_arc_src, alt_arc_dst, alt_arc_ilabel)

        self.trans_diffs = {}
        # key: (arc_src, arc_dst, alt_arc_src, alt_arc_dst)
        # values: [(diff_pairs, input)]

        self.mma_new_states = {}
        # key: (arc_src, arc_dst, arc_char_ilabel)

    def in_seen_trans(self, arc_src, arc_dst, alt_arc):
        tran = (arc_src, arc_dst, alt_arc.srcstate, alt_arc.nextstate, alt_arc.ilabel)
        if tran in self.covered_trans:
            return True
        return False

    def patch_mma(self, src_id, dst_id, cur_inp_ilabel, 
                  alt_arc, new_states_map, 
                  verbose=False):
        mma = self.mma
        if (src_id, dst_id, cur_inp_ilabel) in new_states_map:
            new_state = new_states_map[(src_id, dst_id, cur_inp_ilabel)]
        else:
            sid = mma.add_state()
            new_state = mma.states[sid]
            new_states_map[(src_id, dst_id, cur_inp_ilabel)] = new_state
        alt_arc.nextstate = new_state.stateid
        new_arc = DFAArc(new_state.stateid, dst_id, cur_inp_ilabel)
        new_state.arcs.append(new_arc)

        alt_inp = mma.isyms.find(alt_arc.ilabel) 
        o_arc_f = f"{alt_arc.srcstate} -> {alt_arc.nextstate} {repr(alt_inp)}"
        n_arc_f = f"{new_arc.srcstate} -> {new_arc.nextstate} {mma.isyms.find(cur_inp_ilabel)}"
        logger.info(f"Patching mma {o_arc_f} + {n_arc_f}")



    def check_interest(self, inp, alt_arc,
                       arc_src, arc_dst, arc_char_ilabel, 
                       smtp_results,
                       verbose=False)-> Tuple[bool, bool]:

        tran = (arc_src, arc_dst, alt_arc.srcstate, alt_arc.nextstate, alt_arc.ilabel)
        self.covered_trans.add(tran)

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

        mma_diff = False

        mma_accept = self.mma.consume_input(inp)
        # Patch mma if result diffs
        if not mma_accept:
            # check if any server accepts it
            if not any([c for c,_ in smtp_results.values()]):
                return False, False
            if all([c for c,_ in smtp_results.values()]):
                logger.info(f"Patching MMA for: {inp}")
                self.patch_mma(arc_src, arc_dst, arc_char_ilabel, 
                               alt_arc, self.mma_new_states)
                mma_diff = True

        cur_diff = pairwise_diff(smtp_results)
        tran = (arc_src, arc_dst, alt_arc.srcstate, alt_arc.nextstate)
        seen_diff = False
        if tran in self.trans_diffs:
            for (prev_diff,_) in self.trans_diffs[tran]:
                if not diff_diffdicts(prev_diff, cur_diff):
                    seen_diff = True
                    break
            if not seen_diff:
                self.trans_diffs[tran].append((cur_diff, inp))
        else:
            self.trans_diffs[tran] = [(cur_diff, inp)]

        if not seen_diff:
            logger.info(f"New transition diff for {tran} with input {repr(inp)}")
                
        return mma_diff, not seen_diff


def fuzz_dfa(mma: PythonDFA, 
             full_count: int,
              seed: str, 
              Cov: DDFACoverage, 
              servers: List[str], 
              output_dir: str, 
              query_id: int,
              test_method,
              verbose: bool=False):
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

    full_count += 1

    # Send seed first
    diff, results, output = test_method(servers, seed, verbose=False)
    if (any([c for c,_ in results.values()]) and \
            not all([c for c,_ in results.values()])):
        diff["MUTATE"] = ("SEED", 0, 0, 0)
        query_id = store_output(output_dir, query_id, full_count, seed, diff, results, output)

    mutate_sets,_ = get_input_alts(mma, seed, verbose)

    next_intersting = []

    for (src_id, dst_id, cur_inp_ilabel, alts) in mutate_sets[1:]:
        for arc_nextstate, alt_arcs in alts.items():
            for alt_arc, new_inp in alt_arcs:
                if Cov.in_seen_trans(src_id, dst_id, alt_arc):
                    continue
                full_count += 1
                pair_diff, results, output = test_method(servers, new_inp, verbose=False)
                mma_diff, smtp_diff = Cov.check_interest(new_inp,
                                                         alt_arc,
                                                         src_id, dst_id,
                                                         cur_inp_ilabel,
                                                         results,
                                                         verbose=False)
                if mma_diff or smtp_diff:
                    output = f"MMA_DIFF: {mma_diff}\n\n{output}"
                    pair_diff["MUTATE"] = (mma.isyms.find(alt_arc.ilabel), src_id, dst_id, cur_inp_ilabel)
                    query_id = store_output(output_dir, query_id, full_count, new_inp, pair_diff, results, output)
                if mma_diff:
                    next_intersting.append(new_inp)
    return full_count, query_id, next_intersting
