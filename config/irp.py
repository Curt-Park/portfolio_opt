# -*- coding: utf-8 -*-
"""Configurations for IRP.

- Author: Curt Park
- Contact: www.jwpark.co.kr@gmail.com
"""

from datetime import datetime

config = dict(
    {
        "TICKERS": [
            "219480.KS",  # Kodex S&P500 Futures(H)
            "284430.KS",  # Kodex 200 US Treasury Notes Balanced ETF Fund
        ],
        "START": datetime(2018, 1, 1),
        "END": datetime.now(),
    }
)
