# -*- coding: utf-8 -*-
"""Stock price optimizer.

- Author: Curt Park
- Contact: www.jwpark.co.kr@gmail.com
- Reference: https://github.com/robertmartin8/PyPortfolioOpt
"""


from typing import Any, Dict

import pandas as pd
from pypfopt import EfficientFrontier, expected_returns, risk_models


def run(config: Dict[str, Any]) -> None:
    """Get optimized weights."""
    # read in price data
    print("[INFO] Read a csv file from", config["PRICE_PATH"])
    df = pd.read_csv(config["PRICE_PATH"], parse_dates=True, index_col="Date")
    print(df, "\n")

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

    if config["SAVE_WEIGHTS"]:
        ef.save_weights_to_file(config["WEIGHT_PATH"])  # saves to file
        print("[INFO] Saved weights as", config["WEIGHT_PATH"])
