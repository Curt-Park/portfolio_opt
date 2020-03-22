# -*- coding: utf-8 -*-
"""Stock price optimizer.

- Author: Curt Park
- Contact: www.jwpark.co.kr@gmail.com
- Reference: https://github.com/robertmartin8/PyPortfolioOpt
"""


import argparse
import os

import pandas as pd
from pypfopt import EfficientFrontier, expected_returns, risk_models

parser = argparse.ArgumentParser(description="Stock price optimizer.")
parser.add_argument("--config", type=str, default="irp", help="configuration file name")
parser.add_argument("--save", dest="save", action="store_true", help="save weights")
args = parser.parse_args()


# read in price data
filepath = os.path.join("data", args.config + ".csv")
print("[INFO] Read a csv file from", filepath)
df = pd.read_csv(filepath, parse_dates=True, index_col="Date")
print(df, "\n")

# load configurations
config = getattr(__import__("config." + args.config, fromlist=[args.config]), "config")

# calculate expected returns and sample covariance
mu = expected_returns.mean_historical_return(df)
S = risk_models.sample_cov(df)

# optimize for maximal Sharpe ratio
ef = EfficientFrontier(mu, S, gamma=config["GAMMA"])
raw_weights = ef.max_sharpe()

# check the results
cleaned_weights = ef.clean_weights()
print(cleaned_weights)
ef.portfolio_performance(verbose=True)
print()

if args.save:
    filepath = os.path.join("data", args.config + "_weight.csv")
    ef.save_weights_to_file(filepath)  # saves to file
    print("[INFO] Saved weights as", filepath)
