# -*- coding: utf-8 -*-

import asyncio
import os
import sys

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt.async_support as ccxt  # noqa: E402


async def main():
    exchange = ccxt.kraken({
        'enableRateLimit': True,  # required by the Manual
    })
    for i in range(0, 2):
        # this can be any call instead of fetch_ticker, really
        # 这里似乎有并发，没有需要task, 但是test_17.py里头没有并发，可能sleep函数有特殊性
        # await asyncio.sleep(2)
        # await asyncio.sleep(2)
        print(await exchange.fetch_ticker('ETH/USDT'))
    await exchange.close()


asyncio.get_event_loop().run_until_complete(main())
