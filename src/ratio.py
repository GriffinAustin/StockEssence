def margin(difference, final):
    return(difference / final)

def earnings_per_share(profit, numOutstandingShares):
    return(profit / numOutstandingShares) #Profit from fiscal year

def earnings_per_share_growth(finalEarningsPerShare, initialEarningsPerShare):
    return((finalEarningsPerShare - initialEarningsPerShare) / initialEarningsPerShare)

def price_to_earnings(stockPrice, earningsPerShare):
    return(stockPrice / earningsPerShare)

def price_to_earnings_growth(priceToEarnings, earningsPerShareGrowth):
    return(priceToEarnings / earningsPerShareGrowth) #Lower is better

def decimal_to_percentage(decVal):
    perCent = round(decVal * 100,ndigits=2)
    return "{}%".format(perCent)
