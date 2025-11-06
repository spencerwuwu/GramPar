#!/usr/bin/env python
import argparse
import sys
import codecs
from loguru import logger
from mime_tester import test_mime_parser

logger.remove()
logger.add(sys.stderr, 
       filter={
           "": "INFO",
         }
       )

def main():
    parser = argparse.ArgumentParser('rerun_query.py', 
                                     description='Get the result of parsing MIME')
    parser.add_argument("file")
    args = parser.parse_args()

    # NOTE: intput query
    file = args.file

    with open(file, 'rb') as f:
        content = f.read()
        data = codecs.escape_decode(content)[0]

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
    _, _, log = test_mime_parser(parsers, data, verbose=True)


if __name__ == '__main__':
    main()


