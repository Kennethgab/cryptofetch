# Bittrex

import constants
import classes.fetch
import aiohttp
import asyncio
from classes.cmchandler import CmcHandler
from classes.bittrexhandler import BittrexHandler
import json


symbols = ["BTC"]

handler =  CmcHandler()

loop = asyncio.get_event_loop()

future = asyncio.ensure_future(handler.get_global())



loop.run_until_complete(future)


print(future.result())