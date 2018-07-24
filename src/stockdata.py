import requests
import json

def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

def remove_suffix(text, suffix):
    return text[:-len(suffix)]

class company_info(object):
    def __init__(self, symbol):
        self.symbol = str(symbol)
        url = 'https://financialmodelingprep.com/api/financials/income-statement/' + str(symbol)
        r = requests.get(url)
        c = remove_suffix(remove_prefix(r.text, '<pre>'), '<pre>')
        self.d = json.loads(c)

    def get_net_income(self):
        '''Returns net income of stock in
        the past twelve months'''
        return(str(int(self.d[str(self.symbol)]['Net income']['TTM']) * 1000000))

    def get_revenue(self):
        '''Returns revenue of stock in
        the past twelve months'''
        return(str(int(self.d[str(self.symbol)]['Revenue']['TTM']) * 1000000))

    def get_gross_profit(self):
        '''Returns gross profit of stock in
        the past twelve months'''
        return(str(int(self.d[str(self.symbol)]['Gross profit']['TTM']) * 1000000))

class share_info(object):
    def __init__(self, symbol):
        self.symbol = str(symbol)
        url = 'https://financialmodelingprep.com/public/api/company/profile/' + str(symbol)
        r = requests.get(url)
        c = remove_suffix(remove_prefix(r.text, '<pre>'), '<pre>')
        self.d = json.loads(c)

    def get_share_price(self):
        '''Returns current stock price'''
        return(self.d[str(self.symbol)]['Price'])

    def get_number_of_outstanding_shares(self):
        '''Returns current number stock's of outstanding shares'''
        return(str(int(self.d[str(self.symbol)]['MktCap']) / int(self.d[str(self.symbol)]['Price'])))