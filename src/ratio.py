def profit_margin(netIncome, revenue):
    return(netIncome / revenue) #revenue = net sales

def earnings_per_share(profit, numOutstandingShares):
    return(profit / numOutstandingShares) #Profit from fiscal year

def earnings_per_share_growth(finalEarningsPerShare, initialEarningsPerShare):
    return((finalEarningsPerShare - initialEarningsPerShare) / initialEarningsPerShare)

def price_to_earnings(stockPrice, earningsPerShare):
    return(stockPrice / earningsPerShare)

def price_to_earnings_growth(priceToEarnings, earningsPerShareGrowth):
    return(priceToEarnings / earningsPerShareGrowth) #Lower is better

def decimal_to_percentage(decVal):
    decStr = str(decVal * 100)
    finalStr = ""
    if(decVal >= 0.1):
        finalStr = decStr[:4] + "%"
    elif(decVal < 0.1):
        finalStr = decStr[:3] + "%"
    return finalStr
