import pandas
from datetime import date
from tabulate import tabulate


def _filter_df_by_date(df, date_column, from_month, from_year, to_month, to_year):
    filtered_data = df[
        (df[date_column] >= pandas.Timestamp(date(from_year, from_month, 1))) &
        (df[date_column] < pandas.Timestamp(date(to_year, to_month + 1, 1)))
        ]
    return filtered_data


class Report:
    def __init__(self):
        self.xl = pandas.ExcelFile("SalesDataFull.xlsx")

    def report_profitable_products(self, order, from_month, from_year, to_month, to_year):
        # Show Most Profitable Product order=False
        # Show Least Profitable Product order=True

        profitable_product = []
        orders_only_data = self.xl.parse("Orders")
        orders_only_data['Order Date'] = pandas.to_datetime(orders_only_data['Order Date'])
        filtered_order_data = _filter_df_by_date(orders_only_data, 'Order Date', from_month, from_year, to_month,
                                                 to_year)
        sorted_orders_by_profit = filtered_order_data.sort_values(by="Profit", ascending=order)
        sorted_orders_by_profit['Profit Per Qty'] = sorted_orders_by_profit['Profit'] / \
            sorted_orders_by_profit['Quantity']
        product_names = sorted_orders_by_profit['Product Name'].unique()
        product_names = sorted(product_names)
        for product in product_names:
            product_select = sorted_orders_by_profit.loc[sorted_orders_by_profit["Product Name"] == product]
            my_sum = product_select["Profit Per Qty"].sum()
            my_len = product_select["Profit Per Qty"].count()
            avg_profit = my_sum / my_len
            min_profit = round(product_select["Profit Per Qty"].min(), 2)
            max_profit = round(product_select["Profit Per Qty"].max(), 2)
            profitable_product.append([product, avg_profit, min_profit, max_profit])
        df = pandas.DataFrame(profitable_product, columns=['Product Name', 'Average Profit', 'Min Profit',
                                                           'Max Profit'])
        sorted_df = df.sort_values(by='Average Profit', ascending=order)
        sorted_df['Average Profit'] = sorted_df['Average Profit'].map('${:,.2f}'.format)
        sorted_df['Min Profit'] = sorted_df['Min Profit'].map('${:,.2f}'.format)
        sorted_df['Max Profit'] = sorted_df['Max Profit'].map('${:,.2f}'.format)
        pdtabulate=lambda af: tabulate(af, headers='keys', tablefmt='psql')
        if not order:
            print("Top 10 Most Profitable Products for Time Period: %d/%d to %d/%d" % (from_month, from_year, to_month,
                                                                                       to_year))
        else:
            print("Bottom 10 Least Profitable Products for Time Period: %d/%d to %d/%d" % (from_month, from_year,
                                                                                           to_month, to_year))
        print(pdtabulate(sorted_df.iloc[:10]))

    def report_profitable_product_per_sub_category(self, order, from_month, from_year, to_month, to_year):
        # Show Most Profitable Product order=False
        # Show Least Profitable Product order=True

        orders_only_data = self.xl.parse("Orders")
        filtered_order_data = _filter_df_by_date(orders_only_data, 'Order Date', from_month, from_year, to_month,
                                                 to_year)

        categories = filtered_order_data.Category.unique()
        for category in categories:
            cat_select = filtered_order_data.loc[filtered_order_data["Category"] == category]
            cat_sub_prof = cat_select[["Category", "Sub-Category", "Profit"]]
            best_sub = cat_sub_prof.groupby("Sub-Category").sum().sort_values(by="Profit", ascending=order)
            if order is True:
                print("\nLeast Profitable Sub-Category in the %s Category for the Period from %d/%d to %d/%d" %
                      (category, from_month, from_year, to_month, to_year))
            else:
                print("\nMost Profitable Sub-Category in the %s Category for the Period from %d/%d to %d/%d" %
                      (category, from_month, from_year, to_month, to_year))
            best_sub['Profit'] = best_sub['Profit'].map('${:,.2f}'.format)
            pdtabulate=lambda df: tabulate(df,headers='keys', tablefmt='psql')
            print(pdtabulate(best_sub.iloc[:1]))


if __name__ == "__main__":
    Report().report_profitable_products(True, 1, 2015, 4, 2016)
    Report().report_profitable_products(False, 1, 2015, 4, 2016)
    Report().report_profitable_product_per_sub_category(True, 1, 2015, 4, 2016)
    Report().report_profitable_product_per_sub_category(False, 1, 2015, 4, 2016)