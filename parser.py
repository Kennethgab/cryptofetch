import argparse
import constants
import classes.fetch
import aiohttp
import asyncio
from classes.cmchandler import CmcHandler
from classes.bittrexhandler import BittrexHandler
import json




parser = argparse.ArgumentParser(
	description = "Cryptofetch program"
)


parser.add_argument('action', help =  "actions: price, summary.")
parser.add_argument('market', help = "provide market to fetch from: cmc( coinmarketcap) , bittrex, all", default = "cmc")
parser.add_argument('currencies', help = 'enter currency, or currencies, if needed. example: "bitcoin ethereum", in quotations. ', default = False)


args = parser.parse_args()

market = str(getattr(args,"market")).lower()
action = str(getattr(args,"action")).lower()
currencies = str(getattr(args,"currencies"))



cmcflag = False
bittrexflag = False

cmchandler = CmcHandler()
bittrexhandler = BittrexHandler()

if market == "cmc":
	cmcflag = True
elif market =="bittrex":
	bittrexflag = True
else:
	cmcflag,bittrexflag = True,True

future = None
if action == "price":

	currencies = currencies.split(" ")

	future = asyncio.ensure_future(cmchandler.get_currency(currencies))

loop = asyncio.get_event_loop()
loop.run_until_complete(future)
coins = future.result()
for coin in coins:
	for price in coin:
		print("{} : {}".format(price['name'],price['price_usd']))













