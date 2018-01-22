import asyncio
import aiohttp
import constants
import classes.fetch
from fake_useragent import UserAgent
import json




class CmcHandler:
	def __init__(self):
		self.user_agent = UserAgent()
		self.scraper = classes.fetch.async_scraper()
		self.headers = constants.CMC_HEADER


	async def get_currency(self, symbols):
		url = constants.CMC_CURRENCY
		future = asyncio.ensure_future(self.scraper.run(symbols,url, self.headers, self.user_agent))
		return await future

	async def get_all_tickers(self):
		url = constants.CMC_TICKER
		future = asyncio.ensure_future(self.scraper.run(False,url, self.headers, self.user_agent))
		return await future

	async def get_global(self):
		url = constants.CMC_GLOBAL
		future = asyncio.ensure_future(self.scraper.run(False,url, self.headers, self.user_agent))
		return await future


