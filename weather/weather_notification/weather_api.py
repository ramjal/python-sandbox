import configparser
import requests
import sys
import math
 
def test():
    print('Success!')


def get_api_info():
    try:
        config = configparser.ConfigParser()
        config.read(r'C:\DevLcl\Sandbox\python_sandbox\weather\weather_notification\config.ini')
        return config['openweathermap']['api'], config['openweathermap']['location']
    except Exception as e:
        print(e)
 

def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()
 