#import the request module 
import requests
import json
import argparse

api_key='1c06a8585e4b5ab12a2573f85a9b92ce'


def get_weather(city):
    base_url="https://api.openweathermap.org/data/2.5/weather" 
    params = {
        'q' : city,
        'appid': api_key,
        'units':'metric'
    }
    try:
        response = requests.get(base_url,params)
        response.raise_for_status()
        data = response.json()
        weather_data={
            'city' : data.get('name'),
            'temperature' : data['main'].get('temp'),
            'weather' :data['weather'][0].get('description') if data.get('weather') else None
        }

        print(f'City : {weather_data["city"]}')
        print(f'Temperature :{weather_data["temperature"]}°C')
        print(f'Humidity :{weather_data["humidity"]}')
        print(f'Description :{weather_data['description']}')
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Error : Unauthorized. Check your API Key")
        elif response.status_code == 404:
            print("Error : City not found")
        else: 
            print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f'An error occurred: {err}')

parser = argparse.ArgumentParser(description="Weather Checking App")
parser.add_argument("--city",help="provide the city name e.g. London, New York")

args = parser.parse_args()

get_weather(args.city)
