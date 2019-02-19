import sys
import math
import weather_api
# Add the needed path for send_gmail file
sys.path.append(r"C:\DevLcl\Sandbox\python_sandbox\email")
import send_gmail


def main():
#     print(sys.path)
#     send_gmail.test()
#     weather_api.test()    
    api_key, location = weather_api.get_api_info()
    weather = weather_api.get_weather(api_key, location)

    if weather['cod'] == 200:
        temp = math.ceil(weather['main']['temp'])
        tempMin = math.ceil(weather['main']['temp_min'])
        tempMax = math.ceil(weather['main']['temp_max'])
        msg = []
        subject = '{} weather forcast'.format(weather['name'])
        msg.append('Current temprature: {}°'.format(temp))
        msg.append('Min: {}°'.format(tempMin))
        msg.append('Max: {}°'.format(tempMax))
        l = [w['description'] for w in weather['weather']]
        msg.append('Condition: {}'.format(l))
        message = '\n'.join(msg)
        print(message)

    from_ = 'ramjal@gmail.com'
    to = 'rjalali@westlandinsurance.ca'

    service = send_gmail.service_factory()
    wather_message = send_gmail.create_message(from_, to, subject, message)
    send_gmail.send_message(service, 'me', wather_message)


if __name__ == '__main__':
    main()