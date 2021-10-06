import ccxt


# List of all available exchange classes
print(ccxt.exchanges)

exchange = ccxt.binance()

symbol = "BTC/USDT"
timeframe = "1h"
limit = 100

ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
print(ohlcv)

exchange_id = "binance"
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class()
ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
print(ohlcv)
