import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

def _filter_df_by_date(df, date_column, from_month, from_year, to_month, to_year):
    filtered_data = df[
        (df[date_column] >= pd.Timestamp(date(from_year, from_month, 1))) &
        (df[date_column] < pd.Timestamp(date(to_year, to_month + 1, 1)))
        ]
    return filtered_data

def chart_example_one():
    xl = pd.ExcelFile("SalesDataFull.xlsx")
    df = xl.parse("Orders")
    df = _filter_df_by_date(df, "Order Date", 1, 2015, 1, 2015)
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
    plt.title('Discounts Given out by Region - Month: 1 Year:2015')
    # fix the legend
    current_handles, _ = plt.gca().get_legend_handles_labels()
    reversed_handles = reversed(current_handles)
    labels = sorted(df['Discount'].unique(), reverse=True)
    plt.legend(reversed_handles,labels,loc='lower right', title="Discount")
    plt.show()

def chart_example_two():
    xl = pd.ExcelFile("SalesDataFull.xlsx")
    df = xl.parse("Orders")
    df = _filter_df_by_date(df, "Order Date", 1, 2015, 1, 2015)
    df['Discount'] = pd.Series(["{0:.2f}%".format(val * 100) for val in df['Discount']], index=df.index)
    
    fig, ax = plt.subplots(figsize=(17, 6))
    df.groupby(['Category','Discount']).size().groupby(level=0).apply(
        lambda x: 100 * x / x.sum()
    ).unstack().plot(kind='bar', stacked=True, ax=ax)
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Percentage of Orders")
    # manipulate y-axis label
    vals = ax.get_yticks()
    ax.set_yticklabels(['{:.0f}%'.format(x) for x in vals])
    plt.title('Discounts by Product Category - Month: 1 Year:2015')
    # fix the legend
    current_handles, _ = plt.gca().get_legend_handles_labels()
    reversed_handles = reversed(current_handles)
    labels = sorted(df['Discount'].unique(), reverse=True)
    plt.legend(reversed_handles,labels,loc='lower right', title="Discount")
    plt.show()

def chart_example_three():
    xl = pd.ExcelFile("SalesDataFull.xlsx")
    df = xl.parse("Orders")
    df = _filter_df_by_date(df, "Order Date", 1, 2015, 1, 2015)
    
    fig, ax = plt.subplots(figsize=(17, 6))
    df = df[['Sales', 'Profit','Region']]
    df_groupby_sales = df.groupby(['Region']).sum()
    df_groupby_sales = df_groupby_sales.reset_index()
    df_groupby_sales.set_index('Region')[['Sales', 'Profit']].plot(kind='bar', ax=ax)
    plt.title('Sales and Profits by Region - Month: 1 Year:2015')
    ax.set_xlabel("Region")
    ax.set_ylabel("Dollar Amount")
    vals = ax.get_yticks()
    ax.set_yticklabels(['${:,.0f}'.format(x).replace('$-', '-$') for x in vals])
    plt.show()

def chart_example_four():
    sales = {}
    profits = {}
    
    xl = pd.ExcelFile("SalesDataFull.xlsx")
    df = xl.parse("Orders")
    
    a = 2.5
    for i in range(1, 12):
        s = _filter_df_by_date(df, "Order Date", i, 2015, i, 2015)
        sales[a] = s['Sales'].sum()
        profits[a] = s['Profit'].sum()
        a = a + 4
    sales_list = sorted(sales.items())
    profits_list = sorted(profits.items())
    
    x1, y1 = zip(*profits_list)
    x2, y2 = zip(*sales_list)
        
    df = _filter_df_by_date(df, "Order Date", 1, 2015, 1, 2016)
    df.set_index(df["Order Date"],inplace=True)
    
    df1 = df.groupby([pd.Grouper(freq='M'), 'Region'])['Profit'].sum()
    df2 = df.groupby([pd.Grouper(freq='M'), 'Region'])['Sales'].sum()
    result = pd.concat([df1, df2], axis=1, sort=False)
 
    # define the number of ticks
    
    fig, ax = plt.subplots(figsize=(17, 6))
    ax.set_title("Sales and Profits by Region per Month vs Company Total per Month")

    ax.set(ylabel='Dollar Amount')
    result.plot(kind='bar', ax=ax)
    ax.plot(x1, y1, '-o', color='#1f77b4')
    ax.plot(x2, y2, '-o', color='#ff7f0e')
    vals = ax.get_yticks()
    ax.set_yticklabels(['${:,.0f}'.format(x) for x in vals])         
    i = 0
    for x, y in sales.items():
        ax.text(x+0.2, y, '${:,.0f}'.format(y), horizontalalignment='left', size='medium', color='black', weight='bold')
        i = i + 1
    for x, y in profits.items():
        ax.text(x+0.2, y, '${:,.0f}'.format(y), horizontalalignment='left', size='medium', color='black', weight='bold')
        i = i + 1
    plt.show()

#chart_example_one()
#chart_example_two()
#chart_example_three()
chart_example_four()