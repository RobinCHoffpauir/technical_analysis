# -*- coding: utf-8 -*-
"""
Created on Wed May  4 00:10:47 2022

@author: robin
"""

# %%
!pip install mplfinance
!pip install finta

# %%
import yfinance as yf, mplfinance as mpf, finta as fta, numpy as np, matplotlib.pyplot as plt
from finta import TA
slow = '20d'
fast = '8d'
efoi = yf.download('efoi',period='1y', interval='1d')
amd = yf.download('amd',period='1y',interval='1d')


# %% plot 8ema and 20 ema with RSI
fig,(ax1, ax2) = plt.subplots(2)
amd['RSI'] = TA.RSI(amd)
amd['20_ema'] = TA.EMA(amd, 20)
amd['8_ema'] = TA.EMA(amd, 8)
amd['Signal'] = 0.0
amd['Signal'] = np.where(amd['20_ema'] > amd['8_ema'], 1.0, 0.0)
amd['Position'] = amd['Signal'].diff()
ax1.plot(amd[['20_ema','8_ema','Close']])
ax1.legend(amd[['20_ema','8_ema','Close']])
ax1.set_title('8 day & 20 day EMA')
ax2.plot(amd['RSI'][4:],color='r')
fig.text(.68,.35,'< 40 = undervalued')
fig.text(.68,.40,'> 60 = overvalued')
# %%
amd[['MACD','Sig']]=TA.MACD(amd, period_fast=8, period_slow=20)


# %%
plt.figure(figsize = (20,10))
# plot Close, short-term and long-term moving averages
amd['Close'].plot(color = 'y', label= 'Close')
amd['8_ema'].plot(color = 'b',label = '8-day SMA')
amd['20_ema'].plot(color = 'g', label = '20-day EMA')

# plot ‘buy’ signals
plt.plot(amd[amd['Position'] == 1].index,
         amd['8_ema'][amd['Position'] == 1],
         'v', markersize = 15, color = 'r', label = 'sell')

# plot ‘sell’ signals
plt.plot(amd[amd['Position'] == -1].index,
         amd['8_ema'][amd['Position'] == -1],
         '^', markersize = 15, color = 'g', label = 'buy')
plt.ylabel('Price in USD', fontsize = 20 )
plt.xlabel('Date', fontsize = 20 )
plt.title('AMD', fontsize = 40)
plt.legend()
plt.grid()
plt.show()

# %% get bollinger bands
bbands = TA.BBANDS(amd)
bands = TA.BBANDS(efoi)
efoi_df = mpf.plotting.make_addplot(efoi)
amd_df = mpf.plotting.make_addplot(amd)

#fill na with 0
bbands = bbands.fillna(0)
bands = bands.fillna(0)
# %% attach bollinger bands to DFs
amd[['BB_Upper','BB_Middle','BB_Lower']] = bbands
efoi[['BB_Upper','BB_Middle','BB_Lower']] = bands
# %%using mplfinance to plot with OHLC chart
mpf.plot(amd)
mpf.plot(efoi)

# %% using matplotlib to plot DFs with Bollingerbands
fig, (ax1,ax2) = plt.subplots(2)
ax1.plot(amd[['BB_Upper','BB_Lower','Close']][19:])
fig.text(.70,.80, 'Ticker: AMD', fontsize=15)
ax2.plot(efoi[['BB_Upper','BB_Lower','Close']][19:])
fig.text(.70,.35, 'Ticker: EFOI', fontsize=15)
# %%
