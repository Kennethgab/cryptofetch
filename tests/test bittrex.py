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
agent_string = ua.random
header_bit = constants.BITTREX_HEADER
header_bit['User-Agent'] = agent_string
loop = asyncio.get_event_loop()

future = asyncio.ensure_future(scraper.run(market,constants.BITTREX_CURRENCY,header_bit))

loop.run_until_complete(future)

print(future.result())







