# -*- coding: utf-8 -*-
"""Common utility functions.

- Author: Curt Park
- Contact: www.jwpark.co.kr@gmail.com
"""

from datetime import datetime
from typing import List, Tuple

import pandas as pd
from pandas_datareader import data
import plotly.graph_objs as go
import plotly.offline as offline


def get_stock_prices(
    ticker: str, start: datetime, end: datetime
) -> Tuple[pd.DataFrame, go.Scatter]:
    """Get daily stock prices."""
    df = data.get_data_yahoo(ticker, start=start, end=end).Close

    # remove incomplete rows
    df = df.dropna()

    # sorting
    df = df.sort_index(ascending=True)
    trace = go.Scatter(x=df.index, y=df, name=ticker)

    return df, trace


def plot_line_graphs(traces: List[go.Scatter]) -> None:
    """Plot line graphs of stock prices."""
    layout = dict(
        title="Time Series: closed prices",
        xaxis=dict(
            rangeselector=dict(
                buttons=list(
                    [
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=3, label="3m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=12, label="12m", step="month", stepmode="backward"),
                        dict(step="all"),
                    ]
                )
            ),
            rangeslider=dict(),
            type="date",
        ),
    )

    fig = go.Figure(data=traces, layout=layout)
    offline.plot(fig)
