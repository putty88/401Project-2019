import base64
import requests
import json
api_key = "e0c4e5ec-08d5-414d-88ce-9b392f"
pswrd = "MYSPORTSFEEDS"

# Basic API Call with inputs as season and keyword to use in all data collection
def basicAPICall(season, keyword):
    suffix = ''
    if('gamelogs' in keyword):
        suffix = '?team=det'
    try:
        response = requests.get(
            url='https://api.mysportsfeeds.com/v2.1/pull/mlb/' + season + '-regular/' + keyword + '.json' + suffix,
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
    homeScores = []
    response = basicAPICall(season, 'games')
    for i in range(len(response['games'])):
        if(response['games'][i]['schedule']['homeTeam']['abbreviation'] == teamAbbreviation):
            homeScores.append(response['games'][i]['schedule']['startTime'])
            homeScores.append(response['games'][i]['score'])
    return homeScores

def collectAllHomeGames(teamAbbreviation):
    homeScores = []
    for i in range (2016, 2019):
        homeScores.append(collectHomeGames(teamAbbreviation, str(i)))
    return homeScores


def collectAwayGames(teamAbbreviation, season):
    awayScores = []
    response = basicAPICall(season, 'games')
    for i in range(len(response['games'])):
        if(response['games'][i]['schedule']['awayTeam']['abbreviation'] == teamAbbreviation):
            awayScores.append(response['games'][i]['schedule']['startTime'])
            awayScores.append(response['games'][i]['score'])
    return awayScores

def collectAllAwayGames(teamAbbreviation):
    awayScores = []
    for i in range (2016, 2019):
        awayScores.append(collectAwayGames(teamAbbreviation, str(i)))
    return awayScores


def collectPlayerGamelogs(teamAbbreviation, season):
    playerGamelogs = []
    response = basicAPICall(season, 'player_gamelogs')
    for i in range(len(response['gamelogs'])):
        if(response['gamelogs'][i]['team']['abbreviation'] == teamAbbreviation):
            playerGamelogs.append(response['gamelogs'][i])
    return playerGamelogs

def collectAllPlayerGamelogs(teamAbbreviation):
    playerGamelogs = []
    for i in range (2016, 2019):
        playerGamelogs.append(collectPlayerGamelogs(teamAbbreviation, str(i)))
    return playerGamelogs


def collectTeamGamelogs(teamAbbreviation, season):
    teamGamelogs = []
    response = basicAPICall(season, 'team_gamelogs')
    for i in range(len(response['gamelogs'])):
        if(response['gamelogs'][i]['team']['abbreviation'] == teamAbbreviation):
            teamGamelogs.append(response['gamelogs'][i])
    return teamGamelogs

def collectAllTeamGamelogs(teamAbbreviation):
    teamGamelogs = []
    for i in range (2016, 2019):
        teamGamelogs.append(collectTeamGamelogs(teamAbbreviation, str(i)))
    return teamGamelogs





# Problem! Boxscore requires the teams in the API url! 
def collectHomeBoxscore(teamAbbreviation, season):
    homeBoxscore = []
    response = basicAPICall(season, 'boxscore')
    for i in range(len(response['game'])):
        if(response['game'][i]['homeTeam']['abbreviation'] == teamAbbreviation):
            homeBoxscore.append(response['gamelogs'][i])
    return homeBoxscore

def collectAllHomeBoxscore(teamAbbreviation):
    homeBoxscore = []
    for i in range (2016, 2019):
        homeBoxscore.append(collectHomeBoxscore(teamAbbreviation, str(i)))
    return homeBoxscore


def collectAwayBoxscore(teamAbbreviation, season):
    awayBoxscore = []
    response = basicAPICall(season, 'boxscore')
    for i in range(len(response['game'])):
        if(response['game'][i]['awayTeam']['abbreviation'] == teamAbbreviation):
            awayBoxscore.append(response['gamelogs'][i])
    return awayBoxscore

def collectAllAwayBoxscore(teamAbbreviation):
    awayBoxscore = []
    for i in range (2016, 2019):
        awayBoxscore.append(collectAwayBoxscore(teamAbbreviation, str(i)))
    return awayBoxscore


collectAllHomeGames('OAK')




# print(len(collectAllHomeGames('OAK', '2016')[2]))


def testAPICall(season, keyword):
    try:
        response = requests.get(
            url='https://api.mysportsfeeds.com/v2.1/pull/mlb/' + season + '-regular/' + keyword + '.json?team=det',
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format(api_key,pswrd).encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
