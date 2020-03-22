# -*- coding: utf-8 -*-
"""Stock price getter.

- Author: Curt Park
- Contact: www.jwpark.co.kr@gmail.com
"""


import argparse
from datetime import datetime
import os

import pandas as pd
import plotly.graph_objs as go

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
traces = []
for ticker in config["TICKERS"]:
    print(f"[INFO] Scraping {ticker} prices...")
    df = get_stock_prices(ticker, config["START"], config["END"])
    print(df)
    traces.append(go.Scatter(x=df.index, y=df.Close, name=ticker))
    print(f"[INFO] Scraping {ticker} prices done.\n")

# plot graphs
if args.plot:
    plot_line_graphs(traces)
