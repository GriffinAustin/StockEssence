import ratio        # Stock ratio calculations (See this for more info https://www.investopedia.com/articles/stocks/06/ratios.asp)
import stockdata    #Retrieve stock information

import json         #Parse json

import datetime     #Calculate current date
import configparser #Read/Write data file

import timeit       #Benchmarking

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
    parser.read('data\data.ini')

    if parser.get('TimeData', 'LastDay') == 'NULL' or int(parser.get('TimeData', 'LastDay')) != now.timetuple().tm_yday:
        parser.set('TimeData', 'LastDay', str(now.timetuple().tm_yday))
        with open('data\data.ini', 'w') as cfg:
            parser.write(cfg)
    
    # Processes number of days since last load
    if parser.get('TimeData', 'LastLoad') == 'NULL' or int(parser.get('TimeData', 'lastload')) > 30:      
        write_json('data\companydata.json', companyList) #Load protocol
        parser.set('TimeData', 'LastLoad', '0')
        with open('data\data.ini', 'w') as cfg:
            parser.write(cfg)
    elif int(parser.get('TimeData', 'LastLoad')) <= 30 and int(parser.get('TimeData', 'LastDay')) != now.timetuple().tm_yday:
        parser.set('TimeData', 'LastLoad', str(int(parser.get('TimeData', 'LastLoad')) + 1))
        with open('data\data.ini', 'w') as cfg:
            parser.write(cfg)

def write_json(file, companiesList):
    '''Logs company data to file for increased speed in future loads'''
    data = {}
    data['Companies'] = []
    for company in companiesList:
        try:
            data['Companies'].append({
                'Symbol': str(company),
                'Net Income': str(stockdata.get_net_income(company)),
                'Revenue': str(stockdata.get_revenue(company)),
                'Gross Profit': str(stockdata.get_gross_profit(company)),
                'Stock Price': str(stockdata.get_stock_price(company)),
                'Number of Outstanding Shares': str(stockdata.get_outstanding_shares(company))
            })
            print(company, 'done')
        except:
            print(company, 'failed')
    with open(file, 'w') as outfile:
            json.dump(data, outfile, indent=4)
            print("wrote to json")
            

def main():
    start = timeit.default_timer()

    companies = get_stock_symbols("data\snp500.txt")
    process_config('data\data.ini', companies)
    
    stop = timeit.default_timer()
    print("run time:", stop-start, "seconds")

if __name__ == "__main__":
    main()
