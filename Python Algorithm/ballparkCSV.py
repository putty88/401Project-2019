import base64
import requests
import json
import csv
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


#def collectHomeGames(season, teamAbbreviation):
#    with open(basicAPICall(season, 'games')) as csvfile:
#    # readCSV = csv.reader(csvfile, delimiter=','
    

# def getSeasonalTeamStats(season, )




 basicAPICall(2018, keyword):