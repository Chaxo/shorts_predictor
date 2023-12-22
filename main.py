import requests
import streamlit as st
from PIL import Image
from pathlib import Path

def retrieve_weather_from_weatherapi(location, api_key):
    url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        'key' : api_key,
        'q' : location,
        'days' : 1,
        'aqi' : 'no',
        'alerts': 'no'
    }
    headers = {
        'Content-Type': 'application/json'
    }
    r = requests.get(url=url, params=params, headers=headers)
    weather_info = r.json()
    return weather_info

def wear_shorts(avgtemp_c, daily_chance_of_rain):
    if avgtemp_c >= 21 and daily_chance_of_rain < 50:
        return True
    if avgtemp_c >= 25:
        return True

if __name__ == '__main__':
    location = st.text_input('Enter your location')
    api_key = "53e70973ea12442ea8f205919231912"
    current_directory = Path.cwd()
    images_folder = current_directory / 'images'
    shorts_image = images_folder / 'shorts_01.jpg'
    pants_image = images_folder / 'pants_01.jpg'
    if location:
        weather_info = retrieve_weather_from_weatherapi(location, api_key)
        date = weather_info['forecast']['forecastday'][0]['date']
        place = weather_info['location']['name']
        region = weather_info['location']['region']
        country = weather_info['location']['country']
        avgtemp_c = weather_info['forecast']['forecastday'][0]['day']['avgtemp_c']
        daily_chance_of_rain = weather_info['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
        if wear_shorts(avgtemp_c, daily_chance_of_rain) == True:
            chosen_image = Image.open(shorts_image)
        else:
            chosen_image = Image.open(pants_image)
        st.image(chosen_image)
        st.json({
            'Date' : date,
            'Place': place,
            'region' : region,
            'Country': country,
            'Average Temperature': avgtemp_c,
            'Chance of Rain': daily_chance_of_rain
        })
        