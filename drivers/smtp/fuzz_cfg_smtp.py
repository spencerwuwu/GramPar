#!/usr/bin/env python
import argparse
import sys
import os
import codecs
from typing import List, Tuple, Dict, Mapping

from loguru import logger

from grampar.utils import setup_output_dir
from grampar.cfgfuzz import fuzz_cfg
from grampar.antlr_drivers.smtp.driver.SMTPLexer import SMTPLexer
from grampar.antlr_drivers.smtp.driver.SMTPParser import SMTPParser

from smtpfuzz.fuzz import pairwise_diff
from smtpfuzz.grid import print_grid
from smtpfuzz.grampar_driver import query_garden_full


CORE = 1

logger.remove()
logger.add(sys.stderr, 
           filter={
               "smtpfuzz": "ERROR", 
               #"": "INFO",
               "": "DEBUG",
             }
           )

"""
  Paths
"""
SMPT_GARDEN_PATH = os.getenv("SMTP_GARDEN_PATH", "")
if not SMPT_GARDEN_PATH:
    print("SMTP_GARDEN_PATH environment variable is not set.")
    exit(1)


def smtp_two_diff(pa: Tuple[bool, Tuple[str, str]], 
                  pb: Tuple[bool, Tuple[str, str]])-> bool:
    # Sanitize done in query_garden_full
    return pa[0] == pb[0] and pa[1] == pb[1]


def test_smtp_from_cfg(servers: List[str],
                       smtp_payload_str: str,
                       verbose: bool=False
                       )-> Tuple[Mapping[str, bool],
                            Mapping[str, Tuple[bool, Tuple[str, str]]], 
                             str]:


    smtp_payloads = [f"{s}\n".encode("latin-1") for s in smtp_payload_str.split("\n")]

    cur_dir = os.getcwd()
    os.chdir(SMPT_GARDEN_PATH)

    garden_results = query_garden_full(servers, smtp_payloads)

    os.chdir(cur_dir)

    full_output = ""
    has_tail = False
    for server, (accept, output) in garden_results.items():
        msg = f"\n\n* {server}: {accept}\n{output[0]}\n--\n{output[1]}"
        full_output += msg + "\n" + "-"*10 + "\n"
        if verbose:
            print(msg)
        if "TAIL" in output[0] or "TAIL" in output[1]:
            has_tail = True
    diff = pairwise_diff(garden_results, smtp_two_diff)
    full_output += print_grid(servers, diff, verbose)

    return diff, garden_results, full_output


def fuzz_smtp_cfg(parsers: List=[str],
                  cfg_file: str="./CFG_smtp.txt",
              output_dir: str="./output",
              seed_dir: str="./cfg_seeds/",
              mutate_seed_dir: str="./cfg_mutate_seeds/",
              test_method=test_smtp_from_cfg,
              verbose: bool=False
              ):

    if not setup_output_dir(output_dir):
        exit(1)

    skip_rulenames = [
            "#CNF", "ANTLR_new",
            "_opt", "_star", "_plus",
            ]
    no_mutate = []

    seeds = []
    # NOTE: back to ascii only
    for root, dirs, files in os.walk(seed_dir):
        for f in files:
                data = b""
                with open(f"{root}/{f}", "r") as fd:
                    for line in fd:
                        linebytes = codecs.escape_decode(bytes(line[0:-1], "latin-1"))[0]
                        #print(type(linebytes), repr(linebytes))
                        data += linebytes
                    seeds.append(data.decode())

    mutate_seeds = []
    for root, dirs, files in os.walk(mutate_seed_dir):
        for f in files:
                data = b""
                with open(f"{root}/{f}", "r") as fd:
                    for line in fd:
                        linebytes = codecs.escape_decode(bytes(line[0:-1], "latin-1"))[0]
                        #print(type(linebytes), repr(linebytes))
                        data += linebytes
                    mutate_seeds.append(data.decode())

    query_id = 0

    full_count = 0

    full_count, query_id, _ = fuzz_cfg(cfg_file, 
                                       full_count,
                                       SMTPLexer,
                                       SMTPParser,
                                       "session",
                                       seeds, 
                                       mutate_seeds,
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
    parser.add_argument("-o", dest="output_dir", default="./output-cfg")
    parser.add_argument("-c", dest="cfg_file", default="./CFG_smtp.txt")
    args = parser.parse_args()

    servers = [
            "msmtp", 
            "nullmailer", 
            "aiosmtpd", 
            "exim", 
            "postfix", 
            #"opensmtpd", 
            "james-maildir",
            ]

    fuzz_smtp_cfg(servers, 
                  args.cfg_file,
                  args.output_dir,
                  "./cfg_seeds",
                  "./cfg_seeds", 
                  test_smtp_from_cfg,
                  verbose=False)


if __name__ == '__main__':
    main()

