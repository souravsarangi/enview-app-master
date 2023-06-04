from json import JSONDecodeError
from flask import Flask

import requests
import requests_cache

FLUSH_PERIOD = 10 * 60  # 10 minutes in seconds
requests_cache.install_cache(expire_after=FLUSH_PERIOD)


def get_ip(app: Flask):
    base_url_ip = 'https://api.ipify.org'
    # app.logger.info('%s', requests.get(base_url_ip).text)
    return requests.get(base_url_ip).text


def get_geo(app: Flask, ip):
    response_geo = requests.get(f'http://ip-api.com/json/{ip}', headers={'User-Agent': 'sourav_weather_app'}).json()
    geo_info = ('lat', 'lon', 'city', 'country')
    # app.logger.info('%s', response_geo)
    return {info: response_geo[info] for info in geo_info}


def get_weather(app: Flask, lat, lon):
    base_url_weather = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'
    response_weather = requests.get(base_url_weather, params={'lat': str(lat), 'lon': str(lon)})
    # app.logger.info('%s', response_weather)
    try:
        response_weather = response_weather.json()
        return response_weather['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']
    except JSONDecodeError as e:
        return 42.0


def convert_to_fr(temp_C):
    return 9 / 5 * temp_C + 32


def greet(app: Flask, ip):
    geo_info = get_geo(app, ip)
    temp = get_weather(app, geo_info['lat'], geo_info['lon'])
    return f'It is {temp} degree celsius right now at your location: {geo_info["city"]}, {geo_info["country"]}'
