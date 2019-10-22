import pandas
from tabulate import tabulate


class Report:
    def __init__(self):
        self.xl = pandas.ExcelFile("SalesDataFull.xlsx")

    def report_profitable_products(self, order):
        profitable_product = []
        orders_only_data = self.xl.parse("Orders")
        sorted_orders_by_profit = orders_only_data.sort_values(by="Profit", ascending=order)
        sorted_orders_by_profit['Profit Per Qty'] = sorted_orders_by_profit['Profit'] / sorted_orders_by_profit['Quantity']
        product_names = sorted_orders_by_profit['Product Name'].unique()
        product_names = sorted(product_names)
        for product in product_names:
            product_select = sorted_orders_by_profit.loc[sorted_orders_by_profit["Product Name"] == product]
            my_sum = product_select["Profit Per Qty"].sum()
            my_len = product_select["Profit Per Qty"].count()
            avg_profit = my_sum / my_len
            # print("Sum: " + str(my_sum) + " Count: " + str(my_len))
            min_profit = round(product_select["Profit Per Qty"].min(), 2)
            max_profit = round(product_select["Profit Per Qty"].max(), 2)
            '''
            if min_profit == max_profit:
                print("Product: " + product + " Profit: ${:.2f}".format(min_profit))
            else:
                print("Product: " + product + " Profit Min: ${:.2f}".format(min_profit) + " Max: ${:.2f}".format(max_profit))
            '''
            profitable_product.append([product, avg_profit, min_profit, max_profit])
        df = pandas.DataFrame(profitable_product, columns=['Product Name', 'Average Profit', 'Min Profit', 'Max Profit'])
        sorted_df = df.sort_values(by='Average Profit', ascending=False)
        print(sorted_df.head(10))
        # for index, row in sorted_orders_by_profit.iterrows():
        #    print(row['Quantity'], row['Profit'], row['Profit Per Qty'])

    def report_profitable_product_per_sub_category(self, order):
        # Show Most Profitable Product order=False
        # Show Least Profitable Product order=True

        orders_only_data = self.xl.parse("Orders")

        categories = orders_only_data.Category.unique()
        for category in categories:
            cat_select = orders_only_data.loc[orders_only_data["Category"] == category]
            cat_sub_prof = cat_select[["Category", "Sub-Category", "Profit"]]
            best_sub = cat_sub_prof.groupby("Sub-Category").sum().sort_values(by="Profit", ascending=order)
            if order is True:
                print("\nLeast Profitable Sub-Category in the {} Category".format(category))
            else:
                print("\nMost Profitable Sub-Category in the {} Category".format(category))
            best_sub['Profit'] = best_sub['Profit'].map('${:,.2f}'.format)
            pdtabulate=lambda df: tabulate(df,headers='keys', tablefmt='psql')
            print(pdtabulate(best_sub.iloc[:1]))


if __name__ == "__main__":
    # Report().report_profitable_products(False)
    Report().report_profitable_product_per_sub_category(True)
    Report().report_profitable_product_per_sub_category(False)