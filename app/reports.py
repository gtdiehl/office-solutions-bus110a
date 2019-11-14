# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:30:32 2019

@author: Admin
"""


import pandas as pd
from datetime import date
import numpy as np
import Pandas_Format
import matplotlib.pyplot as plt
import seaborn as sns

SalesDataFull = pd.ExcelFile("SalesDataFull.xlsx")
OrdersOnlyData = SalesDataFull.parse("Orders")
ordersinfo = OrdersOnlyData[["Order Date", "Product Name", "Quantity", "Profit"]]

def profit_of_ten_products_ave(from_month, from_year, to_month, to_year, sort, duration, num):
    fitered_ordersinfo = _filter_df_by_date(ordersinfo, "Order Date", from_month, from_year, to_month, to_year)
    fitered_ordersinfo_sum = fitered_ordersinfo[["Product Name", "Profit", "Quantity", "Order Date"]]\
        .groupby(["Product Name"]).sum()
    fitered_ordersinfo_sum = fitered_ordersinfo_sum.reset_index()

    fitered_ordersinfo_sum["Average Profit/Unit"] = fitered_ordersinfo_sum.loc[:, "Profit"].apply(np.float) / \
        fitered_ordersinfo_sum.loc[:, "Quantity"].apply(np.float)
    fitered_ordersinfo_sum = fitered_ordersinfo_sum.sort_values(by="Average Profit/Unit", ascending=sort)
    print("\n\n" + "="*117)
    if sort and duration == 'q':
        title = "Least Profitable Product Report - Quarter: " + str(_change_month_to_quarter(num)) + " Year: " + str(from_year)
        print("\t\t\t\t--------[Least Profitable Product Report]--------[Quarter: " +
              str(_change_month_to_quarter(num)) + " Year: " + str(from_year) + "]--------\n")
    elif sort and duration == 'm':
        title = "Least Profitable Product Report - Month: " + str(num) + " Year: " + str(from_year)
        print("\t\t\t\t--------[Least Profitable Product Report]--------[Month: " +
              str(num) + " Year: " + str(from_year) + "]--------\n")
    elif sort is False and duration == 'q':
        title = "Most Profitable Product Report - Quarter: " + str(_change_month_to_quarter(num)) + " Year: " + str(from_year)
        print("\t\t\t\t--------[Most Profitable Product Report]--------[Quarter: " +
              str(_change_month_to_quarter(num)) + " Year: " + str(from_year) + "]--------\n")
    elif sort is False and duration == 'm':
        title = "Most Profitable Product Report - Month: " + str(num) + " Year: " + str(from_year)
        print("\t\t\t\t--------[Most Profitable Product Report]--------[Month: " +
              str(num) + " Year: " + str(from_year) + "]--------\n")
    Pandas_Format.print_report(fitered_ordersinfo_sum, 10)
    print("="*117 + "\n")
    chart_df = fitered_ordersinfo_sum[:10]
    _generate_bar_chart(chart_df, title, 90, "Product Name", "Product Name", "Average Profit/Unit",
                        "Average Profit/Unit")


def active_customer_report(from_month, from_year, to_month, to_year, sort, duration, num):
    customers = OrdersOnlyData[["Order Date", "Customer Name", "Profit"]]
    filtered_customers = _filter_df_by_date(customers, "Order Date", from_month, from_year, to_month, to_year)

    unique_customer_list = filtered_customers["Customer Name"].unique()
    num_of_orders_dic = {}
    for cust in unique_customer_list:
        customer_select = filtered_customers.loc[filtered_customers["Customer Name"] == cust]
        my_len = customer_select["Customer Name"].count()
        num_of_orders_dic[cust] = my_len

    filtered_customers_sum = filtered_customers.groupby(["Customer Name"]).sum()
    filtered_customers_sum = filtered_customers_sum.reset_index()
    filtered_customers_sum['Total Num of Orders'] = filtered_customers_sum['Customer Name'].map(num_of_orders_dic)
    filtered_customers_sum = filtered_customers_sum.sort_values(by="Profit", ascending=sort)
    print("\n\n" + "="*117)
    if sort and duration == 'q':
        title = "Least Profitable Customer Report - Quarter: " + str(_change_month_to_quarter(num)) + " Year: " + str(from_year)
        print("\t\t\t\t--------[Least Profitable Customer Report]--------[Quarter: " +
              str(_change_month_to_quarter(num)) + " Year: " + str(from_year) + "]--------\n")
    elif sort and duration == 'm':
        title = "Least Profitable Customer Report - Month: " + str(num) + " Year: " + str(from_year)
        print("\t\t\t\t--------[Least Profitable Customer Report]--------[Month: " +
              str(num) + " Year: " + str(from_year) + "]--------\n")
    elif sort is False and duration == 'q':
        title = "Most Profitable Customer Report - Quarter: " + str(_change_month_to_quarter(num)) + " Year: " + str(from_year)
        print("\t\t\t\t--------[Most Profitable Customer Report]--------[Quarter: " +
              str(_change_month_to_quarter(num)) + " Year: " + str(from_year) + "]--------\n")
    elif sort is False and duration == 'm':
        title = "Most Profitable Customer Report - Month: " + str(num) + " Year: " + str(from_year)
        print("\t\t\t\t--------[Least Profitable Customer Report]--------[Month: " +
              str(num) + " Year: " + str(from_year) + "]--------\n")
    Pandas_Format.print_report(filtered_customers_sum, 10)
    print("=" * 117 + "\n")
    chart_df = filtered_customers_sum[:10]
    _generate_bar_chart_with_line_twinx(chart_df, title, 0, "Customer Name", "Customer Name", "Profit",
                                        "Total Num of Orders", "Profit", "Total Num of Orders")


def _generate_bar_chart(df, title, xaxis_rotation, xaxis_df_name, xaxis_label, yaxis_df_name, yaxis_label):

    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.set_title(title)

    sns.barplot(ax=ax, x=xaxis_df_name, y=yaxis_df_name, data=df)

    ax.set_xticklabels(labels=df[xaxis_df_name], rotation=xaxis_rotation)
    ax.set(xlabel=xaxis_label, ylabel=yaxis_label)
    vals = ax.get_yticks()
    ax.set_yticklabels(['${:,.0f}'.format(x).replace('$-', '-$') for x in vals])
    
    plt.show()

def _generate_bar_chart_with_line_twinx(df, title, xaxis_rotation, xaxis_df_name, xaxis_label, yaxis1_df_name,
                                        yaxis2_df_name, yaxis1_label, yaxis2_label):
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(15, 6))
    
    # define the number of ticks
    NUM_TICKS=11
    
    ax.yaxis.set_major_locator(plt.LinearLocator(numticks=NUM_TICKS))
    
    ax.set_title(title)
    ax2 = ax.twinx()

    sns.barplot(ax=ax, x=xaxis_df_name, y=yaxis1_df_name, data=df)
    sns.scatterplot(ax=ax2, x=xaxis_df_name, y=yaxis2_df_name, data=df)

    ax.set_xticklabels(labels=df[xaxis_df_name], rotation=xaxis_rotation)
    ax.set(xlabel=xaxis_label, ylabel=yaxis1_label)
    vals = ax.get_yticks()
    ax.set_yticklabels(['${:,.0f}'.format(x).replace('$-', '-$') for x in vals])
    
    ax2.set(ylabel=yaxis2_label)
    
    ax2.set_yticks(np.linspace(ax2.get_yticks()[0], ax2.get_yticks()[-1], len(ax.get_yticks())))
    ax2.yaxis.set_major_locator(plt.LinearLocator(numticks=NUM_TICKS))
    
    i = 0
    for line in df.index.values.tolist():
        ax2.text(i+0.1, df[yaxis2_df_name][line], df[yaxis2_df_name][line], horizontalalignment='left', size='medium', color='black', weight='bold')
        i = i +1
    plt.show()

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
