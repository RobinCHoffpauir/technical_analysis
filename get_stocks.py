# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import yfinance as yf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
t = pd.DataFrame()
close = pd.DataFrame()


class Stocks:
    def __init__(self, ticker1, start, end=None, ticker2=None, ticker3=None, ticker4=None):
        Stocks.ticker1 = ticker1
        Stocks.ticker2 = ticker2
        Stocks.ticker3 = ticker3
        Stocks.ticker4 = ticker4
        Stocks.start = start
        Stocks.end = end
        if '__name__' == '__init__':
            Stocks()

    def get_stocks(ticker1, start, multipleplots=None, end=None, ticker2=None, ticker3=None, ticker4=None):
        """


        Parameters
        ----------
        ticker1 : TYPE-['str']
        -a single  stock ticker symbol(s) ex.'msft'.

        start : TYPE-datetime
        -iso format of datetime that is the first day that stock data will be collected.

        multipleplots : TYPE-Boolean (True/False)
        -OPTIONAL-True=each stock displays seperate plot, False=stocks display on one plot.

        end : TYPE-datetime
        -OPTIONAL-iso format of datetime that is the last day that stock data will be collected.

        ticker2 : TYPE-['str']
        -OPTIONAL-a single  stock ticker symbol(s) ex.'msft'

        ticker3 : TYPE-['str']
        -OPTIONAL-a single  stock ticker symbol(s) ex.'msft'

        ticker4 : TYPE-['str']
        -OPTIONAL-a single  stock ticker symbol(s) ex.'msft'
        ----------
        Returns :
            a plot (or subplots) & 
            pandas dataframe
            columns - open, close, adj close, high,
            and low stock prices for respective day.

        """
        global t
        global close
        ticks = list([ticker1, ticker2, ticker3, ticker4])
        tickersInUpCases = [elem.upper() for elem in ticks]
        t = yf.download(tickersInUpCases, start=start, end=end)
        close = t.get('Close')
        return close.plot.area(subplots=multipleplots, title=False)

    def chart_stocks(self, ticker1, start, end=None, ticker2=None, ticker3=None, ticker4=None):
        sns.lineplot(x=t.index, y=t['Close'])
