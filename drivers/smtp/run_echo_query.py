#!/usr/bin/env python3
import os
import sys
import argparse
import codecs

from loguru import logger

from smtpfuzz.fuzz import pairwise_diff
from smtpfuzz.grid import print_grid
from smtpfuzz.grampar_driver import query_garden_full
from fuzz_cfg_smtp import smtp_two_diff

logger.remove()
logger.add(sys.stderr, 
           filter={
               #"smtpfuzz": "ERROR", 
               "": "INFO",
             }
           )

"""
  Paths
"""
SMPT_GARDEN_PATH = os.getenv("SMTP_GARDEN_PATH", "")
if not SMPT_GARDEN_PATH:
    print("SMTP_GARDEN_PATH environment variable is not set.")
    exit(1)


if __name__ == "__main__":

    parser = argparse.ArgumentParser('run_echo_query.py', 
                                     description='Get the result of parsing SMTP')
    parser.add_argument("file")
    args = parser.parse_args()

    payload_file = args.file

    verbose = False

    if verbose:
        print(f"\n.....................................\n")
    smtp_payloads = []
    with open(f"{payload_file}", "r") as fd:
        for line in fd:
            linebytes = codecs.escape_decode(bytes(line[0:-1], "latin-1"))[0]
            smtp_payloads.append(linebytes)
            if verbose:
                print(line[0:-1])
    if verbose:
        print(f"\n.....................................\n")

    servers = [
            "postfix", 
            "msmtp", 
            "exim", 
            "opensmtpd", 
            "nullmailer", 
            "aiosmtpd", 
            "james-maildir",
            ]

    output_dir = "/tmp/smtp_output/"
    os.system(f"rm -rf {output_dir}")
    os.makedirs(output_dir)

    cur_dir = os.getcwd()
    os.chdir(SMPT_GARDEN_PATH)

    garden_results = query_garden_full(servers, smtp_payloads)

    os.chdir(cur_dir)

    full_output = ""
    for server, (accept, output) in garden_results.items():
        msg = f"\n\n* {server}: {accept}\n{output[0]}\n--\n{output[1]}"
        full_output += msg + "\n" + "-"*10 + "\n"
        #if verbose:
        #    print(msg)
        if "TAIL" in output[0] or "TAIL" in output[1]:
            has_tail = True
    diff = pairwise_diff(garden_results, smtp_two_diff)
    full_output += print_grid(servers, diff, verbose)

    print(f"\n.....................................\n")
    print(full_output)

