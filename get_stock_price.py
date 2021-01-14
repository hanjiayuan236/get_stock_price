#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:15:40 2021

@author: jiayuanhan
"""

import pandas as pd
import pandas_datareader.data as web   
import datetime

def get_stock_price_today(stock_label):
    date = datetime.date.today()

    try:
        prices = web.DataReader(stock_label, "yahoo", date, date)
        return prices[['High', 'Low', 'Open', 'Close']]
    except:
        print('No data fetched for symbol {} from Yahoo.com. Please try other symbols.\n'
              .format(stock_label))
        return pd.DataFrame(columns = ['High', 'Low', 'Open', 'Close'])