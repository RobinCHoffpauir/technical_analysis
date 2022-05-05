import yfinance as yf



x = yf.download('btc-usd', period='2y', interval='1d')
print(x)