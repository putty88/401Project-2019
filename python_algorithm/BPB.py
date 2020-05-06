import base64
import json
import requests
import numpy as np
import pickle
import os
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)



# initialize functions. I use global variables bc opening pkl files is slow and if we put it 
# in a for loop, it literally takes 10+ hours to run a season
win_list_2016 = pickle.load(open('win_list_2016.pkl', 'rb'))
win_list_2017 = pickle.load(open('win_list_2017.pkl', 'rb'))
win_list_2018 = pickle.load(open('win_list_2018.pkl', 'rb'))
win_list_2019 = pickle.load(open('win_list_2019.pkl', 'rb'))

games_response_2016 = pickle.load(open('games_response_2016.pkl', 'rb'))
games_response_2017 = pickle.load(open('games_response_2017.pkl', 'rb'))
games_response_2018 = pickle.load(open('games_response_2018.pkl', 'rb'))
games_response_2019 = pickle.load(open('games_response_2019.pkl', 'rb'))

def initialize_games_call_response(season):
    if(season == 2016):
        games_response = games_response_2016
    elif(season == 2017):
        games_response = games_response_2017
    elif(season == 2018):
        games_response = games_response_2018
    elif(season == 2019):
        games_response = games_response_2019
    return games_response

# I think we can delete lineups and just keep the all_lineups
lineups1 = pickle.load(open('lineups2.pkl', 'rb'))
lineups2 = pickle.load(open('lineups1.pkl', 'rb'))
all_lineups = {**lineups1, **lineups2}


team_stats_2016 = pickle.load(open('team_stats_2016.pkl', 'rb'))
team_stats_2017 = pickle.load(open('team_stats_2017.pkl', 'rb'))
team_stats_2018 = pickle.load(open('team_stats_2018.pkl', 'rb'))
team_stats_2019 = pickle.load(open('team_stats_2019.pkl', 'rb'))
def initialize_team_stats(season):
    if(season == 2016):
        team_stats = team_stats_2016
    elif(season == 2017):
        team_stats = team_stats_2017
    elif(season == 2018):
        team_stats = team_stats_2018
    elif(season == 2019):
        team_stats = team_stats_2019
    return team_stats

player_stats_2016 = pickle.load(open('player_stats_2016.pkl', 'rb'))
player_stats_2017 = pickle.load(open('player_stats_2017.pkl', 'rb'))
player_stats_2018 = pickle.load(open('player_stats_2018.pkl', 'rb'))
player_stats_2019 = pickle.load(open('player_stats_2019.pkl', 'rb'))
def initialize_player_stats(season):
    if(season == 2016):
        player_stats = player_stats_2016
    elif(season == 2017):
        player_stats = player_stats_2017
    elif(season == 2018):
        player_stats = player_stats_2018
    elif(season == 2019):
        player_stats = player_stats_2019
    return player_stats

# ========================================================================================================================================================

# Collect venue win percentage in a given season, team, and id
def venue_win(venue_id, team_id, season):
    games_response = initialize_games_call_response(season)
    wins = 0
    losses = 0
    # Cycle through all games
    for i in range(len(games_response['games'])):
        # If venue matches and team id is the away team : 
        if(games_response['games'][i]['schedule']['venue']['id'] == venue_id and games_response['games'][i]['schedule']['awayTeam']['id'] == team_id):
            # If the away team won
            if(games_response['games'][i]['score']['awayScoreTotal'] > games_response['games'][i]['score']['homeScoreTotal']):
                wins += 1
            else:
                losses += 1
        # If venue matches and team id is the home team : 
        if(games_response['games'][i]['schedule']['venue']['id'] == venue_id and games_response['games'][i]['schedule']['homeTeam']['id'] == team_id):
            # If the home team won
            if(games_response['games'][i]['score']['awayScoreTotal'] < games_response['games'][i]['score']['homeScoreTotal']):
                wins += 1
            else:
                losses += 1
    # If the team has never played at that venue, return 50%
    if(wins == 0 and losses == 0):
        return 0.5
    else:
        return wins / (wins + losses)


# TEAM STATS
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

# Helper function : given team stats (all teams), and an index, return an array of floats of all the stats of that team
def append_team_stats(stats):
    team_stats = []
    # Batting stats
    for b in range(len(team_stats_batting)):
        team_stats.append(stats['batting'][team_stats_batting[b]])
    # Pitching stats
    for p in range(len(team_stats_pitching)):
        team_stats.append(stats['pitching'][team_stats_pitching[p]])
    # Fielding stats
    for f in range(len(team_stats_fielding)):
        team_stats.append(stats['fielding'][team_stats_fielding[f]])
    # Standings
    for s in range(len(team_stats_standings)):
        team_stats.append(stats['standings'][team_stats_standings[s]])
    return team_stats


# This function returns the away minus home team stats given a game ID
def collect_team_stats(game_id, season):
    lineup = all_lineups[game_id]
    team_stats = initialize_team_stats(season)
    away_team_id = lineup['game']['awayTeam']['id']
    home_team_id = lineup['game']['homeTeam']['id']
    away_stats = []
    home_stats = []
    # Cycle thru all teams
    for i in range(len(team_stats['teamStatsTotals'])):
        # If we find the away team id matches
        if(away_team_id == team_stats['teamStatsTotals'][i]['team']['id']):
            away_stats = append_team_stats(team_stats['teamStatsTotals'][i]['stats'])
        # If we find the home team id matches
        elif(home_team_id == team_stats['teamStatsTotals'][i]['team']['id']):
            home_stats = append_team_stats(team_stats['teamStatsTotals'][i]['stats'])
    # Create and return away minus home array
    away_minus_home = []
    for i in range(len(away_stats)):
        away_minus_home.append(away_stats[i] - home_stats[i])
    return away_minus_home






# Player stats we collect, 4 categories
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
# We will use the following dictionary and array to help order the positions
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


position_array = ['1B', '2B', '3B', 'BO1', 'BO2', 'BO3', 'BO4', 'BO5', 'BO6', 'BO7', 
'BO8', 'BO9', 'C', 'CF', 'DH', 'LF', 'P', 'RF', 'SS']

# Away = 0, Home = 1
# Takes in a lineup call, returns the player ids for one team in an array in the order above. If player is null or it returns 0
def collect_player_ids(lineup, away, actual_or_expected):
    ids = [0]*19
    for i in range(len(lineup['teamLineups'][away][actual_or_expected]['lineupPositions'])):
        if(lineup['teamLineups'][away][actual_or_expected]['lineupPositions'][i]['player'] is not None and lineup['teamLineups'][away][actual_or_expected]['lineupPositions'][i]['position'] != 'OF'):
            ids[position_dictionary[lineup['teamLineups'][away][actual_or_expected]['lineupPositions'][i]['position']]] = lineup['teamLineups'][away][actual_or_expected]['lineupPositions'][i]['player']['id']
    return ids

# Given a list of player ids, returns a list of 19 dictionaries (0 if null)
# We need away to determine the team of the player in question (one player can play for more than one team in a season)
def collect_dictionaries(lineup, away, player_stats, player_ids):
    dictionary_array = []
    player_team_id = lineup['teamLineups'][away]['team']['id']
    for i in range(len(player_ids)):
        player_found = False
        for j in range(len(player_stats['playerStatsTotals'])):
            if(player_stats['playerStatsTotals'][j]['player']['id'] == player_ids[i] and player_stats['playerStatsTotals'][j]['team']['id'] == player_team_id):
                dictionary_array.append(player_stats['playerStatsTotals'][j]['stats'])
                player_found = True
        if(player_found == False):
            dictionary_array.append(0)
    return dictionary_array

# This function converts the dictionaries to float arrays.
# If the player is null, it fills it with the average for that position and year
# And divides the stats by the number of games played by that specific player
def dictionary_to_float(dictionaries, season):
    float_array = []
    for i in range(len(dictionaries)):
        position = position_array[i]
        if(dictionaries[i] == 0):
            float_array += pickle.load(open('average_' + position + '_' + str(season) + '.pkl', 'rb'))
        else:
            games_played = dictionaries[i]['gamesPlayed']
            if(games_played == 0):
                games_played = 1
            for b in range(len(player_stats_batting)):
                float_array.append(dictionaries[i]['batting'][player_stats_batting[b]] / games_played)
            for f in range(len(player_stats_fielding)):
                float_array.append(dictionaries[i]['fielding'][player_stats_fielding[f]] / games_played)
            for m in range(len(player_stats_miscellaneous)):
                float_array.append(dictionaries[i]['miscellaneous'][player_stats_miscellaneous[m]] / games_played)
            if(position == 'P'):
                if('pitching' in dictionaries[i]):
                    for p in range(len(player_stats_pitching)):
                        float_array.append(dictionaries[i]['pitching'][player_stats_pitching[p]] / games_played)
                else:
                    for p in range(len(player_stats_pitching)):
                        float_array.append(pickle.load(open('average_P_' + str(season) + '.pkl', 'rb'))[len(player_stats_batting) + len(player_stats_fielding) + len(player_stats_miscellaneous) + p])
    return float_array





# PLAYER STATS
# Away = 0, Home = 1
# actual_or_expected is just a string 'actual' or 'expected'
def collect_player_stats(game_id, season, actual_or_expected):
    player_stats = initialize_player_stats(season)
    lineup = all_lineups[game_id]
    away_player_ids = collect_player_ids(lineup, 0, actual_or_expected)
    home_player_ids = collect_player_ids(lineup, 1, actual_or_expected)
    away_dictionaries = collect_dictionaries(lineup, 0, player_stats, away_player_ids)
    home_dictionaries = collect_dictionaries(lineup, 1, player_stats, home_player_ids)
    away_floats = dictionary_to_float(away_dictionaries, season)
    home_floats = dictionary_to_float(home_dictionaries, season)
    away_minus_home = []
    for i in range(len(away_floats)):
        away_minus_home.append(away_floats[i] - home_floats[i])
    return away_minus_home



# collect_player_stats(48847, 2019, 'actual')


def create_training_set():
    training_set = []
    for i in range(len(games_response_2016['games'])):
        print('2016 GAME ', i)
        venue_id = games_response_2016['games'][i]['schedule']['venue']['id']
        away_team_id = games_response_2016['games'][i]['schedule']['awayTeam']['id']
        home_team_id = games_response_2016['games'][i]['schedule']['homeTeam']['id']
        game_id = games_response_2016['games'][i]['schedule']['id']
        win_differential = venue_win(venue_id, away_team_id, 2016) - venue_win(venue_id, home_team_id, 2016)
        team_stats = collect_team_stats(game_id, 2016)
        player_stats = collect_player_stats(game_id, 2016, 'actual')
        training_single_game = []
        training_single_game.append(win_differential)
        training_single_game += team_stats
        training_single_game += player_stats
        training_set.append(training_single_game)
    for i in range(len(games_response_2017['games'])):
        print('2017 GAME ', i)
        venue_id = games_response_2017['games'][i]['schedule']['venue']['id']
        away_team_id = games_response_2017['games'][i]['schedule']['awayTeam']['id']
        home_team_id = games_response_2017['games'][i]['schedule']['homeTeam']['id']
        game_id = games_response_2017['games'][i]['schedule']['id']
        win_differential = venue_win(venue_id, away_team_id, 2017) - venue_win(venue_id, home_team_id, 2017)
        team_stats = collect_team_stats(game_id, 2017)
        player_stats = collect_player_stats(game_id, 2017, 'actual')
        training_single_game = []
        training_single_game.append(win_differential)
        training_single_game += team_stats
        training_single_game += player_stats
        training_set.append(training_single_game)
    for i in range(len(games_response_2018['games'])):
        print('2018 GAME ', i)
        venue_id = games_response_2018['games'][i]['schedule']['venue']['id']
        away_team_id = games_response_2018['games'][i]['schedule']['awayTeam']['id']
        home_team_id = games_response_2018['games'][i]['schedule']['homeTeam']['id']
        game_id = games_response_2018['games'][i]['schedule']['id']
        win_differential = venue_win(venue_id, away_team_id, 2018) - venue_win(venue_id, home_team_id, 2018)
        team_stats = collect_team_stats(game_id, 2018)
        player_stats = collect_player_stats(game_id, 2018, 'actual')
        training_single_game = []
        training_single_game.append(win_differential)
        training_single_game += team_stats
        training_single_game += player_stats
        training_set.append(training_single_game)
    return training_set

def create_test_set():
    test_set = []
    for i in range(len(games_response_2019['games'])):
        print('2019 GAME ', i)
        venue_id = games_response_2019['games'][i]['schedule']['venue']['id']
        away_team_id = games_response_2019['games'][i]['schedule']['awayTeam']['id']
        home_team_id = games_response_2019['games'][i]['schedule']['homeTeam']['id']
        game_id = games_response_2019['games'][i]['schedule']['id']
        win_differential = venue_win(venue_id, away_team_id, 2018) - venue_win(venue_id, home_team_id, 2018)
        team_stats = collect_team_stats(game_id, 2018)
        player_stats = collect_player_stats(game_id, 2018, 'expected')
        test_single_game = []
        test_single_game.append(win_differential)
        test_single_game += team_stats
        test_single_game += player_stats
        test_set.append(test_single_game)
    return test_set

# training_set = create_training_set()
# pickle.dump(training_set, open('training_set.pkl', 'wb'))
training_set = pickle.load(open('training_set.pkl', 'rb'))

training_win_list = win_list_2016 + win_list_2017 + win_list_2018

test_win_list = win_list_2019

# test_set = create_test_set()
# pickle.dump(test_set, open('test_set.pkl', 'wb'))
test_set = pickle.load(open('test_set.pkl', 'rb'))


def get_clean_idx(stats):
    means = np.mean(stats, axis=0)
    variances = np.var(stats, axis=0)
    idx = np.where(variances == 0)[0]
    allidx = np.asarray(range(means.shape[0]))
    cleanidx = np.setdiff1d(allidx, idx)
    return cleanidx

def get_clean_stats(stats, idx):
    return stats[:, idx]

# Convert all four arrays to numpy
training_set_numpy = np.asarray(training_set, dtype=np.float32)
test_set_numpy = np.asarray(test_set, dtype=np.float32)
training_win_list_numpy = np.asarray(training_win_list, dtype=np.float32)
test_win_list_numpy = np.asarray(test_win_list, dtype=np.float32)

clean_idx = get_clean_idx(training_set_numpy)
clean_train_set = get_clean_stats(training_set_numpy, clean_idx)
clean_test_set = get_clean_stats(test_set_numpy, clean_idx)

def normalize(stats, mean, std):
    return (stats - mean / std)

train_mean = np.mean(clean_train_set, axis=0)
train_std = np.std(clean_train_set, axis=0)

norm_train_stats = normalize(clean_train_set, train_mean, train_std)
norm_test_stats = normalize(clean_test_set, train_mean, train_std)


model_logistic = LogisticRegression(penalty='l2', tol=0.05)
# model_logistic = LogisticRegression(penalty='l2')
model_logistic.fit(norm_train_stats, training_win_list_numpy)
score = model_logistic.score(norm_test_stats, test_win_list_numpy)
print('test shape = ', norm_test_stats.shape)
# print('SCORE = ', score)


# Convert to numpy (normalized stats)
# training_set_numpy = np.asarray(norm_train_stats, dtype=np.float32)
# test_set_numpy = np.asarray(norm_test_stats, dtype=np.float32)

# pickle.dump(training_set_numpy, open('training_set.pkl', 'wb'))
# pickle.dump(test_set_numpy, open('test_set.pkl', 'wb'))



# training_set_numpy = pickle.load(open('training_set.pkl', 'rb'))
# test_set_numpy = pickle.load(open('test_set.pkl', 'rb'))



# model_logistic = LogisticRegression(penalty='l2', C=0.1, tol=0.04)
# model_logistic.fit(training_set_numpy, training_win_list_numpy)
# score = model_logistic.score(test_set_numpy, test_win_list_numpy)
# print('on average score = ', score)

'''
C = [0.01, 0.1, 0.50, 0.75, 1.0, 2.0, 3.0, 4.0, 5.0]
# tol = [1e1, 1e0, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5]
tol = [0.05, 0.06, 0.07]
# penalty = ['l1', 'l2']
penalty = ['l2']
# tol = [0.04]
# C = [0.99, 0.1,0.11]
# C = [0.0999, 0.1, 0.1005]
for p in penalty:
    for c in C:
        for t in tol:
            model_logistic = LogisticRegression(penalty=p, C=c, tol=t)
            model_logistic.fit(training_set_numpy, training_win_list_numpy)
            score = model_logistic.score(test_set_numpy, test_win_list_numpy)
            print('penalty = ', p, ' C = ', c, ' tol = ', t, ' on average score = ', score)
'''


# model_logistic = LogisticRegression(penalty='l2', tol=0.585)
# # model_logistic = LogisticRegression(penalty='l2')
# model_logistic.fit(training_set_numpy, training_win_list_numpy)
# score = model_logistic.score(test_set_numpy, test_win_list_numpy)
# # print('penalty = l2 tol = 0.004 on average score = ', score)





def collect_prediction_array(game_id):
    lineup = all_lineups[game_id]
    venue_id = lineup['game']['venue']['id']
    #print(venue_id)
    away_team_id = lineup['game']['awayTeam']['id']
    #print(away_team_id)
    home_team_id = lineup['game']['homeTeam']['id']
    #print(home_team_id)
    game_id = lineup['game']['id']
    #print('GAME ID HERE: ', game_id)
    win_differential = venue_win(venue_id, away_team_id, 2018) - venue_win(venue_id, home_team_id, 2018)
    team_stats = collect_team_stats(game_id, 2018)
    player_stats = collect_player_stats(game_id, 2018, 'expected')
    test_single_game = []
    test_single_game.append(win_differential)
    test_single_game += team_stats
    test_single_game += player_stats
    return test_single_game




# This is the final function. The one that returns a win percentage for any given game
def predict(game_id):
    prediction = collect_prediction_array(game_id)
    del prediction[1494:1504]
    prediction_numpy = np.asarray(prediction, dtype=np.float32)
    norm_prediction = normalize(prediction_numpy, train_mean, train_std)
    #print('PREDICTION SHAPE = ', norm_prediction.shape)
    probability = model_logistic.predict_proba(np.expand_dims(norm_prediction, axis=0))[0]
    print('NOMR PREDICTION', norm_prediction)
    print('Probability', probability)
    return probability
    


#print('training shape = ', norm_train_stats.shape)
print(predict(51248))

# ========================================================================================================================================

'''
api_key = "e0c4e5ec-08d5-414d-88ce-9b392f"
pswrd = "MYSPORTSFEEDS"
seasons = [2016, 2017, 2018, 2019]
def basicAPICall(season, keyword):
    print('basic API call : ', keyword, ' season = ', season)
    try:
        response = requests.get(
            url='https://api.mysportsfeeds.com/v2.1/pull/mlb/' + str(season) + '-regular/' + keyword + '.json',
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format(api_key,pswrd).encode('utf-8')).decode('ascii')
            })
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    return (json.loads(response.content))
def lineupAPICall(season, id):
    print('lineup API call, GAME ID = ', id, ' season = ', season)
    try:
        response = requests.get(
            url='https://api.mysportsfeeds.com/v2.1/pull/mlb/'+ str(season) + '-regular/games/' + str(id) + '/lineup.json',
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
THE FOLLOWING WAS JUST USED TO GET THE PICKLE DATA AND API CALLS, WE NEVER USE THE API AGAIN FROM NOW 
for i in range(len(seasons)):
    # GAMES RESPONSE
    if os.path.exists('games_response_' + str(seasons[i]) + '.pkl'):
        games_call_response = pickle.load(open('games_response_' + str(seasons[i]) + '.pkl', 'rb'))
    else:
        games_call_response = basicAPICall(seasons[i], 'games')
        pickle.dump( games_call_response, open('games_response_' + str(seasons[i]) + '.pkl', 'wb' ) )
    # Collect all game ids
    game_ids = []
    for j in range(len(games_call_response['games'])):
        game_ids.append(games_call_response['games'][j]['schedule']['id'])
    if os.path.exists('game_ids_' + str(seasons[i]) + '.pkl'):
        game_ids = pickle.load(open('game_ids_' + str(seasons[i]) + '.pkl', 'rb'))
    else:
        pickle.dump(game_ids, open('game_ids_' + str(seasons[i]) + '.pkl', 'wb'))
    # PLAYER STATS RESPONSE
    if os.path.exists('player_stats_' + str(seasons[i]) + '.pkl'):
        player_stats_totals_response = pickle.load(open('player_stats_' + str(seasons[i]) + '.pkl', 'rb'))
    else:
        player_stats_totals_response = basicAPICall(seasons[i], 'player_stats_totals')
        pickle.dump( player_stats_totals_response, open('player_stats_' + str(seasons[i]) + '.pkl', 'wb'))
    # TEAM STATS RESPONSE
    if os.path.exists('team_stats_' + str(seasons[i]) + '.pkl'):
        team_stats_totals_response = pickle.load(open('team_stats_' + str(seasons[i]) + '.pkl', 'rb'))
    else:
        team_stats_totals_response = basicAPICall(seasons[i], 'team_stats_totals')
        pickle.dump( team_stats_totals_response, open('team_stats_' + str(seasons[i]) + '.pkl', 'wb'))
    # LINEUPS RESPONSE
    if os.path.exists('lineup_responses_' + str(seasons[i]) + '.pkl'):
        lineup_call_responses = pickle.load(open('lineup_responses_' + str(seasons[i]) + '.pkl', 'rb'))
    else:
        lineup_call_responses = dict()
        for j in range(len(game_ids)):
            print('GAME ', j, ' season : ', seasons[i])
            lineup_call_response = lineupAPICall(seasons[i], game_ids[j])
            lineup_call_responses[game_ids[j]] = lineup_call_response
        pickle.dump(lineup_call_responses, open('lineup_responses_' + str(seasons[i]) + '.pkl', 'wb' ))
def create_win_list(season):
    win_list = []
    games_response = initialize_games_call_response(season)
    for i in range(len(games_response['games'])):
        if(games_response['games'][i]['score']['awayScoreTotal'] > games_response['games'][i]['score']['homeScoreTotal']):
            win_list.append(1)
        else:
            win_list.append(0)
    return win_list
for i in range(len(seasons)):
    win_list = create_win_list(seasons[i])
    pickle.dump(win_list, open( 'win_list_' + str(seasons[i]) + '.pkl', 'wb'))
'''