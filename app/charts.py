import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

from matplotlib.pyplot import title


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
    xl = pd.ExcelFile("SalesDataFull.xlsx")
    df = xl.parse("Orders")
    df = _filter_df_by_date(df, "Order Date", 1, 2015, 1, 2016)
    df.set_index(df["Order Date"],inplace=True)
    
    df1 = df.groupby([pd.Grouper(freq='M'), 'Region'])['Profit'].sum()
    df2 = df.groupby([pd.Grouper(freq='M'), 'Region'])['Sales'].sum()
    result = pd.concat([df1, df2], axis=1, sort=False)
    
    fig, ax = plt.subplots(figsize=(17, 6))
    result.plot(kind='bar', ax=ax)
    plt.show()

chart_example_one()
chart_example_two()
chart_example_three()
chart_example_four()