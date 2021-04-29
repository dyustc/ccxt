# -*- coding: utf-8 -*-

import os
import sys
from pprint import pprint

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt  # noqa: E402


print('CCXT Version:', ccxt.__version__)

for exchange_id in ccxt.exchanges:
    try:
        # Note: where is the ccxt.py？ ccxt.exchanges in the __init__.py
        exchange = getattr(ccxt, exchange_id)()
        print(exchange_id)
        # do what you want with this exchange
        if exchange_id == 'kraken':
            pprint(dir(exchange))
            pprint(getattr(exchange, 'id'))
    except Exception as e:
        print(e)