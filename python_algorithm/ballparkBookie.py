import base64
import json
import requests
import csv
import pandas as pd
import numpy as np
import pickle
import os
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

api_key = "e0c4e5ec-08d5-414d-88ce-9b392f"
pswrd = "MYSPORTSFEEDS"
seasons = ['2016', '2017', '2018', '2019']

def basicAPICall(season, keyword, format):
    try:
        response = requests.get(
            url='https://api.mysportsfeeds.com/v2.1/pull/mlb/' + season + keyword + '.' + format,
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format(api_key,pswrd).encode('utf-8')).decode('ascii')
            }
        )
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    if(format == 'json'):
        return (json.loads(response.content))
    else:
        return (response.content)

def lineupAPICall(season, id):
    try:
        response = requests.get(
            url='https://api.mysportsfeeds.com/v2.1/pull/mlb/'+ season + '-regular/games/' + str(id) + '/lineup.json',
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


# We want to convert indicators from boolean to floats. 
# Venues = Instead of home / away,              input home % win, away % win
# Players = Instead of playing / Not playing,   input % win
# If I have enough time, collect all players stats (of the ones playing)

venues_call_response = basicAPICall('2019-regular/', 'venues', 'json')
venues_wins = [0]*len(venues_call_response['venues'])
venues_losses = [0]*len(venues_call_response['venues'])

highest_id = 148
indexes = [0] * highest_id
for i in range(len(venues_call_response['venues'])):
    indexes[venues_call_response['venues'][i]['venue']['id']] = i
# indexes[id] = index of the venue

games_call_response = basicAPICall('2019-regular/', 'games', 'json')

for i in range(len(games_call_response['games'])):
    index = indexes[games_call_response['games'][i]['schedule']['venue']['id']]
    if( games_call_response['games'][i]['score']['homeScoreTotal'] > games_call_response['games'][i]['score']['awayScoreTotal']):
        venues_wins[index] += 1
    else:
        venues_losses[index] += 1

venues_win_ratio = []
for i in range(len(venues_wins)):
    venues_win_ratio.append(venues_wins[i]/ (venues_losses[i] + venues_wins[i]))


# We need to use the fuckin IDs instead of dates and abbreviations n shit
game_ids = []
dates = []
home_abbreviations = []
away_abbreviations = []


for i in range(len(games_call_response['games'])):
    games_call_response['games'][i]['schedule']['id']
    game_ids.append(games_call_response['games'][i]['schedule']['id'])


# Now, we want to collect the players

# check that the number of players on the lineup is constant
lineup_response = []


for i in range(2400):
    print('GAME #', i)
    print(len(lineupAPICall('2019', game_ids[i])['teamLineups'][0]['actual']['lineupPositions']))
# Seems to always be 20 players


# Question for Wong : We have the actual team lineup and the expected team lineup.
# Which one should we use? Both? 
# Actual lineup : Obviously because they played
# Expected lineup : Because the expected lineup is all we have before a game
# Wong says actual lineups

home_players_ids = []
away_players_ids = []

number_of_players = 20

# for i in range(len(dates)):
#     lineup_response = lineupAPICall('2019', dates[i], home_abbreviations[i], away_abbreviations[i])
#     for j in range(number_of_players):
#         home_players_ids.append(lineup_response['teamLineups'][0]['expected']['lineupPositions'][j]['player']['id'])
#         away_players_ids.append(lineup_response['teamLineups'][1]['expected']['lineupPositions'][j]['player']['id'])


# We need to convert ids to indexes and store all the players stats
# 1. Find the largest id
# 2. create 0 array of that size
# 3. cycle thru the ids and add them one by one to the array

player_stats_totals_response = basicAPICall('2019-regular/', 'player_stats_totals', 'json')
number_of_players = len(player_stats_totals_response['playerStatsTotals'])
players_wins = [0]*number_of_players
players_losses = [0]*number_of_players

maximum_id = 17123




# for i in range(len(player_stats_totals_response['playerStatsTotals'])):
#     # print(i)
#     if(maximum_id < player_stats_totals_response['playerStatsTotals'][i]['player']['id']):
#         print(maximum_id)
#         print(i)
#         maximum_id = player_stats_totals_response['playerStatsTotals'][i]['player']['id']

# player_id_to_index = [0]*maximum_id


# for i in range(len(player_ids_to_index)):
#     player_id_to_index[player_stats_totals_response['playerStatsTotals'][i]['player']['id']] = i







# Now we can input player_id_to_index[id] = index

# Now we need to cycle thru the expected lineup
# Take the id of each player
# input that id in the id to index array, get the index
# Use that index to collect the palyer's stats
# collect all that into a data array (in order), there are 20 players


