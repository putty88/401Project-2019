import base64
import requests
import json
api_key = "e0c4e5ec-08d5-414d-88ce-9b392f"
pswrd = "MYSPORTSFEEDS"

# Basic API Call with inputs as season and keyword to use in all data collection
def basicAPICall(season, keyword):
    try:
        response = requests.get(
            url='https://api.mysportsfeeds.com/v2.1/pull/mlb/' + season + '-regular/' + keyword + '.json',
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format(api_key,pswrd).encode('utf-8')).decode('ascii')
            }
        )
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    return (json.loads(response.content))


# Collects all home games of a team given a season and returns it as an array containing JSON Scores.
def collectHomeGames(teamAbbreviation, season):
    home = []
    response = basicAPICall(season, 'games')
    for i in range(len(response['games'])):
        if(response['games'][i]['schedule']['homeTeam']['abbreviation'] == teamAbbreviation):
            home.append(response['games'][i]['schedule']['startTime'])
            home.append(response['games'][i]['score'])
    return home

def collectAllHomeGames(teamAbbreviation, season):
    home = []
    for i in range (2016, 2019):
        home.append(collectHomeGames(teamAbbreviation, str(i)))
    print(home)




def collectAwayGames(teamAbbreviation, season):
    away = []
    response = basicAPICall(season, 'games')
    for i in range(len(response['games'])):
        if(response['games'][i]['schedule']['awayTeam']['abbreviation'] == teamAbbreviation):
            away.append(response['games'][i]['schedule']['startTime'])
            away.append(response['games'][i]['score'])
    return away

def collectAllHomeGames(teamAbbreviation, season):
    away = []
    for i in range (2016, 2019):
        away.append(collectHomeGames(teamAbbreviation, str(i)))
    print(away)




collectAllHomeGames('OAK', '2016')

