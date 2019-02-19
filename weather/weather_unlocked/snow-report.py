import configparser
import requests
import sys
import math
 

def get_snow_report(resort_id, app_id, app_key):
    url = "https://api.weatherunlocked.com/api/snowreport/{}?app_id={}&app_key={}".format(resort_id, app_id, app_key)
    r = requests.get(url)
    return r.json(), r.status_code
 
def main():
    resort_id = 333003 
    app_id = 'e40e2a01'
    app_key = '1244b0ef81a7b9031d968f64ee0dd8d4'
    report, status = get_snow_report(resort_id, app_id, app_key)
    print('Status:', status)
    if status != 200:
        if 'title' in report:
            print(report['title'])
    else:
        print('Resort: {}'.format(report['resortname']))
        print('Total Snow: {} cm'.format(int(float(report['uppersnow_cm']))))
        print('New Snow: {} cm'.format(int(float(report['newsnow_cm']))))
        print('-----------------------------')
        print(report)


 
if __name__ == '__main__':
    main()  