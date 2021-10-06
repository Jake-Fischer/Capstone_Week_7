import os
import requests
from pprint import pprint
from datetime import datetime

key = os.environ.get('WEATHER_KEY')

query_params = {'q': 'minneapolis,us', 'units':'imperial', 'appid':key}

url = 'http://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query_params).json()

list_of_forecasts = data['list']

for forecast in list_of_forecasts:
    temp = forecast['main']['temp']
    timestamp = forecast['dt']
    forecast_date = datetime.fromtimestamp(timestamp)
    print(f'At {forecast_date} the temp should be {temp}F')

