import os
import codecs
import string
import json
import itertools
import copy
from pathlib import Path
from loguru import logger
from typing import List, Tuple, Dict, Mapping


def get_common_unicode():
    return list(string.printable) + \
            list("\r\n\0") + \
            ['\x01', '\x02', '\x7e']
    basic_latin = list(range(0x00, 0x7E+1))
    return [chr(a) for a in basic_latin]


def store_output(output_dir, query_id, all_cnts, query, diff, output, log)-> int:
    with open(f"{output_dir}/id_log.txt", "a") as fd:
        fd.write(f"{query_id}\t{all_cnts}\n")

    with open(f"{output_dir}/query/{query_id}", "w") as fd:
        bline = query.encode('latin-1')
        export = codecs.escape_encode(bline)[0].decode()
        fd.write(export)
    with open(f"{output_dir}/output/{query_id}", "w") as fd:
        json.dump(output, fd, indent=2)
    with open(f"{output_dir}/pairwise_json/{query_id}", "w") as fd:
        json.dump(diff, fd, indent=2)
    with open(f"{output_dir}/log/{query_id}", "w") as fd:
        fd.write(log)
    return query_id + 1
    

def setup_output_dir(output_dir)-> bool:
    path = Path(output_dir)
    if not path.exists():
        os.makedirs(output_dir, exist_ok=True)
    if not path.is_dir():
        print(f"Error: {output_dir} is not a dir.")
    if any(path.iterdir()):
        print(f"Error: {output_dir} not empty.")
        return False

    os.makedirs(f"{output_dir}/query", exist_ok=True)
    os.makedirs(f"{output_dir}/output", exist_ok=True)
    os.makedirs(f"{output_dir}/pairwise_json", exist_ok=True)
    os.makedirs(f"{output_dir}/log", exist_ok=True)
    return True


def simple_diff(a:bytes, b:bytes)-> bool:
    if a == b:
        return True
    return False


def pairwise_diff(results: Mapping,
                  diff_method=simple_diff)-> Mapping[str, bool]:
    """
    Input:
        results: Mapping[str, {whatever}]
    Output:
        { str(sorted([server_a, server_b])): same/diff }
    """
    # TODO: only compare directly now
    diff = {}
    for server_a, recv_a in results.items():
        for server_b, recv_b  in results.items():
            if server_a == server_b:
                continue
            pair = str(sorted([server_a, server_b]))
            if pair in diff:
                continue
            if recv_a is None or recv_b is None:
                diff[pair] = None
            else:
                diff[pair] = diff_method(recv_a, recv_b) 
    return diff


def print_grid(servers: list[str], results: Mapping[str, bool], verbose=False) -> str:
    """
    Input:
        servers: List of server names
        results: Mapping of the pairwise server name and result compare
    Output:
        -
    """
    labels = copy.deepcopy(servers)
    first_column_width: int = max(map(len, labels))
    labels = [label.ljust(first_column_width) for label in labels]

    printed = set()
    # Vertical labels
    result: str = (
        "".join(
            f'{"".ljust(first_column_width - 1)}{" ".join(row)}\n'
            for row in itertools.zip_longest(
                *(s.strip().rjust(len(s)) for s in [" " * len(labels[0]), *labels]),
            )
        )
        + f"{''.ljust(first_column_width)}+{'-' * (len(labels) * 2 - 1)}\n"
    )

    for label in labels:
        result += label.ljust(first_column_width) + "|"
        for rlabel in labels:
            symbol: str
            if label == rlabel:
                symbol = "\x1b[0;32m-\x1b[0m"
            else:
                pair = str(sorted([label.strip(), rlabel.strip()]))
                if pair in printed:
                    symbol = ' '
                else:
                    if results[pair]:
                        symbol = "\x1b[0;32m✓\x1b[0m"
                    elif results[pair] is None:
                        symbol = "\x1b[0;33m∅\x1b[0m"
                    else:
                        symbol = "\x1b[0;31m✖\x1b[0m"
                    printed.add(pair)
            result += symbol + " "
        
        result += "\n"

    if verbose:
        print(result)
    return result

