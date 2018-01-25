# dataframe testing


import constants
import classes.fetch
import aiohttp
import asyncio
from classes.cmchandler import CmcHandler
from classes.bittrexhandler import BittrexHandler
import json
import pandas as pd



loop = asyncio.get_event_loop()
handler = CmcHandler()


future = asyncio.ensure_future(handler.get_all_tickers())

loop.run_until_complete(future)

res = future.result()[0]

df = pd.DataFrame(res)

file_name = "dataframe.xlsx"

df.to_excel(file_name, encoding='utf-8')
