#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:43:21 2021

@author: jiayuanhan
"""

from get_stock_price import get_stock_price_today

#stock symbols for testing
stock_symbols = ['ISRG', 'AAPL', 'AAAA', 'CHAU']
for stock_symbol in stock_symbols:
    prices = get_stock_price_today(stock_symbol)
    if len(prices):
        print('price information for {}:'.format(stock_symbol))
        print('High:  {:.2f}'.format(prices['High'][0]))
        print('Low:   {:.2f}'.format(prices['Low'][0]))
        print('Open:  {:.2f}'.format(prices['Open'][0]))
        print('Close: {:.2f}'.format(prices['Close'][0]))
        print('--------------------------\n')
    else:
        print('--------------------------\n')