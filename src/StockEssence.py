import ratio        # Stock ratio calculations (See this for more info https://www.investopedia.com/articles/stocks/06/ratios.asp)
import stockdata    # Retrieve stock information

import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

import threading

import json         # Parse json

import datetime     # Calculate current date
import configparser # Read/Write data file

import timeit       # Benchmarking

import os
dir = os.path.dirname(__file__)
data_ini = os.path.join(dir, 'data', 'data.ini') # Config file
read_file = 'my_companies.txt' # Name of company list to read from (Must be in src/data/)

def get_stock_symbols(file):
    '''Reads txt file and returns first
    grouped characters'''
    companies = []
    with open(file, "r") as fileObj:
        for line in fileObj:
            companies.append(line.split()[0])
    return companies[1:]

def process_config(file, companyList):
    '''Reads and writes data file'''
    now = datetime.datetime.now()
    parser = configparser.ConfigParser()
    parser.read(data_ini)

    if parser.get('TimeData', 'LastDay') == 'NULL' or int(parser.get('TimeData', 'LastDay')) != now.timetuple().tm_yday:
        parser.set('TimeData', 'LastDay', str(now.timetuple().tm_yday))
        with open(data_ini, 'w') as cfg:
            parser.write(cfg)
    
    # Processes number of days since last load
    if parser.get('TimeData', 'LastLoad') == 'NULL' or int(parser.get('TimeData', 'lastload')) >= 30:      
        write_json(os.path.join(dir, 'data', 'companydata.json'), companyList) #Load protocol
        parser.set('TimeData', 'LastLoad', '0')
        with open(data_ini, 'w') as cfg:
            parser.write(cfg)
    elif int(parser.get('TimeData', 'LastLoad')) <= 30 and int(parser.get('TimeData', 'LastDay')) != now.timetuple().tm_yday:
        parser.set('TimeData', 'LastLoad', str(int(parser.get('TimeData', 'LastLoad')) + 1))
        with open(data_ini, 'w') as cfg:
            parser.write(cfg)

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
        MainView.progress.text = str(index) + "/" + str(len(companiesList))
        MainView.company.text = str(company)
    with open(file, 'w') as outfile:
            json.dump(data, outfile, indent=4)
            print("wrote to json")
            

def main():
    start = timeit.default_timer()

    companies = get_stock_symbols(os.path.join(dir, 'data', read_file))
    process_config(data_ini, companies)
    
    stop = timeit.default_timer()
    print("run time:", stop-start, "seconds")

class MainView(BoxLayout):
    progress = Label()
    company = Label()
    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)

        self.add_widget(self.progress)
        self.add_widget(self.company)

class StockEssence(App):
    def build(self):
        return MainView()

def run_app():
    StockEssence().run()

if __name__ == "__main__":
    mainThread = threading.Thread(target=main)
    mainThread.start()
    run_app()