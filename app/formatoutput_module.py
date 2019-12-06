import pandas as pd


class FormatOutput:

    def __init__(self):
        pd.set_option('display.max_columns', None)  
        pd.set_option('display.expand_frame_repr', False)
        pd.set_option('max_colwidth', -1)
        pd.set_option("display.colheader_justify","left")


    def print_report(self, df, rows):
        if df.empty:
            print("No data exists for the specified time period.\n")
        else:
            with pd.option_context('display.float_format', self._formatfunc):
                print(df[:rows].to_string(index=False))


    def _formatfunc(self, *args, **kwargs):
        value = args[0]
        if value >= 0:
            return '${:,.2f}'.format(value)
        else:
            return '-${:,.2f}'.format(abs(value))
