import requests
import json

def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

def remove_suffix(text, suffix):
    return text[:-len(suffix)]

def get_net_income(symbol):
    '''Returns net income of stock based on
    symbol in the past twelve months'''
    url = 'https://financialmodelingprep.com/api/financials/income-statement/' + str(symbol)
    r = requests.get(url)
    c = remove_suffix(remove_prefix(r.text, '<pre>'), '<pre>')
    d = json.loads(c)
    return(d[str(symbol)]['Net income']['TTM'])

def get_revenue(symbol):
    url = 'https://financialmodelingprep.com/api/financials/income-statement/' + str(symbol)
    r = requests.get(url)
    c = remove_suffix(remove_prefix(r.text, '<pre>'), '<pre>')
    d = json.loads(c)
    return(d[str(symbol)]['Revenue']['TTM'])

def get_gross_profit(symbol):
    url = 'https://financialmodelingprep.com/api/financials/income-statement/' + str(symbol)
    r = requests.get(url)
    c = remove_suffix(remove_prefix(r.text, '<pre>'), '<pre>')
    d = json.loads(c)
    return(d[str(symbol)]['Gross profit']['TTM'])

def get_stock_price(symbol):
    url = 'https://financialmodelingprep.com/api/company/price/' + str(symbol)
    r = requests.get(url)
    c = remove_suffix(remove_prefix(r.text, '<pre>'), '<pre>')
    d = json.loads(c)
    return(d[str(symbol)]['price'])
