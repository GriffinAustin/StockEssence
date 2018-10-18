import ratio        # Stock ratio calculations (See this for more info https://www.investopedia.com/articles/stocks/06/ratios.asp)
import stockdata    # Retrieve stock information

import threading

import json         # Parse json

import datetime     # Calculate current date

import timeit       # Benchmarking

import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.core.text import LabelBase
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.write()

# Register fonts
LabelBase.register(name='OpenSans', fn_regular="OpenSans-Regular.ttf")

class StockEssence(Widget):
    def init(self):
        mainThread = threading.Thread(target=StockEssenceApp().main, args=(self,))
        mainThread.start()

class StockEssenceApp(App):
    def build(self):
        return StockEssence()

    def main(self, btn):
        start = timeit.default_timer()
        btn.disabled = True
        companies = get_stock_symbols('companylist.txt')
        write_json('companydata.json', companies)  # Load protocol
        btn.disabled = False

        stop = timeit.default_timer()
        print("run time:", stop - start, "seconds")


def get_stock_symbols(file):
    '''Reads txt file and returns first
    grouped characters'''
    companies = []
    with open(file, "r") as fileObj:
        for line in fileObj:
            companies.append(line.split()[0])
    return companies[1:]

def write_json(file, companiesList):
    '''Logs company data to file for increased speed in future loads'''
    data = {}
    data['Companies'] = []    
    for company in companiesList:
        try:
            companyStatement = stockdata.company_info(company)
            stock = stockdata.share_info(company)
            data['Companies'].append({
                'Updated': str(datetime.date.today()),
                'Symbol': company,
                'Net Income': companyStatement.get_net_income(),
                'Revenue': companyStatement.get_revenue(),
                'Gross Profit': companyStatement.get_gross_profit(),
                'Stock Price': str(stock.get_share_price()),
                'Number of Outstanding Shares': str(int(round(float(stock.get_number_of_outstanding_shares())))),
                'Net Profit Margin': str(ratio.margin(int(companyStatement.get_net_income()), int(companyStatement.get_revenue()))),
                'Gross Profit Margin': str(ratio.margin(int(companyStatement.get_gross_profit()), int(companyStatement.get_revenue()))),
                'Earnings Per Share': str(ratio.earnings_per_share(int(companyStatement.get_gross_profit()), float(stock.get_number_of_outstanding_shares()))),
                'Price to Earnings': str(ratio.price_to_earnings(float(stock.get_share_price()), ratio.earnings_per_share(int(companyStatement.get_gross_profit()), float(stock.get_number_of_outstanding_shares()))))
            })
            print(company, 'done')
        except:
            print(company, 'failed')
        index = int(companiesList.index(company))+1
        print(index, "/", len(companiesList))
    with open(file, 'w') as outfile:
            json.dump(data, outfile, indent=4)
            print("wrote to json")

def init():
    StockEssenceApp().run()


if __name__ == "__main__":
    guiThread = threading.Thread(target=init)
    guiThread.start()
