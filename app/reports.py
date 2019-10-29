# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:30:32 2019

@author: Admin
"""


import pandas as pd
#import scipy.stats
#import seaborn as sns
#import matplotlib.pyplot as plt
SalesDataFull = pd.ExcelFile("SalesDataFull.xlsx")
OrdersOnlyData = SalesDataFull.parse("Orders")
lines = "="*25

def top_ten_profits():
            prodcol_and_profcol = OrdersOnlyData[["Product Name","Profit"]]
            most_profit = prodcol_and_profcol.sort_values(by= "Profit", ascending = False)
            print(most_profit.head(10))
            
                
def least_ten_profits():
            prodcol_and_profcol = OrdersOnlyData[["Product Name","Profit"]]
            least_profit = prodcol_and_profcol.sort_values(by= "Profit")
            print(least_profit.head(10))          
        
                  
top_ten_profits()          
least_ten_profits()





