import requests
from pprint import pprint

coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(coindesk_url)

data = response.json()
#pprint(data)

dollars_exchange_rate = data['bpi']['USD']['rate_float']
print(dollars_exchange_rate)

bitcoin = float(input('Enter number of bitcoins: '))

bitcoin_value_in_USD = bitcoin * dollars_exchange_rate

print(f'{bitcoin} bitcoin is worth ${bitcoin_value_in_USD}')