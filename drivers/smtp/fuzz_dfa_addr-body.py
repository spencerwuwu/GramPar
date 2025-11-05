#!/usr/bin/env python
import argparse
import sys
import os
import string
from typing import List, Tuple, Dict, Mapping

from grampar.flex2fst import Flexparser
from grampar.dfafuzz import DDFACoverage, fuzz_dfa
from grampar.utils import setup_output_dir

from smtpfuzz.grampar_driver import query_garden_header, query_garden_body
from smtpfuzz.fuzz import pairwise_diff
from smtpfuzz.grid import print_grid

from loguru import logger


SMPT_GARDEN_PATH = os.getenv("SMTP_GARDEN_PATH", "")
if not SMPT_GARDEN_PATH:
    print("SMTP_GARDEN_PATH environment variable is not set.")
    exit(1)


logger.remove()
logger.add(sys.stderr, 
           filter={
               "smtpfuzz": "ERROR", 
               "": "INFO",
             }
           )


def create_mailfrom_payloads(addr: str)-> List[bytes]:
    b_addr = addr.encode('latin-1')
    msg = [
        b"EHLO smtpgarden\r\n",
        b"MAIL FROM:" + b_addr + b"\r\n",
        b"RCPT TO:<user1@echo.smtp.garden>\r\n",
        #b"RCPT TO:" + b_addr + b"\r\n",
        b"DATA\r\n",
        b":HEADxxxTAIL\r\n",
        b"\r\n.\r\n",
        b"QUIT\r\n"
    ]
    return msg


def create_recpto_payloads(addr: str)-> List[bytes]:
    b_addr = addr.encode('latin-1')
    msg = [
        b"EHLO smtpgarden\r\n",
        b"MAIL FROM:<root@google.com>\r\n",
        b"RCPT TO:" + b_addr + b"\r\n",
        b"DATA\r\n",
        b":HEADxxxTAIL\r\n",
        b"\r\n.\r\n",
        b"QUIT\r\n"
    ]
    return msg


def create_body_payloads(body: str)-> List[bytes]:
    b_body = body.encode('latin-1')
    msg = [
        b"EHLO smtpgarden\r\n",
        b"MAIL FROM:<root@google.com>\r\n",
        b"RCPT TO:<user1@xxx.xxx>\r\n",
        b"DATA\r\n",
        b":HEAD" + b_body + b"TAIL\r\n",
        b"\r\n.\r\n",
        b"QUIT\r\n"
    ]
    return msg


def test_body(servers: List[str],
              body: str,
              verbose: bool=False
              )-> Tuple[Mapping[str, bool],
                        Mapping[str, Tuple[bool, str]], 
                        str]:


    logger.info("Querying garden DATA with body: {} ...", repr(body))
    smtp_payloads = create_body_payloads(body)
    return test_body_input(servers, smtp_payloads, verbose)


def test_recpto(servers: List[str],
                  addr: str,
                  verbose: bool=False
                  )-> Tuple[Mapping[str, bool],
                            Mapping[str, Tuple[bool, str]], 
                            str]:

    logger.info("Querying garden RECPTO with ADDR: {} ...", repr(addr))
    smtp_payloads = create_recpto_payloads(addr)
    return test_header_input(servers, smtp_payloads, verbose)


def test_mailfrom(servers: List[str],
                  addr: str,
                  verbose: bool=False
                  )-> Tuple[Mapping[str, bool],
                            Mapping[str, Tuple[bool, str]], 
                            str]:

    logger.info("Querying garden MAILFROM with ADDR: {} ...", repr(addr))
    smtp_payloads = create_mailfrom_payloads(addr)
    #smtp_payloads = create_recpto_payloads(addr)
    return test_header_input(servers, smtp_payloads, verbose)


def test_body_input(servers: List[str],
                      smtp_payloads: List[bytes],
                      verbose: bool=False
                      )-> Tuple[Mapping[str, bool],
                               Mapping[str, Tuple[bool, str]], 
                                str]:

    cur_dir = os.getcwd()
    os.chdir(SMPT_GARDEN_PATH)

    logger.debug(f"Setting working directory to {SMPT_GARDEN_PATH}")
    garden_results = query_garden_body(servers, smtp_payloads)

    os.chdir(cur_dir)

    full_output = ""
    for server, (accept, output) in garden_results.items():
        msg = f"\n\n* {server}: {accept}\n" + output
        full_output += msg + "\n" + "-"*10 + "\n"
        if verbose:
            print(msg)
    diff = pairwise_diff(garden_results)
    full_output += print_grid(servers, diff, verbose)

    return diff, garden_results, full_output


def test_header_input(servers: List[str],
                      smtp_payloads: List[bytes],
                      verbose: bool=False
                      )-> Tuple[Mapping[str, bool],
                                Mapping[str, Tuple[bool, str]], 
                                str]:

    cur_dir = os.getcwd()
    os.chdir(SMPT_GARDEN_PATH)

    logger.debug(f"Setting working directory to {SMPT_GARDEN_PATH}")
    garden_results = query_garden_header(servers, smtp_payloads)

    os.chdir(cur_dir)

    full_output = ""
    for server, (accept, output) in garden_results.items():
        msg = f"\n\n* {server}: {accept}\n" + output
        full_output += msg + "\n" + "-"*10 + "\n"
        if verbose:
            print(msg)
    diff = pairwise_diff(garden_results)
    full_output += print_grid(servers, diff, verbose)

    return diff, garden_results, full_output


# https://en.wikipedia.org/wiki/List_of_Unicode_characters
def get_common_unicode():
    return  list(string.ascii_letters) + \
            list(string.digits) + \
            list(".<>@,:\\\"") + \
            list("!#$%&'*+/=?^_`{|}~-\r\n \t") + ['\x00', '\x01', '\x02']

    #return basic_latin + new_lines

#def get_base_unicode():
#    basic_latin = list(range(0x00, 0x7E+1))
#    return [chr(a) for a in basic_latin]


def fuzz_addr(lex_filename: str="addrspec.l",
              servers: List=[str],
              output_dir: str="./output",
              recpto_mailfrom: int=0,
              verbose: bool=False
              ):

    #flex_a = Flexparser(get_base_unicode())
    #mma = flex_a.yyparse(filename)

    #print("---")
    #print(mma)
    #model_name = "model_b-" + filename.replace('.', '_')
    #mma.save(model_name + ".txt")

    #request = "root@google.com"
    #print("T", mma.consume_input(request))

    #request = "@router1,@router2:\"a+b=c\"@mail.host.net"
    #print("T", mma.consume_input(request))

    #  ---------------------------------

    flex_a = Flexparser(get_common_unicode())
    mma = flex_a.yyparse(lex_filename)

    print("---")
    print(mma)
    #model_name = "model_" + filename.replace('.', '_')
    #mma.save(model_name + ".txt")
    print("---")

    if not setup_output_dir(output_dir):
        exit(1)

    cov_addr = DDFACoverage(mma)

    query_id = 0

    region_method = None
    if recpto_mailfrom == 0:
        region_method = test_mailfrom
    else:
        region_method = test_recpto

    #all_interesting = []
    requests = [
                "<google.com>", 
                "<@google.com>", "<a@google.com>",
                "<@router1,@router2:\"a+b=c\"@mail.host.net>"
                ]
    full_cnt = 0
    for seed in requests:
        full_cnt, query_id,_ = fuzz_dfa(mma, full_cnt,
                                        seed, cov_addr,
                                        servers, output_dir, query_id, 
                                        region_method,
                                        verbose=verbose)
    #    for s in interesting:
    #        if s not in all_interesting:
    #            all_interesting.append(s)

    #print("")
    #print("NEXT_INTERESTING:")
    #for q in all_interesting:
    #    print(q)

    #print("Full queries sent:", full_cnt)


def fuzz_body(lex_filename: str="databody.l",
              servers: List=[str],
              output_dir: str="./output",
              verbose: bool=False
              ):
    flex_a = Flexparser(get_common_unicode())
    mma = flex_a.yyparse(lex_filename)

    if not setup_output_dir(output_dir):
        exit(1)

    cov_addr = DDFACoverage(mma)

    query_id = 0

    requests = ["xxx\r\n.\r\nxx",
                "xxx\rxx\r\n.\r\nxx",
                "xxx\r\nxx\r\n.\r\nxx",
                "xxx\r\n.\rxx\r\n.\r\nxx"
                ]

    full_cnt = 0
    for seed in requests:
        full_cnt, query_id,_ = fuzz_dfa(mma, full_cnt,
                                        seed, cov_addr,
                                        servers, output_dir, query_id, 
                                        test_body,
                                        verbose=verbose)



def main():
    parser = argparse.ArgumentParser('fuzz_dfa_addr-body.py.py', 
                                     description='Lexer based SMTP fuzzing driver')
    parser.add_argument("mode", help="<mailfrom|recpto|data>")
    parser.add_argument("-o", dest="output_dir", 
                        default="output")
    args = parser.parse_args()

    servers = [
            "msmtp", 
            "nullmailer", 
            "aiosmtpd", 
            "exim", 
            "postfix", 
            #"opensmtpd",  # weird resending
            "james-maildir",
            ]

    if args.mode == "mailfrom":
        fuzz_addr("addrspec.l", servers, args.output_dir, 
                  recpto_mailfrom=0,    # 0 -> MAILFROM, 1 -> RECPTO
                  verbose=False)
    elif args.mode == "recpto":
        fuzz_addr("addrspec.l", servers, args.output_dir, 
                  recpto_mailfrom=1,    # 0 -> MAILFROM, 1 -> RECPTO
                  verbose=False)
    elif args.mode == "data":
        fuzz_body("databody.l", servers, args.output_dir, 
                  verbose=False)
    else:
        print("ERROR: unsupported mode <mailfrom|recpto|data>")
        exit(1)
    

if __name__ == '__main__':
    main()

