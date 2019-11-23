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

headers = ['#GamesPlayed','#AtBats','#Runs','#Hits','#SecondBaseHits','#ThirdBaseHits','#Homeruns',
'#UnearnedRuns','#RunsBattedIn','#EarnedRuns','#BatterWalks','#BatterSwings','#BatterStrikes',
'#BatterStrikesFoul','#BatterStrikesMiss','#BatterStrikesLooking','#BatterGroundBalls',
'#BatterFlyBalls','#BatterLineDrives','#LeftOnBase','#BatterStrikeouts','#BatterSplitters',
'#BatterCutters','#Batter4SeamFastballs','#BatterSinkers','#BatterChangeups','#Batter2SeamFastballs',
'#OpponentsLeftOnBase','#BatterSliders','#BatterCurveballs','#StolenBases','#CaughtBaseSteals',
'#BatterStolenBasePct','#BattingAvg','#BatterOnBasePct','#BatterSluggingPct',
'#BatterOnBasePlusSluggingPct','#BatterIntentionalWalks','#HitByPitch','#BatterSacrificeBunts',
'#BatterSacrificeFlies','#TotalBases','#ExtraBaseHits','#BatterDoublePlays','#BatterTriplePlays',
'#BatterTagOuts','#BatterForceOuts','#BatterPutOuts','#BatterGroundOuts','#BatterFlyOuts',
'#BatterGroundOutToFlyOutRatio','#PitchesFaced','#PlateAppearances','#OpponentAtBats','#EarnedRunAvg',
'#InningsPitched','#HitsAllowed','#SecondBaseHitsAllowed','#ThirdBaseHitsAllowed','#RunsAllowed',
'#EarnedRunsAllowed','#HomerunsAllowed','#PitcherWalks','#PitcherSwings','#PitcherStrikes',
'#PitcherStrikesFoul','#PitcherStrikesMiss','#PitcherStrikesLooking','#PitcherGroundBalls',
'#PitcherFlyBalls','#PitcherLineDrives','#Pitcher4SeamFastballs','#PitcherSinkers','#PitcherChangeups',
'#Pitcher2SeamFastballs','#PitcherSliders','#PitcherSacrificeBunts','#PitcherCurveballs',
'#PitcherSplitters','#PitcherCutters','#PitcherSacrificeFlies','#PitcherStrikeouts','#PitchingAvg',
'#WalksAndHitsPerInningPitched','#Shutouts','#BattersHit','#PitcherIntentionalWalks',
'#PitcherGroundOuts','#PitcherFlyOuts','#PitcherWildPitches','#Balks','#PitcherStolenBasesAllowed',
'#PitcherCaughtStealing','#PickoffAttempts','#Pickoffs','#TotalBattersFaced','#PitchesThrown',
'#PitcherGroundOutToFlyOutRatio','#PitcherOnBasePct','#PitcherSluggingPct',
'#PitcherOnBasePlusSluggingPct','#StrikeoutsPer9Innings','#WalksAllowedPer9Innings',
'#HitsAllowedPer9Innings','#StrikeoutsToWalksRatio','#PitchesPerInning','#InningsPlayed',
'#TotalChances','#FielderForceOuts','#FielderTagOuts','#FielderPutOuts','#Assists','#Errors',
'#FielderDoublePlays','#FielderTriplePlays','#FielderStolenBasesAllowed','#FielderCaughtStealing',
'#FielderStolenBasePct','#PassedBalls','#FielderWildPitches','#FieldingPct','#DefenceEfficiencyRatio',
'#OutsFaced','#Wins','#Losses','#WinPct','#GamesBack','#RunsFor','#RunsAgainst','#RunDifferential']

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
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    if(format == 'json'):
        return (json.loads(response.content))
    else:
        return (response.content)


# Returns team stats for a given season
def choose_team(A, season):
    df = pd.read_csv('teamStats' + season + '.csv', index_col='#Team ID')
    A_stats = df.loc[A].rename_axis('#Team ID').values
    return A_stats

def collect_stats(teams, seasons):
    stats = []
    for i in range(len(seasons)):
        for j in range(len(teams)):
            stats.append(choose_team(teams[j], seasons[i]))
    return np.asarray(stats)

# Just removes constant variables that are useless
def sanitize(stats):
    means = np.mean(stats, axis=0)
    variances = (np.var(stats, axis=0))
    idx = np.where(variances == 0)[0]
    allidx = np.asarray(range(means.shape[0]))
    cleanidx = np.setdiff1d(allidx, idx)
    return np.float32(stats[:, cleanidx])

# To normal form
def normalize(stats):
    return (stats - np.mean(stats, axis=0) / np.std(stats, axis=0))


def createJsonObject(season):
    result = basicAPICall(season, 'games', 'json')
    return result

def createWinList(season):
    winList = []
    seasonJson = createJsonObject(season)
    for i in range(len(basicAPICall(season, 'games', 'json')['games'])):
        game = seasonJson['games'][i]
        if(game['score']['homeScoreTotal'] > game['score']['awayScoreTotal']):
            winList.append((1, game['schedule']['homeTeam']['id'], game['schedule']['awayTeam']['id']))
        else:
            winList.append((-1, game['schedule']['homeTeam']['id'], game['schedule']['awayTeam']['id']))
    return winList

def loadWinList(season):   
    fileName = 'results' + season + '.pkl'
    if(os.path.exists(fileName)):
        with open(fileName, 'rb') as f:
            winList = pickle.load(f)
    else:
        winList = createWinList(season)
        with open(fileName, 'wb') as f:
            pickle.dump(winList, f)
    return winList

# winList2018 BECOMES loadWinList('2018)

winList2016 = loadWinList('2016')
winList2017 = loadWinList('2017')
winList2018 = loadWinList('2018')
winList2019 = loadWinList('2019')

# Collects team IDs in a set. Kinda useless but whatever.
teams = set()
for i in range(len(winList2018)):
    _, homeID, awayID = winList2018[i]
    teams.add(homeID)
    teams.add(awayID)
teams = list(teams)
teams.sort()



collectYear = 2018
testList = winList2019

# does not collect the first 4 stats cuz they are not numbers
stats = collect_stats(teams, seasons)[:, 4:]
# cleans up the data and removes the constant ones
stats = sanitize(stats)
# To normal form
normalized_stats = normalize(stats)

# print(normalized_stats.shape)

X_train = []
Y_train = []
# Loops through each game of a season (2340 games)
# THIS IS WHERE YOU PUT THE YEAR YOU TEST
for i in range(len(winList2016)):
    # result = 1 or -1, homeID = ID of home team, same for away
    result, homeID, awayID = winList2016[i]
    # get the index of home and way team in teams list
    homeIndex = teams.index(homeID)
    awayIndex = teams.index(awayID)
    # The reason we say 2*30 + index is : 2018 = 2016 + 2. 
    # We skip the first two years! Not sure with the , : notation
    # THIS IS THE BEFORE (data collection)
    increment = 0
    homeStats = normalized_stats[increment*len(teams)+homeIndex, :]
    awayStats = normalized_stats[increment*len(teams)+awayIndex, :]
    delta = homeStats - awayStats
    X_train.append(delta)
    # PREDICTION
    Y_train.append(result)
for i in range(len(winList2017)):
    result, homeID, awayID = winList2017[i]
    homeIndex = teams.index(homeID)
    awayIndex = teams.index(awayID)
    increment = 1
    homeStats = normalized_stats[increment*len(teams)+homeIndex, :]
    awayStats = normalized_stats[increment*len(teams)+awayIndex, :]
    delta = homeStats - awayStats
    X_train.append(delta)
    Y_train.append(result)
for i in range(len(winList2018)):
    result, homeID, awayID = winList2018[i]
    homeIndex = teams.index(homeID)
    awayIndex = teams.index(awayID)
    increment = 2
    homeStats = normalized_stats[increment*len(teams)+homeIndex, :]
    awayStats = normalized_stats[increment*len(teams)+awayIndex, :]
    delta = homeStats - awayStats
    X_train.append(delta)
    Y_train.append(result)

X_train = np.asarray(X_train)
Y_train = np.asarray(Y_train)


X_test = []
Y_test = []
for i in range(len(winList2019)):
    result, homeID, awayID = winList2019[i]
    homeIndex = teams.index(homeID)
    awayIndex = teams.index(awayID)
    increment = 3
    homeStats = normalized_stats[increment*len(teams)+homeIndex, :]
    awayStats = normalized_stats[increment*len(teams)+awayIndex, :]
    delta = homeStats - awayStats
    X_test.append(delta)
    Y_test.append(result)

X_test = np.asarray(X_test)
Y_test = np.asarray(Y_test)

'''
penalty = ['l1', 'l2']
C = [0.01, 0.1, 0.50, 0.75, 1.0, 2.0, 3.0, 4.0, 5.0]
tol = [1e1, 1e0, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5]
for p in penalty:
    for c in C:
        for t in tol:
            model_logistic = LogisticRegression(penalty=p, C=c, tol=t)
            model_logistic.fit(X_train, Y_train)
            score = model_logistic.score(X_test, Y_test)

            print('penalty={}  C={} tol={} : score={}'.format(p, c, t, score))
'''

p ='l1'  
c = 2.0 
t = 0.01 
model_logistic = LogisticRegression(penalty=p, C=c, tol=t)
model_logistic.fit(X_train, Y_train)
score = model_logistic.score(X_test, Y_test)

# print('On average, your algorithm succeeds at a rate of : ', score)

import random 
# team_idx = np.asarray([random.randint(0, 29) for i in range(2)])
team_increment = 111
homeID = 128
awayID = 137
team_idx = np.asarray([homeID - team_increment, awayID - team_increment])
# year_idx = np.asarray([random.randint(0, 3) for i in range(1)])
# team_ids = np.asarray(teams)[team_idx]
# team_ids = [113,136]
# year_id = np.asarray(seasons)[year_idx]
year_map = { '2016' : 0, '2017' : 1, '2018' : 2, '2019' : 3}
# increment = year_map[str(year_id[0])]
increment = 3
print((2016+increment), [homeID, awayID])

# home_team = normalized_stats[increment*len(teams)+team_idx[0]]
# away_team = normalized_stats[increment*len(teams)+team_idx[1]]
# x = home_team-away_team
# prob = model_logistic.predict_proba(np.expand_dims(x, axis=0))
# print(model_logistic.classes_)
# print(prob)




def createPredictions():
    increment = 3
    number_of_teams = 30
    result = [[0]*30]*30
    for h in range(number_of_teams):
        for a in range(number_of_teams):
            home_team = normalized_stats[increment*number_of_teams+h]
            away_team = normalized_stats[increment*number_of_teams+a]
            x = home_team - away_team
            result[h][a] = model_logistic.predict_proba(np.expand_dims(x, axis=0))
    return result


print(createPredictions())