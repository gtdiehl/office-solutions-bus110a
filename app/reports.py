# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:30:32 2019

@author: Admin
"""


import pandas as pd
from datetime import date
import Pandas_Format

#import scipy.stats
#import seaborn as sns
#import matplotlib.pyplot as plt
SalesDataFull = pd.ExcelFile("SalesDataFull.xlsx")
OrdersOnlyData = SalesDataFull.parse("Orders")
lines = "="*25

def top_ten_profits(from_month, from_year, to_month, to_year):
            prodcol_and_profcol = OrdersOnlyData[["Order Date", "Product Name","Profit"]]
            
            fitered_df = _filter_df_by_date(prodcol_and_profcol, "Order Date", from_month, from_year, to_month, to_year)
            
            most_profit = fitered_df.sort_values(by= "Profit", ascending = False)
            #print(most_profit.head(10))
            Pandas_Format.print_report(most_profit, 10)
            
                
def least_ten_profits():
            prodcol_and_profcol = OrdersOnlyData[["Product Name","Profit"]]
            least_profit = prodcol_and_profcol.sort_values(by= "Profit")
            print(least_profit.head(10))          
        
        
def _filter_df_by_date(df, date_column, from_month, from_year, to_month, to_year):
    filtered_data = df[
        (df[date_column] >= pd.Timestamp(date(from_year, from_month, 1))) &
        (df[date_column] < pd.Timestamp(date(to_year, to_month + 1, 1)))
        ]
    return filtered_data

print()
                  
#top_ten_profits()          
#least_ten_profits()





