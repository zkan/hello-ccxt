from datetime import datetime

import ccxt


# List of all available exchange classes
print(ccxt.exchanges)

exchange = ccxt.binance()

symbol = "BTC/USDT"
timeframe = "1h"
limit = 100

# # Open, High, Low, Close and Volume
# ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
# print(ohlcv)

exchange_id = "binance"
exchange_class = getattr(ccxt, exchange_id)

exchange = exchange_class()
ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
print(ohlcv)

timeframe = "1m"
shiba_symbol = "SHIB/USDT"
ohlcv = exchange.fetch_ohlcv(shiba_symbol, timeframe=timeframe, limit=5)
print(ohlcv)

timeframe = "5m"
shiba_symbol = "SHIB/USDT"
dt_obj = datetime.strptime("2022-01-01 9:30:00", "%Y-%m-%d %H:%M:%S")
millisec = int(dt_obj.timestamp() * 1000)
ohlcv = exchange.fetch_ohlcv(shiba_symbol, timeframe=timeframe, since=millisec, limit=5)
print(ohlcv)
