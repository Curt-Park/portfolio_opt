# My portfolio optimizer

## Prerequisites
This repository is tested on Anaconda virtual environment with python 3.7+

```bash
$ conda create -n portfolio_opt python=3.7
$ conda activate portfolio_opt
```

## Installation
First, clone the repository.

```bash
$ git clone https://github.com/Curt-Park/portfolio_opt.git
$ cd portfolio_opt
```
Secondly, install packages required to execute the code. Just type:

```bash
$ make dev
```

## Structure

```bash
.
├── Makefile
├── config  # configurations for portfolios
├── data  # saved prices (csv)
├── source  # modules
│   ├── optimizer.py  # portfolio optimizer
│   ├── scraper.py  # stock price getter
│   └── utils.py  # util functions
├── run.py
└── requirements.txt
```

## Usages

### Add configurations in ./config
```python
# for example, irp.py

from datetime import datetime

config = dict(
    {
        # tickers from https://finance.yahoo.com/
        "TICKERS": [
            "143850.KS",  # Tiger S&P500 Futures ETF
            "195980.KS",  # Arirang MSCI Emerging Markets ETF
            "148070.KS",  # KOSEF 10yr KTB
            "153130.KS",  # KODEX KRW Cash
        ],
        "START": datetime(1900, 1, 1),
        "END": datetime.now(),
        "GAMMA": 0.1,  # L2 regularization weight
        "PLOT": True,
        "SAVE_WEIGHTS": True,
        "PRICE_PATH": "data/irp.csv",
        "WEIGHT_PATH": "data/irp_w.csv",
    }
)
```

### Scraping data from yahoo finanace

It will create a csv file in `data/`.
```bash
$ python run.py --module scrape --config irp
```

### Execute portfolio optimization
Sharpe ratio maximization only supported now.

```bash
$ python run.py --module optimize --config irp

{'143850.KS': 0.32176, '195980.KS': 0.0, '148070.KS': 0.67824, '153130.KS': 0.0}
Expected annual return: 3.9%
Annual volatility: 5.3%
Sharpe Ratio: 0.36
```
