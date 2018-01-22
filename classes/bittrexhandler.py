import asyncio
import aiohttp
import constants
import classes.fetch
from fake_useragent import UserAgent
import json




class BittrexHandler:
	def __init__(self):

		self.user_agent = UserAgent()
		self.scraper = classes.fetch.async_scraper()
		self.headers = constants.BITTREX_HEADER




	async  def get_currency(self, symbols):

		url = constants.BITTREX_CURRENCY

		future = asyncio.ensure_future(self.scraper.run(symbols,url, self.headers, self.user_agent))

		return await future


	async def get_currencies(self):

		url = constants.BITTREX_GETCURRENCIES

		future = asyncio.ensure_future(self.scraper.run(False, url, self.headers, self.user_agent))

		return await future

	async def market_summary(self, symbols):

		url = constants.BITTREX_MARKETSUMMARY

		future = asyncio.ensure_future(self.scraper.run(symbols, url, self.headers, self.user_agent))

		return await future


	async def get_markets(self):

		url = constants.BITTREX_GETMARKETS

		future = asyncio.ensure_future(self.scraper.run(False, url, self.headers, self.user_agent))

		return await future

	async def market_history(self, symbols):

		url = constants.BITTREX_MARKETHISTORY
		future = asyncio.ensure_future(self.scraper.run(symbols, url, self.headers, self.user_agent))

		return await future


	async def get_orderbook(self, symbols):

		url = constants.BITTREX_ORDERBOOK
		future = asyncio.ensure_future(self.scraper.run(symbols, url, self.headers, self.user_agent))
		return await future


		



























