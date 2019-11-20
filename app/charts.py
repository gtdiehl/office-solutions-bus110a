import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

def topcust_no_disc():
    xl = pd.ExcelFile("SalesDataFull.xlsx")
    df = xl.parse("Orders")
    df = _filter_df_by_date(df, "Order Date", 1, 2015, 1, 2015)
    
    df2 = df[df.Discount == 0]
    df3 = df2.sort_values(by='Profit', ascending= False)
    df3 = df3.head(15)
    print(df3)
    #Defining 2 plot axis and size of graph
    fig = plt.figure(figsize=(20,5))
    #1x2 Grid
    ax1 = fig.add_subplot(1,2,1)
    
    df3 = df3.rename(columns={"Customer Name":"Customer_Name"})
    
    ax1.bar(df3['Customer_Name'], df3['Profit'])
    ax1.set_xticklabels(df3['Customer_Name'], rotation=60, horizontalalignment='right')
    ax1.set_title("Top 10 Customers Profits Without Discounts")
    ax1.set_ylabel("Profit")
 
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
    ax2 = ax.twinx()
    ax.set_title("Sales and Profits by Region per Month vs Company Total per Month")

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
        ax2.text(x+0.2, y, '${:,.0f}'.format(y), horizontalalignment='left', size='medium', color='black', weight='bold')
        i = i + 1
    for x, y in profits.items():
        ax2.text(x+0.2, y, '${:,.0f}'.format(y), horizontalalignment='left', size='medium', color='black', weight='bold')
        i = i + 1
    plt.show()
    
def chart_example_five():
    xl = pd.ExcelFile("SalesDataFull.xlsx")
    df = xl.parse("Orders")
    df = _filter_df_by_date(df, "Order Date", 1, 2015, 1, 2015)
    
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
            axs[x, y].legend(reversed_handles, labels, loc='lower right', title="Discount")
    

    plt.suptitle('Discounts by Product Category and Sub-Category by Region - Month: 1 Year: 2015')
    plt.subplots_adjust(wspace=0.2, hspace=0.6)
    plt.show()

#chart_example_one()
#chart_example_two()
#chart_example_three()
#chart_example_four()
#chart_example_five()
#    
#chart_example_four()
#chart_example_three()
#chart_example_one()
#chart_example_five()
topcust_no_disc()