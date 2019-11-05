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
ordersinfo = OrdersOnlyData[["Order Date","Product Name","Quantity","Profit",]]


def top_ten_profits(from_month, from_year, to_month, to_year):
    prodcol_and_profcol = OrdersOnlyData[["Order Date", "Product Name","Profit"]]

    fitered_df = _filter_df_by_date(prodcol_and_profcol, "Order Date", from_month, from_year, to_month, to_year)

    most_profit = fitered_df.sort_values(by= "Profit", ascending = False)
    Pandas_Format.print_report(most_profit, 10)


def top_ten_profit_ave(from_month, from_year, to_month, to_year):
    df1 = ordersinfo[["Product Name","Quantity","Profit", 
                "Order Date"]].groupby("Product Name").sum()

    df1["Average Profit Per Unit"] = df1.loc[:,"Profit"].apply(np.float) / df1.loc[:,"Quantity"].apply(np.float)                
    df1 = df1.sort_values(by="Average Profit Per Unit", ascending=False)
    Pandas_Format.print_report(df1, 10)
            
                
def least_ten_profits(from_month, from_year, to_month, to_year):
    prodcol_and_profcol = OrdersOnlyData[["Product Name","Profit"]]
    least_profit = prodcol_and_profcol.sort_values(by= "Profit")
    Pandas_Format.print_report(least_profit, 10)


def least_ten_profits_ave(from_month, from_year, to_month, to_year):
    df1 = ordersinfo[["Product Name","Quantity","Profit", 
                "Order Date"]].groupby("Product Name").sum()

    df1["Average Profit Per Unit"] = df1.loc[:,"Profit"].apply(np.float) / df1.loc[:,"Quantity"].apply(np.float)                
    df1 = df1.sort_values(by="Average Profit Per Unit", ascending=True)
    Pandas_Format.print_report(df1, 10)

        
def _filter_df_by_date(df, date_column, from_month, from_year, to_month, to_year):
    filtered_data = df[
        (df[date_column] >= pd.Timestamp(date(from_year, from_month, 1))) &
        (df[date_column] < pd.Timestamp(date(to_year, to_month + 1, 1)))
        ]
    return filtered_data





