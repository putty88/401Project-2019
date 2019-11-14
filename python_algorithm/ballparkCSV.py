import base64
import json
import requests
import csv
import pandas as pd
import numpy as np
import pickle
import os
from sklearn.linear_model import LogisticRegression

api_key = "e0c4e5ec-08d5-414d-88ce-9b392f"
pswrd = "MYSPORTSFEEDS"

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
        # f = open(keyword + season + '.csv', "w", encoding='utf-8')
        # f.write(response.text)
        # f.close()
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

def sanitize(stats):
    means = np.mean(stats, axis=0)
    variances = (np.var(stats, axis=0))
    idx = np.where(variances == 0)[0]
    allidx = np.asarray(range(means.shape[0]))
    cleanidx = np.setdiff1d(allidx, idx)
    return np.float32(stats[:, cleanidx])

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
    # for i in range(10):
        if(game['score']['homeScoreTotal'] > game['score']['awayScoreTotal']):
            winList.append((1, game['schedule']['homeTeam']['id'], game['schedule']['awayTeam']['id']))
        else:
            winList.append((-1, game['schedule']['homeTeam']['id'], game['schedule']['awayTeam']['id']))
    return winList

fileName = 'results.pkl'
if(os.path.exists(fileName)):
    with open(fileName, 'rb') as f:
        winList2018 = pickle.load(f)
else:
    winList2018 = createWinList('2018')
    with open(fileName, 'wb') as f:
        pickle.dump(winList2018, f)

# pickle.dump(winList2018, )
# print(winList2018)

teams = set()

for i in range(len(winList2018)):
    _, homeID, awayID = winList2018[i]
    teams.add(homeID)
    teams.add(awayID)


teams = list(teams)
teams.sort()

# print(teams)

seasons = ['2016', '2017', '2018', '2019']

stats = collect_stats(teams, seasons)[:, 4:]

stats = sanitize(stats)

normalized_stats = normalize(stats)

# print(normalized_stats.shape)

X = []
Y = []
for i in range(len(winList2018)):
    result, homeID, awayID = winList2018[i]
    homeIndex = teams.index(homeID)
    awayIndex = teams.index(awayID)
    homeStats = normalized_stats[2*30+homeIndex, :]
    awayStats = normalized_stats[2*30+awayIndex, :]
    delta = homeStats - awayStats
    X.append(delta)
    Y.append(result)
X = np.asarray(X)
Y = np.asarray(Y)

# print(X.shape)
# print(Y.shape)


model_logistic = LogisticRegression()
model_logistic.fit(X, Y)
model_logistic.score(X, Y)

score = model_logistic.score(X,Y)
print(score)

# print(stddevs)

# print(choose_team(130, '2018'))

# def normalize(teamStats, season):
#     data = pd.read_csv('TeamStats' + season + '.csv')
#     means = []
#     stdevs = []
#     normal = []
#     for i in range(len(headers)):   
#         means.append(data[headers[i]].mean())
#         stdevs.append(data[headers[i]].std())
#     for j in range(len(headers)):
#         normal.append( (teamStats[j+4] - means[j]) / stdevs[j])
#     return normal


def subtractArrays(home, away):
    delta = []
    for i in range(len(home)):
        delta.append(home[i]-away[i])
    return delta

# games2019 = basicAPICall('2019', 'games', 'json')
# games2018 = basicAPICall('2018', 'games', 'json')
# games2017 = basicAPICall('2017', 'games', 'json')
# games2016 = basicAPICall('2016', 'games', 'json')


def createDeltaList(season):
    deltaList = []
    seasonJson = createJsonObject(season)
    for i in range(len(basicAPICall(season, 'games', 'json')['games'])):
    # for i in range(100):
        deltaList.append(subtractArrays(normalize(choose_team(seasonJson['games'][i]['schedule']['awayTeam']['id'], season), season), normalize(choose_team(seasonJson['games'][i]['schedule']['homeTeam']['id'], season), season)))
    print(deltaList)
    return deltaList


# createDeltaList('2019')

# print(basicAPICall('2016', 'games', 'json')['games'][0]['score']['homeScoreTotal'])

# subtractArrays( normalize(choose_team(125, '2018'), '2018'),normalize(choose_team(136, '2018'), '2018'))
