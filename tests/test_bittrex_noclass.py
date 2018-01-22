import asyncio
import aiohttp
import constants
import fetch
from fake_useragent import UserAgent
import os
import time


market = ["BTC-LTC", "BTC-XRP", "BTC-OMG"]

scraper = fetch.async_scraper()

ua = UserAgent()
header_bit = constants.BITTREX_HEADER

loop = asyncio.get_event_loop()

 # test btc-ltc, btc- xrp, btc-omg JSON response

print()
print("get currency: ")
print("-"*50)

future = asyncio.ensure_future(scraper.run(market,constants.BITTREX_CURRENCY,header_bit,ua))
loop.run_until_complete(future)
print(future.result())

print()
print("Market summary: ")
print("-"*50)

# test market summary

future = asyncio.ensure_future(scraper.run(market,constants.BITTREX_MARKETSUMMARY,header_bit,ua))
loop.run_until_complete(future)
print(future.result())

print()
print("Get Markets: ")
print("-"*50)

# test getmarkets

future = asyncio.ensure_future(scraper.run(False,constants.BITTREX_GETMARKETS,header_bit,ua))
loop.run_until_complete(future)
print(future.result())

print()
print("Get Currencies:")
print("-"*50)

# test getcurrencies

future = asyncio.ensure_future(scraper.run(False,constants.BITTREX_GETCURRENCIES,header_bit,ua))
loop.run_until_complete(future)
print(future.result())

print()
print("Orderbook: ")
print("-"*50)

# test orderbook both
url = constants.BITTREX_ORDERBOOK
future = asyncio.ensure_future(scraper.run(market, url, header_bit, ua))
loop.run_until_complete(future)
print(future.result())

print()
print("Market history: ")
print("-"*50)

# test markethistory

future = asyncio.ensure_future(scraper.run(market,constants.BITTREX_MARKETHISTORY,header_bit,ua))
loop.run_until_complete(future)
print(future.result())



