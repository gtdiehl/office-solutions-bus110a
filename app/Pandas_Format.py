#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:55:16 2019

@author: joel
"""
#Fixes currency format into USD & two decimal places

import pandas as pd
#from tabulate import tabulate
pd.set_option('display.max_columns', None)  
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)
pd.set_option("display.colheader_justify","left")


def print_report(df, rows):
    if df.empty:
        print("No data exists for the specified time period.\n")
    else:
        with pd.option_context('display.float_format', _formatfunc):
            print(df[:rows].to_string(index=False))
            #print(tabulate(df.iloc[:10], headers='keys', tablefmt='psql', showindex='False'))


def _formatfunc(*args, **kwargs):
    value = args[0]
    if value >= 0:
        return '${:,.2f}'.format(value)
    else:
        return '-${:,.2f}'.format(abs(value))

