# GramPar: Grammar-based Differential Testing of Network Protocol Parsers
Artifact for the paper "GramPar: Grammar-based Differential Testing of Network Protocol Parsers" 
submitted to the 47th IEEE Symposium on Security and Privacy (S&P 2026).


## Installation
### Requirements
- Python 3.8+
- docker

### Instructions
1. Clone the repository recursively and cd into it
   ```bash
   git clone --recursive https://github.com/spencerwuwu/GramPar
   cd GramPar
   ```
2. Set your UID and GID in `testbeds/smtp-grampar/.env` (obtained from running `id` in your terminal)
3. Build the necessary docker images.
   ```bash
   ./build-docker.sh
   ```
4. Install python library **grampar** and **smtpfuzz**
   ```bash
   cd grampar/; pip install -r requirements-dev.txt; cd ../
   cd testbeds/smtp-grampar; pip install -r requirements-dev.txt
   ```

## Usage
### Testing MIME Parsers
```bash
cd drivers/mime
```

1. Set up `MIME_GARDEN_PATH` to the absolute path where *GramPar/testbeds/mime* is, 
   and start the docker containers.
```bash
export MIME_GARDEN_PATH=/<path_to>/GramPar/testbeds/mime
cd <path_to>/GramPar/testbeds/mime; docker compose up
```

2. Open another shell.
   Run our Automata-based and CFG-based fuzzer.
   Running them without any arguments is also fine as default values are provided.
```bash
./fuzz_dfa_mime.py [-h] [-o OUTPUT_DIR] [-i SEED_DIR] [-l LEXER_FILE]
./fuzz_cfg_mime.py [-h] [-o OUTPUT_DIR] [-i SEED_DIR] [-c CFG_FILE]
```

3. To observe the results listed in our paper, use
```bash
./rerun_query.py diff_queries/<input_id>
```

### Testing SMTP Parsers
```
cd drivers/smtp
```
1. Set up `SMTP_GARDEN_PATH` to the absolute path where *GramPar/testbeds/smtp* is
   and start the docker containers.
```bash
export SMTP_GARDEN_PATH=/<path_to>/GramPar/testbeds/smtp-grampar
cd <path_to>/GramPar/testbeds/mime; docker compose up echo postfix msmtp exim opensmtpd nullmailer aiosmtpd james-maildir
```

2. Open another shell.
   Run our Automata-based and CFG-based fuzzer.
   Running them without any arguments is also fine as default values are provided.
```bash
./fuzz_dfa_addr-body.py.py [-h] [-o OUTPUT_DIR] mode
./fuzz_cfg_mime.py [-h] [-o OUTPUT_DIR] [-c CFG_FILE]
```

3. To observe the results listed in our paper, use
```bash
./run_echo_query.py diff_queries/<input_id>
```

### Converting CFG to CNF 
GramPar requires the grammar to be in Chomsky Normal Form (CNF).
This is done by the scripts in `cfg2cnf` with the following commands:
```bash
./cfg2cnf/cfg2cnf.py grampar/src/grampar/antlr_drivers/mime/MimeParser.g4 drivers/mime/CFG_mime.txt mimeMessage
./cfg2cnf/cfg2cnf.py grampar/src/grampar/antlr_drivers/smtp/SMTPParser.g4 drivers/smtp/CFG_smtp.txt session
```


## Directories
- `grampar/`: The main GramPar framework for grammar-based differential testing.
- `drivers/`: The scripts we use to test MIME and SMTP parsers.
- `testbeds/`: Infrastructures for differential testing parsers.
- `cfg2cnf/`: Grammar format converter for translating ANTLR4 grammar to CNF form.


## References
This repository contains/use code from several prior works
- [Sfalearn](https://github.com/GeorgeArgyros/sfalearn): Scripts by George Argyros et al. for DFA construction (G. Argyros, I. Stais, S. Jana, A. D. Keromytis, and A. Kiayias. 2016. SFADiff: Automated Evasion Attacks and Fingerprinting Using Black-box Differential Automata Learning. In Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security (CCS '16). ACM, New York, NY, USA, 1690-1701. doi: 10.1145/2976749.2978383)
- [SMTP Garden](https://github.com/kenballus/smtp-garden): An open-source framework for testing SMTP servers.
- [MIMEminer](https://github.com/MIME-miner/MIMEminer): Base code for differential testing of MIME parsers. (Zhang, Jiahe, et al. "Inbox invasion: Exploiting mime ambiguities to evade email attachment detectors." Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security. 2024.)
- [pyformlang](https://github.com/Aunsiels/pyformlang): A Python library for formal languages and automata theory by Julien Romero for the CYK algorithm implementation.
