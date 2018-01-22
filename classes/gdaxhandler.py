# GDAX

import constants
from fetch import fetch
import aiohttp
import asyncio

async def get_currencies(session):
	url = constants.GDAX_CURRENCIES
	return await fetch(session, url)


async def get_products(session):
	url = constants.GDAX_PRODUCTS
	return await fetch(session, url)

async def get_ticker(session, id):
	url = constants.GDAX_TICKER.format(product = id)
	return await fetch(session, url)


async def get_trades(session, id):
	url = constants.GDAX_TRADES.format(product = id)
	return await fetch(session, url)

async def get_candles(session, id):
	url = constants.GDAX_CANDLES.format(product = id)
	return await fetch(session, url)

async def get_stats(session, id):
	url = constants.GDAX_STATS.format(product = id)
	return await fetch(session, url)

	





