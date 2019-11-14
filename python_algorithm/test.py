import base64
import json
import requests
import csv
import pandas as pd
import numpy as np
api_key = "e0c4e5ec-08d5-414d-88ce-9b392f"
pswrd = "MYSPORTSFEEDS"


def basicAPICall(season, keyword, format):
    suffix = ''
    if('gamelogs' in keyword):
        suffix = '?team=det'
    try:
        response = requests.get(
            url='https://api.mysportsfeeds.com/v2.1/pull/mlb/' + season + '-regular/' + keyword + '.' + format + suffix,
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format(api_key,pswrd).encode('utf-8')).decode('ascii')
            }
        )
        # f = open(keyword + season + '.csv', "w", encoding='utf-8')
        # f.write(response.text)
        # f.close()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    if(format == 'json'):
        return (json.loads(response.content))
    else:
        return (response.content)



print(basicAPICall('2019', 'ga', 'json'))