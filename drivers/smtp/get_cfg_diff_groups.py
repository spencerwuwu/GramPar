#!/usr/bin/env python3
import sys
import os
import json
import argparse
from typing import Tuple, Dict

from smtpfuzz.fuzz import pairwise_diff


def smtp_two_diff(pa: Tuple[bool, Tuple[str, str]], 
                  pb: Tuple[bool, Tuple[str, str]])-> bool:
    if not pa[0] or not pb[0]:
        return True
    # Sanitize done in query_garden_full
    return pa[0] == pb[0] and pa[1] == pb[1]



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
        query_f = os.path.join(f"{path}/../query", query_id)
        with open(query_f, "r") as fd:
            data = fd.read()
            if "HEAD" not in data and "TAIL" not in data:
                continue

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

    # NOTE: this means it's mma rejected
    #print("All acc:")
    #for a in all_same:
    #    print(a)

    #print()
    #print()
    #print("----")
    #print("All diff:")


    groups = {}

    for (query_id, char, d_id)  in sorted(diff_sets, key=lambda x: x[0]):
        if query_id in all_same:
            #print(f"{query_id:4d}", char, "**")
            continue
        #payload_f = f"{path}/..//query/{query_id}"
        #data = b""
        #with open(payload_f, "r") as fd:
        #    for line in fd:
        #        data += codecs.escape_decode(bytes(line, "utf-8"))[0] + b"\n"
        #parsers = [
        #           # c-sharp
        #           "mimekit-parser",
        #           # java
        #           "apache-common-parser",
        #           # pyp
        #           "php-mime-mail-parser",
        #           # js
        #           "mailparser-parser",
        #           "postal-mime-parser",
        #           # python
        #           "email-parser",
        #           #"flanker-parser",
        #           #"mail-parser-parser"
        #           ]
        #_, results,_ = test_mime_parser(
        #    parsers, data, verbose=True)

        # Read prev result
        with open(f"{path}/../output/{query_id}", "r") as fd:
            results = json.load(fd)

        del results["nullmailer"]


        #if int(query_id) in [30]:
        #    print(results["postfix"][1][0], '<"' in results["postfix"][1][0])
        #    exit()

        for key in results:
            if not results[key][0]:
                continue
            # msmtp adds a newline at the end of data
            results[key][1][1] = results[key][1][1].replace("\n", "")
            results[key][1][0] = results[key][1][0].replace("\n", "")

            # postfix adds "" for email address
            results[key][1][0] = results[key][1][0].replace('<"', "<")
            results[key][1][0] = results[key][1][0].replace('"@', "@")

            # Remove the ".>" in <user1@gmail.com.>
            results[key][1][0] = results[key][1][0].replace('.>', ">")


        diff = pairwise_diff(results, smtp_two_diff)

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
    parser = argparse.ArgumentParser('get_cfg_diff_groups.py', 
                                     description='Group discrenpencies by mutation rules')
    parser.add_argument("output_dir")
    args = parser.parse_args()
    main(args.output_dir)

