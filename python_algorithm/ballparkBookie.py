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
    print('BASIC API CALL : ', keyword, ' year : ', season)
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
    print('Lineup API CALL, game id : ', id, ' year : ', season)
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




# PICKLE STUFF. We make the API Calls here, and use the data collected later. We can change seasons manually to use different years.

season = '2016'

# GAMES RESPONSE
if os.path.exists('games_response_' + season + '.pkl'):
    games_call_response = pickle.load(open('games_response_' + season + '.pkl', 'rb'))
else:
    games_call_response = basicAPICall(season + '-regular/', 'games', 'json')
    pickle.dump( games_call_response, open( 'games_response_' + season + '.pkl', 'wb' ) )


# Collect all game ids
game_ids = []
for i in range(len(games_call_response['games'])):
    game_ids.append(games_call_response['games'][i]['schedule']['id'])

# PLAYER STATS RESPONSE
if os.path.exists('player_stats_' + season + '.pkl'):
    player_stats_totals_response = pickle.load(open('player_stats_' + season + '.pkl', 'rb'))
else:
    player_stats_totals_response = basicAPICall(season + '-regular/', 'player_stats_totals', 'json')
    pickle.dump( player_stats_totals_response, open( 'player_stats_' + season + '.pkl', 'wb' ) )

# TEAM STATS RESPONSE
if os.path.exists('team_stats_' + season + '.pkl'):
    team_stats_totals_response = pickle.load(open('team_stats_' + season + '.pkl', 'rb'))
else:
    team_stats_totals_response = basicAPICall(season + '-regular/', 'team_stats_totals', 'json')
    pickle.dump( team_stats_totals_response, open( 'team_stats_' + season + '.pkl', 'wb' ))

# LINEUPS RESPONSE
if os.path.exists('lineup_responses_' + season + '.pkl'):
    lineup_call_responses = pickle.load(open('lineup_responses_' + season + '.pkl', 'rb'))
else:
    lineup_call_responses = dict()
    for i in range(len(game_ids)):
        print('GAME ', i)
        lineup_call_response = lineupAPICall(season, game_ids[i])
        lineup_call_responses[game_ids[i]] = lineup_call_response
    pickle.dump(lineup_call_responses, open('lineup_responses_' + season + '.pkl', 'wb' ))





# Creates an array of 1s for wins and 0s for losses : 1 = away wins, 0 = home wins.
def create_win_list(season):
    win_list = []
    games_call_response = pickle.load(open('games_response_' + season + '.pkl', 'rb'))
    for i in range(len(games_call_response['games'])):
        if(games_call_response['games'][i]['score']['awayScoreTotal'] > games_call_response['games'][i]['score']['homeScoreTotal']):
            win_list.append(1)
        else:
            win_list.append(0)
    return win_list


# global variable.
win_list = create_win_list('2017')

pickle.dump( win_list, open( 'win_list_' + season + '.pkl', 'wb' ))



# We make this dictionary to make a consistent order for all 19 positions.
position_dictionary = dict()
position_dictionary['1B'] = 0
position_dictionary['2B'] = 1
position_dictionary['3B'] = 2
position_dictionary['BO1'] = 3
position_dictionary['BO2'] = 4
position_dictionary['BO3'] = 5
position_dictionary['BO4'] = 6
position_dictionary['BO5'] = 7
position_dictionary['BO6'] = 8
position_dictionary['BO7'] = 9
position_dictionary['BO8'] = 10
position_dictionary['BO9'] = 11
position_dictionary['C'] = 12
position_dictionary['CF'] = 13
position_dictionary['DH'] = 14
position_dictionary['LF'] = 15
position_dictionary['P'] = 16
position_dictionary['RF'] = 17
position_dictionary['SS'] = 18
# We remove OF. We have always null IDs in 2019, not worth keeping
# position_dictionary['OF'] = 19



# List of all player stats we are collecting, 4 categories
player_stats_batting = ['atBats', 'batter2SeamFastballs', 'batter4SeamFastballs', 'batterChangeups',
'batterCurveballs', 'batterCutters', 'batterDoublePlays', 'batterFlyBalls', 'batterFlyOuts', 'batterForceOuts', 
'batterGroundBalls', 'batterGroundOuts', 'batterGroundOutToFlyOutRatio', 'batterIntentionalWalks', 'batterLineDrives', 
'batterOnBasePct', 'batterOnBasePlusSluggingPct', 'batterPutOuts', 'batterSacrificeBunts', 'batterSacrificeFlies', 
'batterSinkers', 'batterSliders', 'batterSluggingPct', 'batterSplitters', 'batterStolenBasePct', 'batterStrikeouts', 
'batterStrikes', 'batterStrikesFoul', 'batterStrikesLooking', 'batterStrikesMiss', 'batterSwings', 'batterTagOuts', 
'batterTriplePlays', 'batterWalks', 'battingAvg', 'caughtBaseSteals', 'earnedRuns', 'extraBaseHits', 'hitByPitch', 
'hits', 'homeruns', 'leftOnBase', 'pitchesFaced', 'plateAppearances', 'runs', 'runsBattedIn', 'secondBaseHits', 'stolenBases',
'thirdBaseHits', 'totalBases', 'unearnedRuns']
player_stats_fielding = ['inningsPlayed', 'totalChances', 'fielderTagOuts', 'fielderForceOuts', 'fielderPutOuts', 'outsFaced', 
'assists', 'errors', 'fielderDoublePlays', 'fielderTriplePlays', 'fielderStolenBasesAllowed', 'fielderCaughtStealing', 
'fielderStolenBasePct', 'passedBalls', 'fielderWildPitches', 'fieldingPct', 'rangeFactor']
player_stats_pitching = ['wins', 'losses', 'earnedRunAvg', 'saves', 'saveOpportunities', 'inningsPitched', 'hitsAllowed', 
'secondBaseHitsAllowed', 'thirdBaseHitsAllowed', 'runsAllowed', 'earnedRunsAllowed', 'homerunsAllowed', 'pitcherWalks', 
'pitcherSwings', 'pitcherStrikes', 'pitcherStrikesFoul', 'pitcherStrikesMiss', 'pitcherStrikesLooking', 'pitcherGroundBalls', 
'pitcherFlyBalls', 'pitcherLineDrives', 'pitcher2SeamFastballs', 'pitcher4SeamFastballs', 'pitcherCurveballs', 'pitcherChangeups', 
'pitcherCutters', 'pitcherSliders', 'pitcherSinkers', 'pitcherSplitters', 'pitcherSacrificeBunts', 'pitcherSacrificeFlies', 
'pitcherStrikeouts', 'pitchingAvg', 'walksAndHitsPerInningPitched', 'completedGames', 'shutouts', 'battersHit', 
'pitcherIntentionalWalks', 'gamesFinished', 'holds', 'pitcherDoublePlays', 'pitcherTriplePlays', 'pitcherGroundOuts', 
'pitcherFlyOuts', 'pitcherWildPitches', 'balks', 'pitcherStolenBasesAllowed', 'pitcherCaughtStealing', 'pickoffAttempts', 
'pickoffs', 'totalBattersFaced', 'pitchesThrown', 'winPct', 'pitcherGroundOutToFlyOutRatio', 'pitcherOnBasePct', 
'pitcherSluggingPct', 'pitcherOnBasePlusSluggingPct', 'strikeoutsPer9Innings', 'walksAllowedPer9Innings', 'hitsAllowedPer9Innings', 
'strikeoutsToWalksRatio', 'pitchesPerInning', 'pitcherAtBats']
player_stats_miscellaneous = ['gamesStarted']



def collect_player_stats(game_id):
    # No need to save the differences to pkl file because they do not require API connection
    # lineup is the lineup of the game with the game_id given as input
    lineup = lineup_call_responses[game_id]
    home_team_id = lineup['game']['homeTeam']['id']
    away_team_id = lineup['game']['awayTeam']['id']
    # We use this array to store all the player ids.
    # 38 because we have 19*2 players
    store_player_ids = [0]*38
    # AWAY TEAM : we collect IDs.
    for i in range(len(lineup['teamLineups'][0]['actual']['lineupPositions'])):
        if(lineup['teamLineups'][0]['actual']['lineupPositions'][i]['position'] != 'OF'):
            index = position_dictionary[lineup['teamLineups'][0]['actual']['lineupPositions'][i]['position']]
            if(lineup['teamLineups'][0]['actual']['lineupPositions'][i]['player'] is not None):
                store_player_ids[index] = lineup['teamLineups'][0]['actual']['lineupPositions'][i]['player']['id']
    # HOME TEAM : we collect IDs.
    for i in range(len(lineup['teamLineups'][1]['actual']['lineupPositions'])):
        if(lineup['teamLineups'][1]['actual']['lineupPositions'][i]['position'] != 'OF'):
            index = position_dictionary[lineup['teamLineups'][1]['actual']['lineupPositions'][i]['position']]
            if(lineup['teamLineups'][1]['actual']['lineupPositions'][i]['player'] is not None):
                # We use 19, because there are 19 players on each team
                store_player_ids[19 + index] = lineup['teamLineups'][1]['actual']['lineupPositions'][i]['player']['id']
    # IF NULL, the array is already filled with zeros, therefore if there is a zero, that means that it is a null player.
    # unique_players is a boolean array : False if the id has been seen earlier in the array, else : True
    # We do this because if we do operations on a player stats, they will change the player stats in multiple positions.
    # We make sure that we don't do operations on one player twice (ex : divide stats by games twice)
    unique_players = []
    for i in range(len(store_player_ids)):
        if(store_player_ids[i] in store_player_ids[0:i] or store_player_ids[i] == 0):
            unique_players.append(False)
        else:
            unique_players.append(True)
    # player_stats is an array  that will be of length 38
    # We fill it up with a dictionary of stats for each player
    # Keep in mind that the length of each player stats is one element in the array.
    players_stats = []
    # We cycle through the player ids in the lineup
    for i in range(len(store_player_ids)):
        # We cycle through the entire list of players in the stats API response (or pkl file).
        for j in range(len(player_stats_totals_response['playerStatsTotals'])):
            # Zero if the player is null (away_player_id == 0).
            # Break because we already  know that the player in question is null and don't want to append more.
            # We make sure the length is equal to the number of players.
            if(store_player_ids[i] == 0):
                players_stats.append(0)
                break
            # AWAY TEAM
            # We append the stats (ONE ELEMENT in the array)
            if(i < 19):
                # Check that the id matches, as well as the team id
                # We check the team id because some players transfer during the year and the stats are different depending on the team.
                if(store_player_ids[i] == player_stats_totals_response['playerStatsTotals'][j]['player']['id'] and  
                away_team_id == player_stats_totals_response['playerStatsTotals'][j]['team']['id']):
                    players_stats.append(player_stats_totals_response['playerStatsTotals'][j]['stats'])
            # HOME TEAM
            # We append the stats (ONE ELEMENT in the array)
            else:
                # Check that the id matches, as well as the team id
                # We check the team id because some players transfer during the year and the stats are different depending on the team.
                if(store_player_ids[i] == player_stats_totals_response['playerStatsTotals'][j]['player']['id'] and  
                home_team_id == player_stats_totals_response['playerStatsTotals'][j]['team']['id']):
                    players_stats.append(player_stats_totals_response['playerStatsTotals'][j]['stats'])
    # We cycle thru the 38 player stats each element is a dictionary or a zero
    for i in range(len(players_stats)):
        # If we have not already divided stats by games played on this player : 
        if(unique_players[i]):
            # cycle through the dictionary and divide by games played for batting and fielding
            for b in range(len(player_stats_batting)):
                players_stats[i]['batting'][player_stats_batting[b]] = players_stats[i]['batting'][player_stats_batting[b]] / players_stats[i]['gamesPlayed']
            for f in range(len(player_stats_fielding)):
                players_stats[i]['fielding'][player_stats_fielding[f]] = players_stats[i]['fielding'][player_stats_fielding[f]] / players_stats[i]['gamesPlayed']
            for m in range(len(player_stats_miscellaneous)):
                players_stats[i]['miscellaneous'][player_stats_miscellaneous[m]] = players_stats[i]['miscellaneous'][player_stats_miscellaneous[m]] / players_stats[i]['gamesPlayed']
            # Special case : pitcher. They are always placed at index 16 (away), and 35 (home). 35 = 16+ 19
            if(i == 16 or i == 35):
                for p in range(len(player_stats_pitching)):
                    players_stats[i]['pitching'][player_stats_pitching[p]] = players_stats[i]['pitching'][player_stats_pitching[p]] / players_stats[i]['gamesPlayed']
    # We return the 38 or so list of dictionaries where each value is divided by the number of games played (with zeros for the null players)
    return players_stats



# SAME THING BUT EXPECTED 
def collect_expected_player_stats(game_id):
    # No need to save the differences to pkl file because they do not require API connection
    # lineup is the lineup of the game with the game_id given as input
    lineup = lineup_call_responses[game_id]
    home_team_id = lineup['game']['homeTeam']['id']
    away_team_id = lineup['game']['awayTeam']['id']
    # We use this array to store all the player ids.
    # 38 because we have 19*2 players
    store_player_ids = [0]*38
    # AWAY TEAM : we collect IDs.
    for i in range(len(lineup['teamLineups'][0]['expected']['lineupPositions'])):
        if(lineup['teamLineups'][0]['expected']['lineupPositions'][i]['position'] != 'OF'):
            index = position_dictionary[lineup['teamLineups'][0]['expected']['lineupPositions'][i]['position']]
            if(lineup['teamLineups'][0]['expected']['lineupPositions'][i]['player'] is not None):
                store_player_ids[index] = lineup['teamLineups'][0]['expected']['lineupPositions'][i]['player']['id']
    # HOME TEAM : we collect IDs.
    for i in range(len(lineup['teamLineups'][1]['expected']['lineupPositions'])):
        if(lineup['teamLineups'][1]['expected']['lineupPositions'][i]['position'] != 'OF'):
            index = position_dictionary[lineup['teamLineups'][1]['expected']['lineupPositions'][i]['position']]
            if(lineup['teamLineups'][1]['expected']['lineupPositions'][i]['player'] is not None):
                # We use 19, because there are 19 players on each team
                store_player_ids[19 + index] = lineup['teamLineups'][1]['expected']['lineupPositions'][i]['player']['id']
    # IF NULL, the array is already filled with zeros, therefore if there is a zero, that means that it is a null player.
    # unique_players is a boolean array : False if the id has been seen earlier in the array, else : True
    # We do this because if we do operations on a player stats, they will change the player stats in multiple positions.
    # We make sure that we don't do operations on one player twice (ex : divide stats by games twice)
    unique_players = []
    for i in range(len(store_player_ids)):
        if(store_player_ids[i] in store_player_ids[0:i] or store_player_ids[i] == 0):
            unique_players.append(False)
        else:
            unique_players.append(True)
    # player_stats is an array  that will be of length 38
    # We fill it up with a dictionary of stats for each player
    # Keep in mind that the length of each player stats is one element in the array.
    players_stats = []
    # We cycle through the player ids in the lineup
    for i in range(len(store_player_ids)):
        # We cycle through the entire list of players in the stats API response (or pkl file).
        for j in range(len(player_stats_totals_response['playerStatsTotals'])):
            # Zero if the player is null (away_player_id == 0).
            # Break because we already  know that the player in question is null and don't want to append more.
            # We make sure the length is equal to the number of players.
            if(store_player_ids[i] == 0):
                players_stats.append(0)
                break
            # AWAY TEAM
            # We append the stats (ONE ELEMENT in the array)
            if(i < 19):
                # Check that the id matches, as well as the team id
                # We check the team id because some players transfer during the year and the stats are different depending on the team.
                if(store_player_ids[i] == player_stats_totals_response['playerStatsTotals'][j]['player']['id'] and  
                away_team_id == player_stats_totals_response['playerStatsTotals'][j]['team']['id']):
                    players_stats.append(player_stats_totals_response['playerStatsTotals'][j]['stats'])
            # HOME TEAM
            # We append the stats (ONE ELEMENT in the array)
            else:
                # Check that the id matches, as well as the team id
                # We check the team id because some players transfer during the year and the stats are different depending on the team.
                if(store_player_ids[i] == player_stats_totals_response['playerStatsTotals'][j]['player']['id'] and  
                home_team_id == player_stats_totals_response['playerStatsTotals'][j]['team']['id']):
                    players_stats.append(player_stats_totals_response['playerStatsTotals'][j]['stats'])
    # We cycle thru the 38 player stats each element is a dictionary or a zero
    for i in range(len(players_stats)):
        # If we have not already divided stats by games played on this player : 
        if(unique_players[i]):
            # cycle through the dictionary and divide by games played for batting and fielding
            for b in range(len(player_stats_batting)):
                players_stats[i]['batting'][player_stats_batting[b]] = players_stats[i]['batting'][player_stats_batting[b]] / players_stats[i]['gamesPlayed']
            for f in range(len(player_stats_fielding)):
                players_stats[i]['fielding'][player_stats_fielding[f]] = players_stats[i]['fielding'][player_stats_fielding[f]] / players_stats[i]['gamesPlayed']
            for m in range(len(player_stats_miscellaneous)):
                players_stats[i]['miscellaneous'][player_stats_miscellaneous[m]] = players_stats[i]['miscellaneous'][player_stats_miscellaneous[m]] / players_stats[i]['gamesPlayed']
            # Special case : pitcher. They are always placed at index 16 (away), and 35 (home). 35 = 16+ 19
            if(i == 16 or i == 35):
                for p in range(len(player_stats_pitching)):
                    players_stats[i]['pitching'][player_stats_pitching[p]] = players_stats[i]['pitching'][player_stats_pitching[p]] / players_stats[i]['gamesPlayed']
    # We return the 38 or so list of dictionaries where each value is divided by the number of games played (with zeros for the null players)
    return players_stats


# collect_expected_player_stats(48847)


# Function to convert a 38 or so list of dictionaries to a longer list of just numbers
def stats_to_float(stats, year):
    float_array = []
    # We cycle thru the 38 or so dictionaries
    for i in range(len(stats)):
        # If null player : We want to append average values for given position over a given season
        # TODO This is where we need to implement the player average stats function
        # PROBLEM : The function is SUPER slow. I don't want to call it dynamically or it'll take way too long
        if(stats[i] == 0):
            # This is how we will implement the average player stats : 
            # Find the position we need by cycling thru the dictionary
            for position, index in position_dictionary.items():    # for name, age in dictionary.iteritems():  (for Python 2.x)
                if index == i:
                    # Function that returns the average player stats array
                    average_for_null_player(year, position)
        # If not null : 
        else:
            # Append batting stats
            for b in range(len(player_stats_batting)):
                float_array.append(stats[i]['batting'][player_stats_batting[b]])
            # Append fielding stats
            for f in range(len(player_stats_fielding)):
                float_array.append(stats[i]['fielding'][player_stats_fielding[f]])
            # Append miscellaneous
            for m in range(len(player_stats_miscellaneous)):
                float_array.append(stats[i]['miscellaneous'][player_stats_miscellaneous[m]])
            # If pitcher, append pitching stats
            if(i == 16 or i == 35):
                for p in range(len(player_stats_pitching)):
                    float_array.append(stats[i]['pitching'][player_stats_pitching[p]])
    # Returns a long array of all 40 player stats, just the numbers (divided by the number of games played)
    return float_array





def player_away_minus_home(stats):
    result = []
    # We need int() because the division transforms the integer to float.
    # Cycle through half the stats
    for i in range(int(len(stats) / 2)):
        # Append the home - away stats
        # The position of the first home stat = int(len(stats) / 2)
        result.append( stats[i] - stats[int(len(stats) / 2) + i] )
    return result


# This is an example on how we are going to collect the proper player stats for each lineup
# a = collect_player_stats(48847)
# b = stats_to_float(a)
# c = player_away_minus_home(b)


# List of all team stats we are collecting, 4 categories
team_stats_batting = ['atBats', 'runs', 'hits', 'secondBaseHits', 'thirdBaseHits', 'homeruns', 'runsBattedIn', 'earnedRuns', 
'unearnedRuns', 'batterWalks', 'batterSwings', 'batterStrikes', 'batterStrikesFoul', 'batterStrikesMiss', 'batterStrikesLooking', 
'batterGroundBalls', 'batterFlyBalls', 'batterLineDrives', 'batterStrikeouts', 'batter2SeamFastballs', 'batter4SeamFastballs', 
'batterCurveballs', 'batterChangeups', 'batterCutters', 'batterSliders', 'batterSinkers', 'batterSplitters', 'leftOnBase', 
'opponentsLeftOnBase', 'stolenBases', 'caughtBaseSteals', 'batterStolenBasePct', 'battingAvg', 'batterOnBasePct', 
'batterSluggingPct', 'batterOnBasePlusSluggingPct', 'batterIntentionalWalks', 'hitByPitch', 'batterSacrificeBunts', 
'batterSacrificeFlies', 'totalBases', 'extraBaseHits', 'batterDoublePlays', 'batterTriplePlays', 'batterTagOuts', 
'batterForceOuts', 'batterPutOuts', 'batterGroundOuts', 'batterFlyOuts', 'batterGroundOutToFlyOutRatio', 'pitchesFaced', 
'plateAppearances', 'opponentAtBats']
team_stats_pitching = ['earnedRunAvg', 'inningsPitched', 'hitsAllowed', 'secondBaseHitsAllowed', 'thirdBaseHitsAllowed', 
'runsAllowed', 'earnedRunsAllowed', 'homerunsAllowed', 'pitcherWalks', 'pitcherSwings', 'pitcherStrikes', 'pitcherStrikesFoul', 
'pitcherStrikesMiss', 'pitcherStrikesLooking', 'pitcherGroundBalls', 'pitcherFlyBalls', 'pitcherLineDrives', 
'pitcherSacrificeBunts', 'pitcher2SeamFastballs', 'pitcher4SeamFastballs', 'pitcherCurveballs', 'pitcherChangeups', 
'pitcherCutters', 'pitcherSliders', 'pitcherSinkers', 'pitcherSplitters', 'pitcherSacrificeFlies', 'pitcherStrikeouts', 
'pitchingAvg', 'walksAndHitsPerInningPitched', 'shutouts', 'battersHit', 'pitcherIntentionalWalks', 'pitcherGroundOuts', 
'pitcherFlyOuts', 'pitcherWildPitches', 'balks', 'pitcherStolenBasesAllowed', 'pitcherCaughtStealing', 'pickoffs', 
'pickoffAttempts', 'totalBattersFaced', 'pitchesThrown', 'pitcherGroundOutToFlyOutRatio', 'pitcherOnBasePct', 
'pitcherSluggingPct', 'pitcherOnBasePlusSluggingPct', 'strikeoutsPer9Innings', 'walksAllowedPer9Innings', 
'hitsAllowedPer9Innings', 'strikeoutsToWalksRatio', 'pitchesPerInning']
team_stats_fielding = ['inningsPlayed', 'totalChances', 'fielderTagOuts', 'fielderForceOuts', 'fielderPutOuts', 'assists', 
'errors', 'fielderDoublePlays', 'fielderTriplePlays', 'fielderStolenBasesAllowed', 'fielderCaughtStealing', 'fielderStolenBasePct', 
'passedBalls', 'fielderWildPitches', 'fieldingPct', 'defenceEfficiencyRatio', 'outsFaced']
team_stats_standings = ['wins', 'losses', 'winPct', 'gamesBack', 'runsFor', 'runsAgainst', 'runDifferential']

# This function returns the away minus home team stats given a game ID
def collect_team_stats(game_id):
    away_team_stats = []
    home_team_stats = []
    # We use the lineup data to get the home and away team IDs
    # We do this because lineup is the only call we use where we can just input a game id and get information 
    # on that specific game
    away_id = lineup_call_responses[game_id]['game']['awayTeam']['id']
    home_id = lineup_call_responses[game_id]['game']['homeTeam']['id']
    # We cycle through all the teams in the MLB to find the right team and stats
    for i in range(len(team_stats_totals_response['teamStatsTotals'])):
        # AWAY TEAM
        # If the game away id == team stats id, append the stats to the away team stats array
        if(away_id == team_stats_totals_response['teamStatsTotals'][i]['team']['id']):
            # Batting stats
            for b in range(len(team_stats_batting)):
                away_team_stats.append(team_stats_totals_response['teamStatsTotals'][i]['stats']['batting'][team_stats_batting[b]])
            # Pitching stats
            for p in range(len(team_stats_pitching)):
                away_team_stats.append(team_stats_totals_response['teamStatsTotals'][i]['stats']['pitching'][team_stats_pitching[p]])
            # Fielding stats
            for f in range(len(team_stats_fielding)):
                away_team_stats.append(team_stats_totals_response['teamStatsTotals'][i]['stats']['fielding'][team_stats_fielding[f]])
            # Standings
            for s in range(len(team_stats_standings)):
                away_team_stats.append(team_stats_totals_response['teamStatsTotals'][i]['stats']['standings'][team_stats_standings[s]])
        # HOME TEAM Same as above
        elif(home_id == team_stats_totals_response['teamStatsTotals'][i]['team']['id']):
            for b in range(len(team_stats_batting)):
                home_team_stats.append(team_stats_totals_response['teamStatsTotals'][i]['stats']['batting'][team_stats_batting[b]])
            for p in range(len(team_stats_pitching)):
                home_team_stats.append(team_stats_totals_response['teamStatsTotals'][i]['stats']['pitching'][team_stats_pitching[p]])
            for f in range(len(team_stats_fielding)):
                home_team_stats.append(team_stats_totals_response['teamStatsTotals'][i]['stats']['fielding'][team_stats_fielding[f]])
            for s in range(len(team_stats_standings)):
                home_team_stats.append(team_stats_totals_response['teamStatsTotals'][i]['stats']['standings'][team_stats_standings[s]])
    # We create a new array where we are going to subtract the home minus the home stats
    away_minus_home = []
    # Cycle thru one of the arrays and subtract away minus home stats
    for i in range(len(home_team_stats)):
        away_minus_home.append(away_team_stats[i] - home_team_stats[i])
    return away_minus_home

# This is a function where, given a venue and team id, we are going to return a winning percentage
# of that team at that venue
def venue_win(venue_id, team_id):
    wins = 0
    losses = 0
    # Cycle through the list of all games in a season
    for i in range(len(games_call_response['games'])):
        # If the team_id matches the id of the away team that played, and the venue_id matches the venue id at that game
        if(team_id == games_call_response['games'][i]['schedule']['awayTeam']['id']
        and venue_id == games_call_response['games'][i]['schedule']['venue']['id']):
        # If the away score is greater than the home score, it's a win, otherwise it's a loss
            if(games_call_response['games'][i]['score']['awayScoreTotal'] > games_call_response['games'][i]['score']['homeScoreTotal']):
                wins += 1
            else:
                losses += 1
        # Exactly the same thing but for the home team
        elif(team_id == games_call_response['games'][i]['schedule']['homeTeam']['id']
        and venue_id == games_call_response['games'][i]['schedule']['venue']['id']):
            if(games_call_response['games'][i]['score']['awayScoreTotal'] < games_call_response['games'][i]['score']['homeScoreTotal']):
                wins += 1
            else:
                losses += 1
    # We get a win percentage
    win_percentage = wins / (wins+losses)
    # If a team has never played at the given venue, we give that team a 50% winning rate.
    if(losses == 0 and wins == 0):
        win_percentage = 0.5
    return win_percentage

# This is an example of how we are going to collect the venue team win percentage
venue_win_test = venue_win(115, 121)


# Function that, given a year and position returns an array of the average stats for a player in that position
# in that year.
# Make sure to input year as a string
def averages_for_null_players(year, position):
    # We use games_call_response_year and it reads the specific file with that year
    games_call_response_year = pickle.load(open('games_response_' + year + '.pkl', 'rb'))
    # We use player_stats_totals_response_year and it reads the specific file with that year
    player_stats_totals_response_year = pickle.load(open('player_stats_' + year + '.pkl', 'rb'))
    # We collect all game IDs of given year
    game_ids = []
    for i in range(len(games_call_response_year['games'])):
        game_ids.append(games_call_response_year['games'][i]['schedule']['id'])
    # We need to keep the sum of games played in that position
    games_played = 0
    # If it's a pitcher, we create an array of pitcher stats length
    if(position == 'P'):
        sum_of_stats = [0] * (len(player_stats_batting) + len(player_stats_fielding) + len(player_stats_miscellaneous) + len(player_stats_pitching))
    # Otherwise, we create an array of normal stats length
    else:
        sum_of_stats = [0] * (len(player_stats_batting) + len(player_stats_fielding) + len(player_stats_miscellaneous))
    # Now we cycle through all the games in that given year
    for i in range(len(game_ids)):
        print('GAME ', i, 'Position = ', position)
        # We use lineup_call_responses_year because it reads the specific file with that year
        lineup_call_responses_year = pickle.load(open('lineup_responses_' + year +'.pkl', 'rb'))
        # lineup = The lineup of game i
        lineup = lineup_call_responses_year[game_ids[i]]
        away_team_id = lineup['game']['awayTeam']['id']
        home_team_id = lineup['game']['homeTeam']['id']
        # AWAY TEAM We cycle through the actual positions. 
        # We are trying to collect the ID of the player in this position
        for j in range(len(lineup['teamLineups'][0]['actual']['lineupPositions'])):
            # Check if player is null and if the position of that player matches our input
            if(lineup['teamLineups'][0]['actual']['lineupPositions'][j]['player'] is not None 
            and position == lineup['teamLineups'][0]['actual']['lineupPositions'][j]['position']):
                away_player_id = lineup['teamLineups'][0]['actual']['lineupPositions'][j]['player']['id']
                # We break out of the loop because we found the away player in the right position
                break
        # HOME TEAM We cycle through the actual positions. 
        # We are trying to collect the ID of the player in this position
        for j in range(len(lineup['teamLineups'][1]['actual']['lineupPositions'])):
            # Check if player is null and if the position of that player matches our input
            if(lineup['teamLineups'][1]['actual']['lineupPositions'][j]['player'] is not None 
            and position == lineup['teamLineups'][1]['actual']['lineupPositions'][j]['position']):
                # Append the id of the player in the right position to our list of player IDs
                home_player_id = lineup['teamLineups'][1]['actual']['lineupPositions'][j]['player']['id']
                # We break out of the loop because we found the player in the right position
                break
        # Cycle through the player stats to find the right player
        for j in range(len(player_stats_totals_response_year['playerStatsTotals'])):
            # We have to check whether or not the player is defined or not, we save boolean variables
            try:
                away_player_id
            except NameError:
                away_player_id_defined = False
            else:
                away_player_id_defined = True
            try:
                home_player_id
            except NameError:
                home_player_id_defined = False
            else:
                home_player_id_defined = True
            # If the IDs match, and the away Team matches with the player's team
            # OR the IDs match, and the home Team matches with the player's team
            if(home_player_id_defined and away_player_id_defined and ((away_player_id == player_stats_totals_response_year['playerStatsTotals'][j]['player']['id']
            and away_team_id == player_stats_totals_response_year['playerStatsTotals'][j]['team']['id'])
            or (home_player_id == player_stats_totals_response_year['playerStatsTotals'][j]['player']['id']
            and home_team_id == player_stats_totals_response_year['playerStatsTotals'][j]['team']['id']))):
                # Increment games_played
                games_played += player_stats_totals_response_year['playerStatsTotals'][j]['stats']['gamesPlayed']
                # Sum batting, fielding, and miscellaneous to sum_of_stats
                for b in range(len(player_stats_totals_response_year['playerStatsTotals'][j]['stats']['batting'])):
                    sum_of_stats[b] += player_stats_totals_response_year['playerStatsTotals'][j]['stats']['batting'][player_stats_batting[b]]
                for f in range(len(player_stats_totals_response_year['playerStatsTotals'][j]['stats']['fielding'])):
                    sum_of_stats[len(player_stats_totals_response_year['playerStatsTotals'][j]['stats']['batting']) + f] += player_stats_totals_response_year['playerStatsTotals'][j]['stats']['fielding'][player_stats_fielding[f]]
                for m in range(len(player_stats_totals_response_year['playerStatsTotals'][j]['stats']['miscellaneous'])):
                    sum_of_stats[len(player_stats_totals_response_year['playerStatsTotals'][j]['stats']['batting']) + len(player_stats_totals_response_year['playerStatsTotals'][j]['stats']['fielding']) + m] += player_stats_totals_response_year['playerStatsTotals'][j]['stats']['miscellaneous'][player_stats_miscellaneous[m]]
                # I GOT THIS SUPER FUCKING ERROR, SO I ADDED THIS
                if 'pitching' in player_stats_totals_response_year['playerStatsTotals'][j]['stats']:
                    pitching_stats_exist = True
                else:
                    pitching_stats_exist = False
                # If the player is a pitcher, add pitching stats as well
                if(position == 'P' and pitching_stats_exist):
                    for p in range(len(player_stats_totals_response_year['playerStatsTotals'][j]['stats']['pitching'])):
                        sum_of_stats[len(player_stats_totals_response_year['playerStatsTotals'][j]['stats']['batting']) + len(player_stats_totals_response_year['playerStatsTotals'][j]['stats']['fielding']) + len(player_stats_totals_response_year['playerStatsTotals'][j]['stats']['miscellaneous']) + p] += player_stats_totals_response_year['playerStatsTotals'][j]['stats']['pitching'][player_stats_pitching[p]]
    # Divide the sum of stats by the total number of games played
    for i in range(len(sum_of_stats)):
        sum_of_stats[i] = sum_of_stats[i] / games_played
    # We return a huge array
    return sum_of_stats



positions = ['1B', '2B', '3B', 'BO1', 'BO2', 'BO3','BO4','BO5','BO6','BO7','BO8','BO9','C','CF','DH','LF', 'P','RF','SS']


for i in range(len(positions)):
    if os.path.exists('average_' + positions[i] + '_' + season + '.pkl'):
        average_position = pickle.load(open('average_' + positions[i] + '_' + season + '.pkl', 'rb'))
    else:
        print('positions[i] =', positions[i])
        average_position = averages_for_null_players(season, positions[i])
        pickle.dump( average_position, open( 'average_' + positions[i] + '_' + season + '.pkl', 'wb' ) )





def average_for_null_player(season, position):
    if os.path.exists('average_' + position + '_' + season + '.pkl'):
        average_position = pickle.load(open('average_' + position + '_' + season + '.pkl', 'rb'))
    else:
        average_position = averages_for_null_players(season, position)
        pickle.dump( average_position, open( 'average_' + position + '_' + season + '.pkl', 'wb' ) )
    return average_position


# Concatenate all 4 years of winlists to get one long array of 0s and 1s.

def concatenate_winlists():
    win_list_2016 = pickle.load(open('win_list_2016.pkl', 'rb'))
    win_list_2017 = pickle.load(open('win_list_2017.pkl', 'rb'))
    win_list_2018 = pickle.load(open('win_list_2018.pkl', 'rb'))
    win_list_2019 = pickle.load(open('win_list_2019.pkl', 'rb'))
    return (win_list_2016 + win_list_2017 + win_list_2018 + win_list_2019)

all_win_lists = concatenate_winlists()




# for each game, team stats, venue, player 


def create_training_arrays():
    return 0





# print(pickle.load(open('average_P_2019.pkl', 'rb'))[0:4])
# print(pickle.load(open('average_P_2018.pkl', 'rb'))[0:4])


# TODO :  
# - Buy access to the odds. At least get approval from BJ to give some money 

# - Cycle thru all games and make 2d array with differences for team, players and venues.
# - Sanitize and normalize data using last semester's functions


# Next week let's train the model.

# QUESTIONS :
# What happens if a player is null in 2020?
# We need to use an average position stat. Should we use the average of 2019? Or the average of all years?



# USED ONLY FOR DEBUGGING : 
# THE COMMENTED CODE BELOW PRINTS A LIST OF NUMBER OF TIMES IT HAS SEEN POSITIONS NULL
# AFTER RUNNING IT FOR OVER HALF OF 2019, THE FOLLOWING POSITIONS WERE NULL AT LEAST ONCE
# null_positions = ['BO2', 'BO6', 'BO7', 'BO9', 'DH', 'OF']




# number_of_null_players = [0]*20
# for i in range(len(game_ids)):
# # for i in range(1):
#     lineup = lineup_call_responses[game_ids[i]]
#     # for a in range(len(lineup['teamLineups'][0]['expected']['lineupPositions'])):
#     #     if(lineup['teamLineups'][0]['expected']['lineupPositions'][a]['player'] is None):
#     #         number_of_null_players[position_dictionary[lineup['teamLineups'][0]['expected']['lineupPositions'][a]['position']]] += 1

#     # with open('lineup.txt', 'w') as f:
#     #     json.dump(lineup, f)
#     for j in range(len(lineup['teamLineups'][0]['actual']['lineupPositions'])):
#         if(lineup['teamLineups'][0]['actual']['lineupPositions'][j]['position'] == 'OF'):
#             away_position_of_OF = j
#     for j in range(len(lineup['teamLineups'][1]['actual']['lineupPositions'])):
#         if(lineup['teamLineups'][1]['actual']['lineupPositions'][j]['position'] == 'OF'):
#             home_position_of_OF = j
#     if(lineup['teamLineups'][0]['actual']['lineupPositions'][away_position_of_OF]['player'] is not None):
#         print('NOT NULL')
#     if(lineup['teamLineups'][1]['actual']['lineupPositions'][home_position_of_OF]['player'] is not None):
#         print('NOT NULL')
#     print('Game ', i)




    # for a in range(len(lineup['teamLineups'][0]['actual']['lineupPositions'])):
    #     if(lineup['teamLineups'][0]['actual']['lineupPositions'][a]['player'] is None):
    #         number_of_null_players[position_dictionary[lineup['teamLineups'][0]['actual']['lineupPositions'][a]['position']]] += 1
    # for a in range(len(lineup['teamLineups'][1]['expected']['lineupPositions'])):
    #     if(lineup['teamLineups'][1]['expected']['lineupPositions'][a]['player'] is None):
    #         number_of_null_players[position_dictionary[lineup['teamLineups'][1]['expected']['lineupPositions'][a]['position']]] += 1
    # for a in range(len(lineup['teamLineups'][1]['actual']['lineupPositions'])):
    #     if(lineup['teamLineups'][1]['actual']['lineupPositions'][a]['player'] is None):
    #         number_of_null_players[position_dictionary[lineup['teamLineups'][1]['actual']['lineupPositions'][a]['position']]] += 1
    # print('GAME ', i)
    # print(number_of_null_players)