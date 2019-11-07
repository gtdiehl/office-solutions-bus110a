# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:30:32 2019

@author: Admin
"""


import pandas as pd
from datetime import date
import numpy as np
import Pandas_Format
SalesDataFull = pd.ExcelFile("SalesDataFull.xlsx")
OrdersOnlyData = SalesDataFull.parse("Orders")
ordersinfo = OrdersOnlyData[["Order Date", "Product Name", "Quantity", "Profit"]]


def profit_of_ten_products_ave(from_month, from_year, to_month, to_year, sort, type, num):
    df1 = ordersinfo[["Product Name", "Quantity", "Profit",
                      "Order Date"]].groupby("Product Name").sum()

    df1["Average Profit Per Unit"] = df1.loc[:, "Profit"].apply(np.float) / df1.loc[:, "Quantity"].apply(np.float)
    df1 = df1.sort_values(by="Average Profit Per Unit", ascending=sort)
    if sort and type == 'q':
        print("\n\n----[Least Profitable Product Report]----[Quarter: " + str(_change_month_to_quarter(num)) +
              " Year: " + str(from_year) + "]----")
    elif sort and type == 'm':
        print("\n\n----[Least Profitable Product Report]----[Month: " + str(num) + " Year: " +
              str(from_year) + "]----")
    elif sort is False and type == 'q':
        print("\n\n----[Most Profitable Product Report]----[Quarter: " + str(_change_month_to_quarter(num)) +
              " Year: " + str(from_year) + "]----")
    elif sort is False and type == 'm':
        print("\n\n----[Most Profitable Product Report]----[Month: " + str(num) + " Year: " +
              str(from_year) + "]----")
    Pandas_Format.print_report(df1, 10)


def _change_month_to_quarter(num):
    if 1 <= num <= 3:
        return 1
    elif 4 <= num <= 6:
        return 2
    elif 7 <= num <= 9:
        return 3
    elif 10 <= num <= 12:
        return 4

        
def _filter_df_by_date(df, date_column, from_month, from_year, to_month, to_year):
    if to_month == 12:
        to_month = 1
        to_year = to_year + 1
    else:
        to_month += 1

    filtered_data = df[
        (df[date_column] >= pd.Timestamp(date(from_year, from_month, 1))) &
        (df[date_column] < pd.Timestamp(date(to_year, to_month, 1)))
        ]
    return filtered_data





