import configparser
import requests
import sys
 
def get_api_key():
    try:
        config = configparser.ConfigParser()
        config.read('OpenWeatherMap\\config.ini')
        return config['openweathermap']['api']
    except Exception as e:
        print(e)
 
def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()
 
def main():
    location = 'London,uk'
    # if len(sys.argv) != 2:
    #     exit("Usage: {} LOCATION".format(sys.argv[0]))
    # location = sys.argv[1]
 
    api_key = get_api_key()
    weather = get_weather(api_key, location)
 
    print(weather['main']['temp'])
    print(weather)
 
 
if __name__ == '__main__':
    main()