# -*- coding: utf-8 -*-
"""Runner.

- Author: Curt Park
- Contact: www.jwpark.co.kr@gmail.com
"""

import argparse

parser = argparse.ArgumentParser(description="Stock price scraper and optimizer.")
parser.add_argument("--module", type=str, required=True, help="Target modul to run")
parser.add_argument("--config", type=str, required=True, help="configuration file name")
args = parser.parse_args()


# load configurations
print("[INFO] Loading configurations", args.config)
config = getattr(__import__("config." + args.config, fromlist=[args.config]), "config")
print(config)
print()

# load a module
print("[INFO] Loading a module", args.module)
module = __import__("source." + args.module, fromlist=[args.module])
print(module)
print()

# run a module
module.run(config)
