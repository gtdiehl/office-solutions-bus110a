#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:55:16 2019

@author: joel
"""
#Fixes currency format into USD & two decimal places

import pandas as pd

xl = pd.ExcelFile("SalesDataFull.xlsx")
df = xl.parse("Orders")

def formatfunc(*args, **kwargs):
    value = args[0]
    if value >= 0:
        return '${:,.2f}'.format(value)
    else:
        return '-${:,.2f}'.format(abs(value))

with pd.option_context('display.float_format', formatfunc):
    print(df)

