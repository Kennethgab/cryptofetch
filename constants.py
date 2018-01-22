#Constants


# CoinMarketCap
# https://coinmarketcap.com/api/

CMC_TICKER   = "https://api.coinmarketcap.com/v1/ticker/"
CMC_GLOBAL   = "https://api.coinmarketcap.com/v1/global/"
CMC_CURRENCY = "https://api.coinmarketcap.com/v1/ticker/{symbol}/"




# Bittrex
# https://bittrex.com/home/api

#parameters:
# market: for example BTC-LTC
# type: type=buy, type=sell or type=both ( buy and sell=)

BITTREX_GETMARKETS    = "https://bittrex.com/api/v1.1/public/getmarkets"
BITTREX_GETCURRENCIES = "https://bittrex.com/api/v1.1/public/getcurrencies"
BITTREX_CURRENCY      = "https://bittrex.com/api/v1.1/public/getticker?market={symbol}" 
BITTREX_MARKETSUMMARY = "https://bittrex.com/api/v1.1/public/getmarketsummary?market={symbol}"
BITTREX_ORDERBOOK     = "https://bittrex.com/api/v1.1/public/getorderbook?market={symbol}&type=both"
BITTREX_MARKETHISTORY = "https://bittrex.com/api/v1.1/public/getmarkethistory?market={symbol}"




#Bitfinex
# https://bitfinex.readme.io/v2/reference

#bitfinex can fetch several markets/tickers at once
# tBTCUSD fetches BTC to USD
# tLTCUSD fetcheds LTC to USD
# can be combined like tBTCUSD,LTCUSD in {markets} to fetch both at once
# precision available values: "P0", "P1", "P2", "P3", "R0"
#Timeframe Available values: '1m', '5m', '15m', '30m', '1h', '3h', '6h', '12h', '1D', '7D', '14D', '1M'
#Section available values: "last", "hist"

BITFINEX_TICKERS = "https://api.bitfinex.com/v2/tickers?symbols={symbols}"
BITFINEX_TICKER  = "https://api.bitfinex.com/v2/ticker/{symbol}"
BITFINEX_TRADES  = "https://api.bitfinex.com/v2/trades/{symbol}/hist"
BITFINEX_BOOKS   = "https://api.bitfinex.com/v2/book/{symbol}/{precision}" 
BITFINEX_CANDLES = "https://api.bitfinex.com/v2/candles/trade::{timeframe}::{symbol}/{section}"



# GDAX
# https://docs.gdax.com/
GDAX_CURRENCIES  = "https://api-public.sandbox.gdax.com/currencies"
GDAX_PRODUCTS    = "https://api-public.sandbox.gdax.com/products"
GDAX_TICKER      = "https://api-public.sandbox.gdax.com/products/{symbol}/ticker"
GDAX_TRADES      = "https://api-public.sandbox.gdax.com/products/{symbol}/trades"
GDAX_CANDLES     = "https://api-public.sandbox.gdax.com/products/{symbol}/candles"
GDAX_STATS       = "https://api-public.sandbox.gdax.com/products/{symbol}/stats"

# gdax headers:



# 

