import base64
import json
import requests
import csv
import pandas as pd
api_key = "e0c4e5ec-08d5-414d-88ce-9b392f"
pswrd = "MYSPORTSFEEDS"


def basicAPICall(season, keyword):
    suffix = ''
    if('gamelogs' in keyword):
        suffix = '?team=det'
    try:
        response = requests.get(
            url='https://api.mysportsfeeds.com/v2.1/pull/mlb/' + season + '-regular/' + keyword + '.csv' + suffix,
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format(api_key,pswrd).encode('utf-8')).decode('ascii')
            }
        )
        f = open('teamStats.csv', "w")
        f.write(response.text)
        f.close()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    return (response.content)

keyword = 'team_stats_totals'
basicAPICall('2018', keyword)

def choose_teams(t1,t2):
    df = pd.read_csv('teamStats.csv', index_col='#Team ID')
    t1_stats = df.loc[t1].rename_axis('#Team ID').values
    t2_stats = df.loc[t2].rename_axis('#Team ID').values
    return t1_stats, t2_stats

# Example of how to ask for NumPy Arrays of two chosen teams
### print(choose_teams(111,133))
