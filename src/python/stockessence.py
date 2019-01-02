import sys
import requests
import json

args = [arg.upper() for arg in sys.argv[1:]]

for arg in args:
    # Basic API URl
    url = 'https://financialmodelingprep.com/public/api/company/profile/' + arg
    request = requests.get(url)
    # First and last 5 characters are removed because JSON data is surrounded by HTML tags
    data = json.loads(request.text[5:-5])

    price = data[arg]["Price"]

    print(arg)
    print("\tPrice: $" + str(price))
    print()
