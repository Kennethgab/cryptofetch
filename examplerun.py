import argparse
import constants
import classes.fetch
import aiohttp
import asyncio
from classes.cmchandler import CmcHandler
from classes.bittrexhandler import BittrexHandler
import json
import pandas as pd



def extract_cmcCurrencies():
    cmchandler = CmcHandler()
    future = asyncio.ensure_future(cmchandler.get_all_tickers())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(future)
    coins = future.result()[0]
    return pd.DataFrame(coins) 

coins = extract_cmcCurrencies()
print(coins)











