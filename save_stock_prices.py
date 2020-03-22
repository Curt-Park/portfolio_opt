# -*- coding: utf-8 -*-
"""Stock price getter.

- Author: Curt Park
- Contact: www.jwpark.co.kr@gmail.com
"""


import argparse

import pandas as pd

from utils import get_stock_prices, plot_line_graphs

parser = argparse.ArgumentParser(description="Stock price getter.")
parser.add_argument("--config", type=str, default="irp", help="configuration file name")
parser.add_argument(
    "--plot", dest="plot", action="store_true", help="plot stock prices"
)
args = parser.parse_args()


# load configurations
config = getattr(__import__("config." + args.config, fromlist=[args.config]), "config")

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

# plot graphs
if args.plot:
    print("[INFO] Plotting all prices")
    plot_line_graphs(traces)
