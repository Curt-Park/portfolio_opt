# -*- coding: utf-8 -*-
"""Stock price optimizer.

- Author: Curt Park
- Contact: www.jwpark.co.kr@gmail.com
- Reference: https://github.com/robertmartin8/PyPortfolioOpt
"""


import argparse

import pandas as pd
from pypfopt import EfficientFrontier, expected_returns, risk_models

parser = argparse.ArgumentParser(description="Stock price optimizer.")
parser.add_argument("--path", type=str, default="data/irp.csv", help="file path")
args = parser.parse_args()


# read in price data
print("[INFO] Read a csv file from", args.path)
df = pd.read_csv(args.path, parse_dates=True, index_col="Date")
print(df, "\n")

# calculate expected returns and sample covariance
mu = expected_returns.mean_historical_return(df)
S = risk_models.sample_cov(df)

# optimize for maximal Sharpe ratio
ef = EfficientFrontier(mu, S)
raw_weights = ef.max_sharpe()
cleaned_weights = ef.clean_weights()
# ef.save_weights_to_file("weights.csv")  # saves to file
print(cleaned_weights)
ef.portfolio_performance(verbose=True)
