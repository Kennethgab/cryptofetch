# fetch code
import asyncio
import aiohttp
import constants
import json



class async_scraper:
	def __init__(self):
		pass


	async def _fetch(self,symbol, url, session, headers):
		if symbol:
			url = url.format(symbol = symbol)
			
		async with session.get(url) as resp:
			return await resp.json()


	async def run(self, symbols,url, headers,useragent):

		tasks = []

		async with aiohttp.ClientSession(headers = {'content-type': 'application/json', 'User-agent' : useragent.random}) as session:
			if symbols is False:
				
				task = asyncio.ensure_future(self._fetch(False, url, session, headers))
				tasks.append(task)
			else:
				for symbol in symbols:
					
					task = asyncio.ensure_future(self._fetch(symbol, url, session, headers))
					tasks.append(task)


			responses = await asyncio.gather(*tasks)
			return responses


