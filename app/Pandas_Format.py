#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:55:16 2019

@author: joel
"""
#Fixes currency format into USD & two decimal places

import pandas as pd
pd.set_option('display.max_columns', None)  
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

#xl = pd.ExcelFile("SalesDataFull.xlsx")
#df = xl.parse("Orders")



def print_report(df, rows):
    with pd.option_context('display.float_format', _formatfunc):
        print(df.head(rows))

def _formatfunc(*args, **kwargs):
    value = args[0]
    if value >= 0:
        return '${:,.2f}'.format(value)
    else:
        return '-${:,.2f}'.format(abs(value))

