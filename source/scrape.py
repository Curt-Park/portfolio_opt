# -*- coding: utf-8 -*-
"""Stock price getter.

- Author: Curt Park
- Contact: www.jwpark.co.kr@gmail.com
"""


from typing import Any, Dict

import pandas as pd

from source.utils import get_stock_prices, plot_line_graphs


def run(config: Dict[str, Any]) -> None:
    """Scrape stock prices and save as a csv file."""
    # get stock prices
    dfs, traces = [], []
    for ticker in config["TICKERS"]:
        print(f"[INFO] Scraping {ticker} prices...")
        df, trace = get_stock_prices(ticker, config["START"], config["END"])
        print(df)
        dfs.append(df)
        traces.append(trace)
        print(f"[INFO] Scraping {ticker} prices done.\n")

    # merge all dataframes
    print("[INFO] Merging all prices by index")
    df = pd.concat(dfs, axis=1, join="inner")
    df.columns = config["TICKERS"]
    print(df)

    # save dataframes
    df.to_csv(config["PRICE_PATH"])
    print("[INFO] Saved information as", config["PRICE_PATH"])

    # plot graphs
    if config["PLOT"]:
        print("[INFO] Plotting all prices")
        plot_line_graphs(traces)
