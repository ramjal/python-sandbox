import configparser
import requests
import sys
import math
 
def get_api_info():
    try:
        config = configparser.ConfigParser()
        config.read('OpenWeatherMap\\config.ini')
        return config['openweathermap']['api'], config['openweathermap']['location']
    except Exception as e:
        print(e)
 
def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()
 
def main():
    api_key, location = get_api_info()
    weather = get_weather(api_key, location)
    
    if weather['cod'] == 200:
        temp = math.ceil(weather['main']['temp'])
        tempMin = math.ceil(weather['main']['temp_min'])
        tempMax = math.ceil(weather['main']['temp_max'])
        print('{}:'.format(location))
        print('Current temprature: {}°'.format(temp))
        print('temprature min: {}°'.format(tempMin))
        print('temprature max: {}°'.format(tempMax))
        l = [w['description'] for w in weather['weather']]
        print('condition: {}'.format(l))

    print('-----------------------------')
    print(weather)



 
if __name__ == '__main__':
    main()