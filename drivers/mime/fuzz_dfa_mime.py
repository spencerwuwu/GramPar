#!/usr/bin/env python
import argparse
import sys
import os
from typing import List, Tuple, Dict, Mapping

from loguru import logger

from grampar.flex2fst import Flexparser
from grampar.utils import setup_output_dir, get_common_unicode
from grampar.dfafuzz import DDFACoverage, fuzz_dfa

from mime_tester import test_mime_parser

logger.remove()
logger.add(sys.stderr, 
           filter={
               "grampar.dfafuzz": "ERROR", 
               "": "INFO",
             }
           )


def fuzz_mime(lex_filename: str="mime.l",
              parsers: List=[str],
              output_dir: str="./output",
              seed_dir: str="./seeds_mime-simple/",
              test_method=test_mime_parser,
              verbose: bool=False
              ):

    if not setup_output_dir(output_dir):
        exit(1)

    flex_a = Flexparser(get_common_unicode())
    mma = flex_a.yyparse(lex_filename)

    # readin seed requests
    seeds = []
    for f in os.listdir(seed_dir):
        with open(f"{seed_dir}/{f}", "r") as fd:
            #data = fd.read().replace("\n", "\r\n")
            data = fd.read()
            seeds.append(data)

    cov_addr = DDFACoverage(mma)

    query_id = 0

    full_count = 0
    for seed in seeds:
        full_count, query_id,_ = fuzz_dfa(mma, full_count,
                                          seed, cov_addr,
                                          parsers, output_dir, query_id, 
                                          test_method,
                                          verbose=verbose)
    

def main():
    parser = argparse.ArgumentParser('fuzz_dfa_mime.py', description='')
    parser.add_argument("-o", dest="output_dir", default="output")
    parser.add_argument("-i", dest="seed_dir", default="./seeds_mime-simple")
    parser.add_argument("-l", dest="lexer_file", default="./mime.l")
    args = parser.parse_args()

    parsers = [
               # c-sharp
               "mimekit-parser",
               # java
               "apache-common-parser",
               # pyp
               "php-mime-mail-parser",
               # js
               "mailparser-parser",
               "postal-mime-parser",
               # python
               "email-parser",
               ]
    fuzz_mime(args.lexer_file, 
              parsers, 
              args.output_dir, 
              args.seed_dir,
              test_mime_parser,
              verbose=False)

if __name__ == '__main__':
    main()
