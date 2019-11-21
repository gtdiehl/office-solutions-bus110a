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

pd.set_option('mode.chained_assignment', None)

SalesDataFull = pd.ExcelFile("SalesDataFull.xlsx")
OrdersOnlyData = SalesDataFull.parse("Orders")
ordersinfo = OrdersOnlyData[["Order Date", "Product Name", "Quantity", "Profit"]]

def profit_of_ten_products_ave(from_month, from_year, to_month, to_year, sort, duration, num):
    fitered_ordersinfo = _filter_df_by_date(ordersinfo, "Order Date", from_month, from_year, to_month, to_year)
    if fitered_ordersinfo.empty:
        print("\nNo data exists for the specified time period.\n")
        return
    
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
    if filtered_customers.empty:
        print("\nNo data exists for the specified time period.\n")
        return
    
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
        title = (f"Least Profitable Customer Report - Quarter:"
                 f"{_change_month_to_quarter(num)} Year: {from_year}")
        
        print(f"\t\t\t\t--------[Least Profitable Customer Report]--------"
              "[Quarter: {_change_month_to_quarter(num)} Year: {from_year}]"
              "--------\n")
    elif sort and duration == 'm':
        title = (f"Least Profitable Customer Report - Month: {num} Year: "
                 f"{from_year}")
        
        print(f"\t\t\t\t--------[Least Profitable Customer Report]--------"
              "[Month: {num} Year: {from_year}]--------\n")
    elif sort is False and duration == 'q':
        title = (f"Most Profitable Customer Report - Quarter: "
                 f"{_change_month_to_quarter(num)} Year: {from_year}")
            
        print(f"\t\t\t\t--------[Most Profitable Customer Report]--------"
              f"[Quarter: {_change_month_to_quarter(num)} Year: {from_year}]"
              f"--------\n")
        
    elif sort is False and duration == 'm':
        title = (f"Most Profitable Customer Report - Month: {num} Year: "
                 f"{from_year}")
        print(f"\t\t\t\t--------[Least Profitable Customer Report]--------"
              f"[Month: {num} Year: {from_year}]--------\n")
        
    Pandas_Format.print_report(filtered_customers_sum, 10)
    print("=" * 117 + "\n")
    chart_df = filtered_customers_sum[:10]
    _generate_bar_chart_with_line_twinx(chart_df, title, 0, "Customer Name",
                                        "Customer Name", "Profit", 
                                        "Total Num of Orders", "Profit", 
                                        "Total Num of Orders")

def sales_and_profits_by_region_yearly(year):
    sales = {}
    profits = {}

    df = OrdersOnlyData  
    a = 1.5
    for i in range(1, 13):
        s = _filter_df_by_date(df, "Order Date", i, year, i, year)
        sales[a] = s['Sales'].sum()
        profits[a] = s['Profit'].sum()
        a = a + 4
    if s.empty:
        print("\nNo data exists for the specified time period.\n")
        return
    sales_list = sorted(sales.items())
    profits_list = sorted(profits.items())
    
    x1, y1 = zip(*profits_list)
    x2, y2 = zip(*sales_list)
        
    df = _filter_df_by_date(df, "Order Date", 1, year, 12, year)
    df.set_index(df["Order Date"],inplace=True)
    
    df1 = df.groupby([pd.Grouper(freq='M'), 'Region'])['Profit'].sum()
    df2 = df.groupby([pd.Grouper(freq='M'), 'Region'])['Sales'].sum()
    result = pd.concat([df1, df2], axis=1, sort=False)
 
    # define the number of ticks
    
    fig, ax = plt.subplots(figsize=(17, 6))
    ax2 = ax.twinx()
    ax.set_title(f"Sales and Profits by Region per Month vs Company Total per "
                 f"Month for the Year {year}")

    ax.set(ylabel='Dollar Amount')
    result.plot(kind='bar', ax=ax)
    ax2.plot(x1, y1, '-o', color='#1f77b4')
    ax2.plot(x2, y2, '-o', color='#ff7f0e')
    vals = ax.get_yticks()
    ax.set_yticklabels(['${:,.0f}'.format(x) for x in vals])
    vals = ax2.get_yticks()
    ax2.set_yticklabels(['${:,.0f}'.format(x) for x in vals]) 
    i = 0
    for x, y in sales.items():
        ax2.text(x+0.2, y, '${:,.0f}'.format(y), horizontalalignment='left',
                 size='medium', color='black', weight='bold')
        i = i + 1
    for x, y in profits.items():
        ax2.text(x+0.2, y, '${:,.0f}'.format(y), horizontalalignment='left',
                 size='medium', color='black', weight='bold')
        i = i + 1
    ax.legend(loc='upper left')
    plt.show()

def sales_and_profits_by_region(from_month, from_year, to_month, to_year,
                                duration, num):

    df = OrdersOnlyData
    df = _filter_df_by_date(df, "Order Date", from_month, from_year, to_month,
                            to_year)
    if df.empty:
        print("\nNo data exists for the specified time period.\n")
        return
    
    fig, ax = plt.subplots(figsize=(17, 6))
    df = df[['Sales', 'Profit','Region']]
    df_groupby_sales = df.groupby(['Region']).sum()
    df_groupby_sales = df_groupby_sales.reset_index()
    df_groupby_sales.set_index('Region')[['Sales', 'Profit']].plot(kind='bar',
                                                                   ax=ax)
    if duration == 'm' or duration == 'M':
        plt.title(f"Sales and Profits by Region - Month: {from_month} Year: "
                  f"{from_year}")
    else:
        plt.title(f"Sales and Profits by Region - Quarter: {_change_month_to_quarter(num)} Year: "
                  f"{from_year}")
        
    ax.set_xlabel("Region")
    ax.set_ylabel("Dollar Amount")
    vals = ax.get_yticks()
    ax.set_yticklabels(['${:,.0f}'.format(x).replace('$-', '-$') for x in vals])
    plt.show()

def discounts_by_region(from_month, from_year, to_month, to_year, duration, num):
    df = OrdersOnlyData
    df = _filter_df_by_date(df, "Order Date", from_month, from_year, to_month,
                            to_year)
    if df.empty:
        print("\nNo data exists for the specified time period.\n")
        return
    
    df['Discount'] = pd.Series(["{0:.2f}%".format(val * 100) for val in df['Discount']], index=df.index)
    
    fig, ax = plt.subplots(figsize=(17, 6))
    df.groupby(['Region','Discount']).size().groupby(level=0).apply(
        lambda x: 100 * x / x.sum()
    ).unstack().plot(kind='bar', stacked=True, ax=ax)
    ax.set_xlabel("Region")
    ax.set_ylabel("Percentage of Orders")
    # manipulate y-axis label
    vals = ax.get_yticks()
    ax.set_yticklabels(['{:.0f}%'.format(x) for x in vals])
    if duration == 'm' or duration == 'M':
        plt.title(f"Discounts Given out by Region - Month: {from_month} Year: "
                  f"{from_year}")
    else:
        plt.title(f"Discounts Given out by Region - Quarter: {_change_month_to_quarter(num)} Year: "
                  f"{from_year}")
    # fix the legend
    current_handles, _ = plt.gca().get_legend_handles_labels()
    reversed_handles = reversed(current_handles)
    labels = sorted(df['Discount'].unique(), reverse=True)
    plt.legend(reversed_handles,labels,loc='lower right', title="Discount")
    plt.show()

def discounts_by_category_and_region(from_month, from_year, to_month, to_year,
                                     duration, num):
    df = OrdersOnlyData
    df = _filter_df_by_date(df, "Order Date", from_month, from_year, to_month,
                            to_year)
    if df.empty:
        print("\nNo data exists for the specified time period.\n")
        return
    
    region_central_df = df[(df['Region'] == 'Central')]
    region_east_df = df[(df['Region'] == 'East')]
    region_south_df = df[(df['Region'] == 'South')]
    region_west_df = df[(df['Region'] == 'West')]
    
    filtered_region_central_df1 = region_central_df[['Order Date', 'Category', 'Discount']]
    filtered_region_east_df1 = region_east_df[['Order Date', 'Category', 'Discount']]
    filtered_region_south_df1 = region_south_df[['Order Date', 'Category', 'Discount']]
    filtered_region_west_df1 = region_west_df[['Order Date', 'Category', 'Discount']]
    
    filtered_region_central_df2 = region_central_df[['Order Date', 'Category', 'Sub-Category', 'Discount']]
    filtered_region_east_df2 = region_east_df[['Order Date', 'Category', 'Sub-Category', 'Discount']]
    filtered_region_south_df2 = region_south_df[['Order Date', 'Category', 'Sub-Category', 'Discount']]
    filtered_region_west_df2 = region_west_df[['Order Date', 'Category', 'Sub-Category', 'Discount']]
    
    fig, axs = plt.subplots(2, 4, figsize=(19,10))
    
    filtered_region_central_df1.groupby(['Category', 'Discount']).size().groupby(level=0).apply(
        lambda x: 100 * x / x.sum()
    ).unstack().plot(kind='bar', stacked=True, ax=axs[0,0])
    axs[0,0].set_title('Central Region')
    axs[0,0].set_ylabel('Percentage of Orders')
    
    filtered_region_east_df1.groupby(['Category', 'Discount']).size().groupby(level=0).apply(
        lambda x: 100 * x / x.sum()
    ).unstack().plot(kind='bar', stacked=True, ax=axs[0,1])
    axs[0,1].set_title('East Region')
    
    filtered_region_south_df1.groupby(['Category', 'Discount']).size().groupby(level=0).apply(
        lambda x: 100 * x / x.sum()
    ).unstack().plot(kind='bar', stacked=True, ax=axs[0,2])
    axs[0,2].set_title('South Region')
    
    filtered_region_west_df1.groupby(['Category', 'Discount']).size().groupby(level=0).apply(
        lambda x: 100 * x / x.sum()
    ).unstack().plot(kind='bar', stacked=True, ax=axs[0,3])
    axs[0,3].set_title('West Region')
    
    filtered_region_central_df2.groupby(['Sub-Category', 'Discount']).size().groupby(level=0).apply(
        lambda x: 100 * x / x.sum()
    ).unstack().plot(kind='bar', stacked=True, ax=axs[1,0])
    axs[1,0].set_title('Central Region')
    axs[1,0].set_ylabel('Percentage of Orders')
    
    filtered_region_east_df2.groupby(['Sub-Category', 'Discount']).size().groupby(level=0).apply(
        lambda x: 100 * x / x.sum()
    ).unstack().plot(kind='bar', stacked=True, ax=axs[1,1])
    axs[1,1].set_title('East Region')
    
    filtered_region_south_df2.groupby(['Sub-Category', 'Discount']).size().groupby(level=0).apply(
        lambda x: 100 * x / x.sum()
    ).unstack().plot(kind='bar', stacked=True, ax=axs[1,2])
    axs[1,2].set_title('South Region')
    
    filtered_region_west_df2.groupby(['Sub-Category', 'Discount']).size().groupby(level=0).apply(
        lambda x: 100 * x / x.sum()
    ).unstack().plot(kind='bar', stacked=True, ax=axs[1,3])
    axs[1,3].set_title('West Region')
    
    for x in range(0, 2):
        for y in range (0, 4):
            vals = axs[x, y].get_yticks()
            axs[x, y].set_yticklabels(['{:.0f}%'.format(z) for z in vals])
            current_handles, labels = axs[x, y].get_legend_handles_labels()
            reversed_handles = reversed(current_handles)
            for a in range(0, len(labels)):
                labels[a] = '{:.0f}%'.format(float(labels[a]) * 100)
            labels = reversed(labels)
            axs[x, y].legend(reversed_handles, labels, loc='lower right',
                             title="Discount")
    
    if duration == 'm' or duration == 'M':
        plt.suptitle(f"Discounts by Product Category and Sub-Category by "
                     f"Region - Month: {from_month} Year: {from_year}")
    else:
        plt.suptitle(f"Discounts by Product Category and Sub-Category by "
                     f"Region - Quarter: {_change_month_to_quarter(num)} Year: {from_year}")
    plt.subplots_adjust(wspace=0.2, hspace=0.6)
    plt.show()
    
def topcust_no_disc(from_month, from_year, to_month, to_year, duration, num):

    df = df = OrdersOnlyData
    df = _filter_df_by_date(df, "Order Date", from_month, from_year, to_month,
                            to_year)
    if df.empty:
        print("\nNo data exists for the specified time period.\n")
    return
    
    df2 = df[df.Discount == 0]
    df3 = df2.sort_values(by='Profit', ascending= False)
    df3 = df3[["Customer Name", "Profit"]]
    df3 = df3.groupby(["Customer Name"]).sum()
    df3 = df3.sort_values(by="Profit", ascending=False)

    fig, ax1 = plt.subplots(figsize=(17,5))
    
    df3 = df3[:10]
    
    if duration == 'm' or duration == 'M':
        print("="*117 + "\n")
        title = (f"Top 10 Customers Profits Without Discounts - Month: {from_month}"
                 f" Year: {from_year}")
        print(f"\t\t--------[Top 10 Customers Profits Without Discounts]"
              f"--------[Month: {from_month} Year: {from_year}]--------\n")
        Pandas_Format.print_report(df3.reset_index(), 10)
        print("="*117 + "\n")
        df3.plot(kind='bar', ax=ax1)
        ax1.set(title=title, ylabel="Profit")
    else:
        print("="*117 + "\n")
        title = (f"Top 10 Customers Profits Without Discounts - Quarter: {_change_month_to_quarter(num)}"
                 f" Year: {from_year}")        
        print(f"\t\t--------[Top 10 Customers Profits Without Discounts]"
              f"--------[Quarter: {_change_month_to_quarter(num)} Year: {from_year}]--------\n")
        Pandas_Format.print_report(df3.reset_index(), 10)
        print("="*117 + "\n")
        df3.plot(kind='bar', ax=ax1)
        ax1.set(title=title, ylabel="Profit")
    vals = ax1.get_yticks()
    ax1.set_yticklabels(['${:.0f}'.format(x) for x in vals])
    plt.show()

def topcust_high_disc(from_month, from_year, to_month, to_year, duration, num):
    df = df = OrdersOnlyData
    df = _filter_df_by_date(df, "Order Date", from_month, from_year, to_month,
                            to_year)

    if df.empty:
        print("\nNo data exists for the specified time period.\n")
    return

    fig, ax1 = plt.subplots(figsize=(17,5))

    df2 = df[df.Discount > 0]
    df3 = df2.sort_values(by='Profit', ascending=True)
    df3 = df3[["Customer Name", "Profit", "Discount"]]
    df3 = df3.groupby(['Customer Name', 'Discount']).sum().sort_values(by='Profit', ascending=True)
    df3 = df3[:10]
    text_df3 = df3.reset_index()
    text_df3['Discount'] = text_df3['Discount'].map('{:.0%}'.format)
    if duration == 'm' or duration == 'M':
        #print("="*117 + "\n")
        title = (f"Bottom 10 Customer Profits With Discounts - Month: {from_month}"
                 f" Year: {from_year}")
        #print(f"\t\t--------[Bottom 10 Customer Profits With Discounts]"
        #      f"--------[Month: {from_month} Year: {from_year}]--------\n")
        #Pandas_Format.print_report(text_df3, 10)
        #print("="*117 + "\n")
    else:
        #print("="*117 + "\n")
        title = (f"Bottom 10 Customer Profits With Discounts - Quarter: {_change_month_to_quarter(num)}"
                 f" Year: {from_year}")        
        #print(f"\t\t--------[Bottom 10 Customer Profits With Discounts]"
        #      f"--------[Quarter: {_change_month_to_quarter(num)} Year: {from_year}]--------\n")
        #Pandas_Format.print_report(text_df3, 10)
        #print("="*117 + "\n")
    df3 = df3.reset_index().pivot('Customer Name', 'Discount', 'Profit')
    df3.plot(kind='bar', stacked=True, ax=ax1)
    ax1.set_title(title)
    vals = ax1.get_yticks()
    ax1.set_yticklabels(['${:,.0f}'.format(x) for x in vals])
    current_handles, _ = plt.gca().get_legend_handles_labels()
    reversed_handles = reversed(current_handles)
    labels = sorted(df['Discount'].unique(), reverse=True)
    for a in range(0, len(labels)):
        labels[a] = '{:.0f}%'.format(float(labels[a]) * 100)
    plt.legend(reversed_handles,labels,loc='lower right', title="Discount")
    ax1.set_yticklabels(['${:,.0f}'.format(x).replace('$-', '-$') for x in vals])
    plt.show()

def _generate_bar_chart(df, title, xaxis_rotation, xaxis_df_name, xaxis_label,
                        yaxis_df_name, yaxis_label):

    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.set_title(title)

    sns.barplot(ax=ax, x=xaxis_df_name, y=yaxis_df_name, data=df)

    ax.set_xticklabels(labels=df[xaxis_df_name], rotation=xaxis_rotation)
    ax.set(xlabel=xaxis_label, ylabel=yaxis_label)
    vals = ax.get_yticks()
    ax.set_yticklabels(['${:,.0f}'.format(x).replace('$-', '-$') for x in vals])
    
    plt.show()

def _generate_bar_chart_with_line_twinx(df, title, xaxis_rotation,
                                        xaxis_df_name, xaxis_label,
                                        yaxis1_df_name, yaxis2_df_name,
                                        yaxis1_label, yaxis2_label):
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(19, 6))
    
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
    
    ax2.set_yticks(np.linspace(ax2.get_yticks()[0], ax2.get_yticks()[-1],
                               len(ax.get_yticks())))
    ax2.yaxis.set_major_locator(plt.LinearLocator(numticks=NUM_TICKS))
    
    i = 0
    for line in df.index.values.tolist():
        ax2.text(i+0.1, df[yaxis2_df_name][line], df[yaxis2_df_name][line],
                 horizontalalignment='left', size='medium', color='black',
                 weight='bold')
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

        
def _filter_df_by_date(df, date_column, from_month, from_year, to_month,
                       to_year):
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
