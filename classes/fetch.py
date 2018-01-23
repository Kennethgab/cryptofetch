# fetch code
import asyncio
import aiohttp
import constants
import json
from fake_useragent import UserAgent



class async_scraper:
	def __init__(self):
		self.user_agent = UserAgent()


	async def _fetch(self,symbol, url, session):
		if symbol:
			url = url.format(symbol = symbol)
			
		async with session.get(url) as resp:
			return await resp.json()


	async def run(self, symbols,url):

		tasks = []

		async with aiohttp.ClientSession(headers = {'content-type': 'application/json', 'User-agent' : self.user_agent.random}) as session:
			if symbols is False:
				
				task = asyncio.ensure_future(self._fetch(False, url, session))
				tasks.append(task)
			else:
				for symbol in symbols:
					
					task = asyncio.ensure_future(self._fetch(symbol, url, session))
					tasks.append(task)


			responses = await asyncio.gather(*tasks)
			return responses


