# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:30:13 2021

@author: robin
"""

import yfinance as yf
import pandas as pd
from datetime import datetime as datetime


class stock:
    def __init__(self):
        ...

    def stock_metrics(tickers=list()):
        ticker_list = tickers
        tickers = yf.download(ticker_list)
        global metrics
        metrics = pd.DataFrame()
        for ticker in ticker_list:
            info = pd.DataFrame(yf.Ticker(ticker).info.values())
            info = info.transpose()
            info.columns = yf.Ticker(ticker).info.keys()
            metrics = pd.concat([metrics, info])
            metrics.index = metrics['symbol']
        return metrics
