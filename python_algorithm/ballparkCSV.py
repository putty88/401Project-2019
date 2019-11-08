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
        f = open('teamStats' + season + '.csv', "w")
        f.write(response.text)
        f.close()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    return (response.content)


# basicAPICall('2016', 'team_stats_totals')
# basicAPICall('2017', 'team_stats_totals')
# basicAPICall('2018', 'team_stats_totals')
# basicAPICall('2019', 'team_stats_totals')

        




def choose_team(A, season):
    df = pd.read_csv('teamStats' + season + '.csv', index_col='#Team ID')
    A_stats = df.loc[A].rename_axis('#Team ID').values
    print(type(A_stats))
    return A_stats

choose_team(125, '2018')


def normie(season):
    data = pd.read_csv('TeamStats' + season + '.csv')
    # print(data['#AtBats'].mean())
    print(data)

normie('2018')

    # Loop thru all the stats
    # Get the mean of each stat
    # Get the std deviation of each stat
    # Calculate : stats[i]-mean / std dev


# def choose_team_B(B, season):
#     df = pd.read_csv('teamStats' + season + '.csv', index_col='#Team ID')
#     B_stats = df.loc[B].rename_axis('#Team ID').values
#     # print(B_stats)
#     return B_stats


# def choose_teams(t1,t2):
#     df = pd.read_csv('teamStats.csv', index_col='#Team ID')
#     t1_stats = df.loc[t1].rename_axis('#Team ID').values
#     t2_stats = df.loc[t2].rename_axis('#Team ID').values
#     return t1_stats, t2_stats

# Example of how to ask for NumPy Arrays of two chosen teams
### print(choose_teams(111,133))
