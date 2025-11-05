#!/usr/bin/env python3
import sys
import os
import json
import argparse
from typing import Tuple, Dict

from grampar.utils import pairwise_diff


def non_empty_diff(pa: Tuple[bool, Dict], pb: Tuple[bool, Dict])-> bool:
    if not pa[0] or not pb[0]:
        return True
    if pa[1].keys() != pb[1].keys():
        return False
    for k in pa[1].keys():
        if pa[1][k] != pb[1][k]:
            return False
    return True


def main(output_dir):
    path = f"{output_dir}/pairwise_json"
    if not os.path.exists(path):
        print(f"Path {path} does not exist.")
        sys.exit(1)

    all_same = []
    diff_sets = []
    diff_values = []
    diff_uniques = []

    for query_id in os.listdir(path):
        full_path = os.path.join(path, query_id)
        with open(full_path, "r") as file:
            data = json.load(file)
            mutate = data.pop("MUTATE", None)
            if all(data.values()):
                all_same.append(int(query_id))

            if (mutate, data) not in diff_values:
                s = repr(mutate[0])
                diff_values.append((mutate, data))
                if data in diff_uniques:
                    d_idx = diff_uniques.index(data)
                else:
                    d_idx = len(diff_uniques)
                    diff_uniques.append(data)
                diff_sets.append((int(query_id), f"{s:5s}", d_idx))

    groups = {}

    for (query_id, char, d_id)  in sorted(diff_sets, key=lambda x: x[0]):
        if query_id in all_same:
            #print(f"{query_id:4d}", char, "**")
            continue

        # Read prev result
        with open(f"{path}/../output/{query_id}", "r") as fd:
            results = json.load(fd)

        diff = pairwise_diff(results, non_empty_diff)

        key = char.split("-")[0]
        if not all(diff.values()):
            if key not in groups:
                groups[key] = []
            groups[key].append((query_id, char))
            #print(f"{query_id:4d}", char)

    for k, v in groups.items():
        print(f"Group {k}:")
        for (query_id, diff) in v:
            print(f"  {query_id:4d} {diff}")

    with open(path.rsplit("pairwise_json", 1)[0] + "refined_id.txt", "w") as fd:
        for k, v in groups.items():
            for (query_id, diff) in v:
                fd.write(f"{query_id:4d}\n")




if __name__ == '__main__':
    parser = argparse.ArgumentParser('get_diff_groups.py', 
                                     description='Group discrenpencies by mutation rules')
    parser.add_argument("output_dir")
    args = parser.parse_args()
    main(args.output_dir)

