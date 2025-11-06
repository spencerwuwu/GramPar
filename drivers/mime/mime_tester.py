#!/usr/bin/env python
import sys
import os
import string
import glob
import random
import shutil
import codecs
import docker
from typing import List, Tuple, Dict, Mapping

from loguru import logger

from grampar.utils import pairwise_diff, print_grid

"""
  Configurations
"""
MIME_CONTAINER_NAME = "mime-garden-container"

MIME_GARDEN_PATH = os.getenv("MIME_GARDEN_PATH", "")
if not MIME_GARDEN_PATH:
    print("MIME_GARDEN_PATH environment variable is not set.")
    exit(1)
if not os.path.exists(f"{MIME_GARDEN_PATH}/garden-io"):
    print(f"{MIME_GARDEN_PATH} does not exists")
    exit(1)

IGNORE_FILENAME = True

fuzz_targets = {
    "mimekit-parser": {
        "name": "mimekit-parser",
        "cwd": "csharp/mimekit-parser",
        "execute_str": "dotnet run ---project mimekit-parser.csproj -i {input_path} -o {output_path}",
    },
    "apache-common-parser": {
        "name": "apache-common-parser",
        "cwd": "java/apache-common-parser/target",
        "execute_str": "java -jar MimeKit-parser-1.0-SNAPSHOT.jar -i {input_path} -o {output_path}",
    },
    "php-mime-mail-parser": {
        "name": "php-mime-mail-parser",
        "cwd": "php/php-mime-mail-parser",
        "execute_str": "php index.php -i {input_path} -o {output_path}",
    },
    "mailparser-parser": {
        "name": "mailparser-parser",
        "cwd": "javascript/mailparser-parser",
        "execute_str": "node index.js -i {input_path} -o {output_path}",
    },
    "postal-mime-parser": {
        "name": "mailparser-parser",
        "cwd": "javascript/postal-mime-parser",
        "execute_str": "node index.mjs {input_path} {output_path}",
    },
    "email-parser": {
        "name": "email-parser",
        "cwd": "python/email-parser",
        "execute_str": "python3 main.py -i {input_path} -o {output_path}",
    },
}


def get_container(container_name):
    client = docker.from_env()
    try:
        container = client.containers.get(container_name)
        return container
    except Exception as e:
        print(f"failed to get container id for {container_name}", file=sys.stderr)
        print(f"reason: {e}", file=sys.stderr)
        sys.exit(1)


def get_mime_parser_result(output_dir: str)-> Tuple[bool, Mapping[str, bytes]]:
    """
    Returns: Mapping[<filename: str>, Tuple[<has_attch: bool>, <content: bytes>]]
    """
    def san(value):
        value = value.replace(b"\r\n", b"\n")
        value = value.replace(b" ", b"")
        # Special handling particularly for postal
        if value.endswith(b"\n\n"):
            value = value[:-1]
        if value.endswith(b"\n"):
            value = value[:-1]
        return value
    results = {}
    if IGNORE_FILENAME:
        output_dir = f"{output_dir}/content/"
    file_paths = sorted(glob.glob(os.path.join(output_dir, "**/*"), recursive=True))
    for file_path in file_paths:
        if os.path.isdir(file_path):
            continue
        with open(file_path, "rb") as fd:
            content = fd.read()
        filename = file_path.replace(output_dir, "")
        results[filename] = san(content)
    return (len(results) != 0, results)


def mime_result_diff(pa: Tuple[bool, Dict], pb: Tuple[bool, Dict])-> bool:
    a = pa[1]
    b = pb[1]
    #def san(value):
    #    value = value.replace(b"\r\n", b"\n")
    #    value = value.replace(b" ", b"")
    #    # Special handling particularly for postal
    #    if value.endswith(b"\n\n"):
    #        value = value[:-1]
    #    if value.endswith(b"\n"):
    #        value = value[:-1]
    #    return value
    if len(a) != len(b):
        return False
    k_as = a.keys()
    k_bs = b.keys()
    if sorted(k_as) != sorted(k_bs):
        return False
    for ka, va in a.items():
        if ka not in b:
            return False
        #san_va = san(va)
        #san_vb = san(b[ka])
        #if san_va != san_vb:
        #    return False
        if va != b[ka]:
            return False
    return True


def test_mime_parser(parsers: List[str],
                     mime: str|bytes,
                     verbose: bool=False
                     )-> Tuple[Mapping[str, bool],
                               Mapping[str, Tuple[bool, str]], 
                               str]:
    def _get_rand_str(size=5):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

    container = get_container(MIME_CONTAINER_NAME) 

    rand_str = _get_rand_str()
    workdir = f"{MIME_GARDEN_PATH}/garden-io/mime-{rand_str}/"
    if os.path.isdir(workdir):
        rand_str = _get_rand_str()
        workdir = f"{MIME_GARDEN_PATH}/garden-io/mime-{rand_str}/"
        #shutil.rmtree(workdir)

    output_dir = f"{workdir}/output"
    os.makedirs(output_dir, exist_ok=True)

    mime_file = f"{workdir}/mime_file"

    # Write the mime to a tmp file
    with open(mime_file, "wb") as fd:
        if type(mime) == str:
            fd.write(mime.encode('utf8'))
        else:
            fd.write(mime)

    mime_results = {}
    full_output = ""
    #logger.info("Querying MIME and store at {}...", output_dir)
    logger.info("Querying MIME")
    if verbose:
        logger.info("Output Dir {}", output_dir)
    # Make output_dir for each parser and run
    for parser in parsers:
        p_outdir = f"{output_dir}/{parser}/"
        os.makedirs(p_outdir, exist_ok=True)

        container_file = mime_file.replace(MIME_GARDEN_PATH, "/")
        container_outdir = p_outdir.replace(MIME_GARDEN_PATH, "/")
        target = fuzz_targets[parser]
        cmd = target["execute_str"].format(input_path=container_file, 
                                           output_path=container_outdir)
        cwd = target["cwd"]
        docker_cmd = f"/bin/bash -c \"cd {cwd} && {cmd}\""

        client = docker.from_env()
        try:
            logger.debug(f"[*] Running: {cmd}")
            exec_log = client.api.exec_create(container.id, docker_cmd)
            output = client.api.exec_start(exec_log['Id']).decode()
            logger.debug(f"[*] Output:\n{output}")
        except Exception as e:
            logger.error(f"failed to run {docker_cmd}")
            logger.error(f"reason: {e}")

        mime_results[parser] = get_mime_parser_result(p_outdir)
        msg = f"\n* {parser}:\n" + repr(mime_results[parser][1]) + "\n"
        full_output += msg + "\n" + "-"*10 + "\n"

    diff = pairwise_diff(mime_results, mime_result_diff)
    full_output += print_grid(parsers, diff, verbose=False)

    # Need to serialize mime_results before returning & storing
    for k in mime_results:
        has_attch, contents = mime_results[k]
        repr_contents = {}
        for fk in contents:
            repr_contents[fk] = codecs.escape_encode(contents[fk])[0].decode()
        mime_results[k] = (has_attch, repr_contents)

    if not verbose:
        shutil.rmtree(workdir)
    if not all(diff.values()):
        logger.debug("++ DIFF!")
        logger.debug("\n{}", mime)
    if verbose:
        print(full_output)
    return diff, mime_results, full_output


def main():
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

    seed_dir = "./seeds_mime-simple/"

    seeds = []
    for f in os.listdir(seed_dir):
        with open(f"{seed_dir}/{f}", "r") as fd:
            #data = fd.read().replace("\n", "\r\n")
            data = fd.read()
            seeds.append(data)

    for seed in seeds:
        test_mime_parser(parsers, seed, verbose=True)


if __name__ == '__main__':
    logger.remove()
    logger.add(sys.stderr, 
               filter={
                   "": "INFO",
                   #"": "DEBUG",
                 }
               )
    main()
