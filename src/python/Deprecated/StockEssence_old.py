__license__ = "MIT"
__version__ = "1.0.0-beta1"
__maintainer__ = "Griffin Austin"
__email__ = "gaustin25@gmail.com"
__status__ = "Beta"

# Stock ratio calculations (See this for more info
# https://www.investopedia.com/articles/stocks/06/ratios.asp)
import ratio
import stockdata  # Retrieve stock information

import threading

import json  # Parse json

import datetime  # Calculate current date

import timeit  # Benchmarking

import kivy
from kivy.config import Config
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.properties import StringProperty

kivy.require('1.10.1')

# Prevents right-clicking from creating red dots (part of baseline Kivy)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
# Prevents pressing escape from closing the app
Config.set('kivy', 'exit_on_escape', '0')

# Register fonts
LabelBase.register(name='OpenSans', fn_regular="OpenSans-Regular.ttf")


class Line(Widget):
    pass


class StockEssence(FloatLayout):
    def init(self):
        main_thread = threading.Thread(target=StockEssenceApp().main, args=(self,))
        main_thread.start()


class StockEssenceApp(App):
    def build(self):
        root = FloatLayout(size=(800, 6001))
        root.add_widget(StockEssence())
        root.add_widget(Line())
        return root

    @staticmethod
    def main(btn):
        start = timeit.default_timer()
        btn.disabled = True
        companies = get_stock_symbols('companylist.txt')
        write_json('companydata.json', companies)  # Load protocol
        btn.disabled = False

        stop = timeit.default_timer()
        print("run time:", stop - start, "seconds")


def get_stock_symbols(filename):
    """Reads txt file and returns first
    grouped characters"""
    companies = []
    with open(filename, "r") as fileObj:
        for line in fileObj:
            companies.append(line.split()[0])
    return companies[1:]


def write_json(filename, companies_list):
    """Logs company data to file for increased speed in future loads"""
    data = {'Companies': []}
    for company in companies_list:
        try:
            company_statement = stockdata.company_info(company)
            stock = stockdata.share_info(company)
            data['Companies'].append({
                'Updated': str(datetime.date.today()),
                'Symbol': company,
                'Net Income': company_statement.get_net_income(),
                'Revenue': company_statement.get_revenue(),
                'Gross Profit': company_statement.get_gross_profit(),
                'Stock Price': str(stock.get_share_price()),
                'Number of Outstanding Shares': str(
                    int(
                        round(
                            float(
                                stock.get_number_of_outstanding_shares())))),
                'Net Profit Margin': str(
                    ratio.margin(
                        int(
                            company_statement.get_net_income()),
                        int(
                            company_statement.get_revenue()))),
                'Gross Profit Margin': str(
                    ratio.margin(
                        int(
                            company_statement.get_gross_profit()),
                        int(
                            company_statement.get_revenue()))),
                'Earnings Per Share': str(
                    ratio.earnings_per_share(
                        int(
                            company_statement.get_gross_profit()),
                        float(
                            stock.get_number_of_outstanding_shares()))),
                'Price to Earnings': str(
                    ratio.price_to_earnings(
                        float(
                            stock.get_share_price()),
                        ratio.earnings_per_share(
                            int(
                                company_statement.get_gross_profit()),
                            float(
                                stock.get_number_of_outstanding_shares()))))
            })
            print(company, 'done')
        except KeyError:
            print(company, 'failed')
        index = int(companies_list.index(company)) + 1
        print(index, "/", len(companies_list))
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)
        print("wrote to json")


def init():
    StockEssenceApp().run()


if __name__ == "__main__":
    guiThread = threading.Thread(target=init)
    guiThread.start()
