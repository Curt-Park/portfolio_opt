# -*- coding: utf-8 -*-
"""Configurations for IRP.

- Author: Curt Park
- Contact: www.jwpark.co.kr@gmail.com
"""

from datetime import datetime

config = dict(
    {
        "TICKERS": [
            "143850.KS",  # Tiger S&P500 Futures ETF
            "195980.KS",  # Arirang MSCI Emerging Markets ETF
            "148070.KS",  # KOSEF 10yr KTB
            "153130.KS",  # KODEX KRW Cash
        ],
        "START": datetime(1900, 1, 1),
        "END": datetime.now(),
    }
)
