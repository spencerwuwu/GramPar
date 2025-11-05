#!/usr/bin/env python
import argparse
import sys
import os
from typing import List, Tuple, Dict, Mapping

from loguru import logger

from grampar.utils import setup_output_dir, get_common_unicode
from grampar.cfgfuzz import fuzz_cfg
from grampar.antlr_drivers.mime.driver.MimeLexer import MimeLexer
from grampar.antlr_drivers.mime.driver.MimeParser import MimeParser

from mime_tester import test_mime_parser

CORE = 20
#CORE = 1

logger.remove()
logger.add(sys.stderr, 
           filter={
               "fuzz_mime": "ERROR", 
               "": "INFO",
             }
           )


def fuzz_mime_cfg(parsers: List=[str],
              cfg_file: str="CFG_mime.txt",
              output_dir: str="./output",
              seed_dir: str="./seeds_mime-simple/",
              test_method=test_mime_parser,
              verbose: bool=False
              ):

    if not setup_output_dir(output_dir):
        exit(1)

    skip_rulenames = [
            "#CNF", "ANTLR_new",
            "_opt", "_star", "_plus",
            "BodyContent", "BodyLine",
            "mimeBody", "contentData"
            ]
    #no_mutate = ["commentcontent", "quotedstringcontent"]
    no_mutate = []

    # readin seed requests
    seeds = []
    for f in os.listdir(seed_dir):
        with open(f"{seed_dir}/{f}", "r") as fd:
            #data = fd.read().replace("\n", "\r\n")
            data = fd.read()
            seeds.append(data)

    query_id = 0

    full_count = 0

    full_count, query_id, _ = fuzz_cfg(cfg_file, 
                                    full_count,
                         MimeLexer,
                         MimeParser,
                         "mimeMessage",
                         seeds, 
                         seeds, 
                         skip_rulenames,
                         no_mutate,
                         parsers, 
                         output_dir, 
                         query_id,
                         test_method,
                         multi_core_num=CORE,
                         dry_run=False,
                         verbose=verbose)

    print("Full queries sent:", full_count)
    

def main():
    parser = argparse.ArgumentParser('fuzz_cfg_mime.py', description='')
    parser.add_argument("-o", dest="output_dir", default="output")
    parser.add_argument("-i", dest="seed_dir", default="./seeds_mime-simple")
    parser.add_argument("-c", dest="cfg_file", default="./CFG_mime.txt")
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
    fuzz_mime_cfg(parsers, 
                  args.cfg_file,
                  args.output_dir,
                  args.seed_dir,
                  test_mime_parser,
                  verbose=False)


if __name__ == '__main__':
    main()
