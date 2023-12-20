import requests
import json

if __name__ == '__main__':
    api_key = "53e70973ea12442ea8f205919231912"
    location = "est netherlands"
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
    response = r.json()
    place = response['location']['name']
    region = response['location']['region']
    country = response['location']['country']
    # print(response['forecast']['forecastday'][0]['day'])
    print(response)