# GramPar: Grammar-based Differential Testing of Network Protocol Parsers
Artifact for the paper "GramPar: Grammar-based Differential Testing of Network Protocol Parsers" 
submitted to the 47th IEEE Symposium on Security and Privacy (S&P 2025).


## Installation
### Requirements
- Python 3.8+
- docker

### Instructions
1. Clone the repository recursively:
   ```bash
   git clone --recurse-submodules
   ```

## Directories
- `grampar/`: The main GramPar framework for grammar-based differential testing.
- `targets/`: Contains the *MIME* and *SMTP* protocol parser targets used in the evaluation.

```bash
./cfg2cnf/cfg2cnf.py grampar/src/grampar/antlr_drivers/mime/MimeParser.g4 CFG_mime.txt mimeMessage
```

```
docker compose build soil
docker compose build echo postfix msmtp exim opensmtpd nullmailer aiosmtpd james-maildir
```

## References
This repository contains/use code from several prior works
- [Sfalearn](https://github.com/GeorgeArgyros/sfalearn): Scripts by George Argyros et al. for DFA construction (G. Argyros, I. Stais, S. Jana, A. D. Keromytis, and A. Kiayias. 2016. SFADiff: Automated Evasion Attacks and Fingerprinting Using Black-box Differential Automata Learning. In Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security (CCS '16). ACM, New York, NY, USA, 1690-1701. doi: 10.1145/2976749.2978383)
- [SMTP Garden](https://github.com/kenballus/smtp-garden): An open-source framework for testing SMTP servers.
- [MIMEminer](https://github.com/MIME-miner/MIMEminer): Base code for differential testing of MIME parsers. (Zhang, Jiahe, et al. "Inbox invasion: Exploiting mime ambiguities to evade email attachment detectors." Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security. 2024.)
- [pyformlang](https://github.com/Aunsiels/pyformlang): A Python library for formal languages and automata theory by Julien Romero for the CYK algorithm implementation.
