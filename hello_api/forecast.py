import requests
import os
import logging


key = os.environ.get('WEATHER_KEY')

url = f'http://api.openweathermap.org/data/2.5/forecast'


def main():
    location = get_location()
    weather_data, error = get_current_weather(location,key)
    if error:
        print('Sorry, could not get the weather.')
        logging.error('An error has occired getting the weather data.')
    else:
        five_day_weather_forecast = get_data(weather_data)
        for forecast in five_day_weather_forecast:
            temp = forecast['temp']
            timestamp = forecast['timestamp'] # Keeping timestamp in UTC time. Reason being this program does not yet have the functionality to determine what timezone a certain country is in
            description = forecast['description']
            wind_speed = forecast['windspeed']

            print(f'At {timestamp} UTC the temperature will be {temp}F, the weather will be {description}, the wind will be {wind_speed}MPH')


def get_location():
    city, country = '',''
    while len(city) == 0:
        city = input('Enter the name of the city: ').strip()

    while len(country) != 2 or not country.isalpha:
        country = input('Enter the 2-letter country code: ').strip()

    location = f'{city},{country}'
    return location


def get_current_weather(location, key):
    try:
        query_params = {'q': location, 'units':'imperial', 'appid':key}
        response = requests.get(url, params=query_params)
        response.raise_for_status() # Raises an exception for 400 or 500 errors
        data = response.json()
        return data, None
    except Exception as e:
        logging.error(e)
        logging.info(response.text)
        return None, e


def get_data(weather_data):
    try:
        data_list_raw = weather_data['list']
        five_day_forecast = []
        for forecast in data_list_raw:
            day_forecast = {}
            day_forecast['temp'] = forecast['main']['temp']
            day_forecast['timestamp'] = forecast['dt']
            day_forecast['description'] = forecast['weather'][0]['description']
            day_forecast['windspeed'] = forecast['wind']['speed']
            five_day_forecast.append(day_forecast)
        return five_day_forecast
    except KeyError:
        print('This data is not in the format expected')
        return 'Unknown'


if __name__ == '__main__':
    main()
