import sys
import requests
import json

args = [arg.upper() for arg in sys.argv[1:]]

for arg in args:
    # Basic API URL
    url = 'https://financialmodelingprep.com/public/api/company/profile/' + arg
    request = requests.get(url)

    print(arg)
    try:
        # First and last 5 characters are removed because JSON data is surrounded by HTML tags
        data = json.loads(request.text[5:-5])
        price = data[arg]["Price"]
        print('\tPrice: $' + str(price))
    except json.decoder.JSONDecodeError:
        print('\tError fetching data')

    print()
