import base64
import json
import requests
import csv
import pandas as pd
import numpy as np
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
        f = open(keyword + season + '.csv', "w", encoding='utf-8')
        f.write(response.text)
        f.close()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    return (response.content)




# basicAPICall('2016', 'games')




def choose_team(A, season):
    df = pd.read_csv('teamStats' + season + '.csv', index_col='#Team ID')
    A_stats = df.loc[A].rename_axis('#Team ID').values
    return A_stats



headers = ['#GamesPlayed','#AtBats','#Runs','#Hits','#SecondBaseHits','#ThirdBaseHits','#Homeruns','#UnearnedRuns','#RunsBattedIn','#EarnedRuns','#BatterWalks','#BatterSwings','#BatterStrikes','#BatterStrikesFoul','#BatterStrikesMiss','#BatterStrikesLooking','#BatterGroundBalls','#BatterFlyBalls','#BatterLineDrives','#LeftOnBase','#BatterStrikeouts','#BatterSplitters','#BatterCutters','#Batter4SeamFastballs','#BatterSinkers','#BatterChangeups','#Batter2SeamFastballs','#OpponentsLeftOnBase','#BatterSliders','#BatterCurveballs','#StolenBases','#CaughtBaseSteals','#BatterStolenBasePct','#BattingAvg','#BatterOnBasePct','#BatterSluggingPct','#BatterOnBasePlusSluggingPct','#BatterIntentionalWalks','#HitByPitch','#BatterSacrificeBunts','#BatterSacrificeFlies','#TotalBases','#ExtraBaseHits','#BatterDoublePlays','#BatterTriplePlays','#BatterTagOuts','#BatterForceOuts','#BatterPutOuts','#BatterGroundOuts','#BatterFlyOuts','#BatterGroundOutToFlyOutRatio','#PitchesFaced','#PlateAppearances','#OpponentAtBats','#EarnedRunAvg','#InningsPitched','#HitsAllowed','#SecondBaseHitsAllowed','#ThirdBaseHitsAllowed','#RunsAllowed','#EarnedRunsAllowed','#HomerunsAllowed','#PitcherWalks','#PitcherSwings','#PitcherStrikes','#PitcherStrikesFoul','#PitcherStrikesMiss','#PitcherStrikesLooking','#PitcherGroundBalls','#PitcherFlyBalls','#PitcherLineDrives','#Pitcher4SeamFastballs','#PitcherSinkers','#PitcherChangeups','#Pitcher2SeamFastballs','#PitcherSliders','#PitcherSacrificeBunts','#PitcherCurveballs','#PitcherSplitters','#PitcherCutters','#PitcherSacrificeFlies','#PitcherStrikeouts','#PitchingAvg','#WalksAndHitsPerInningPitched','#Shutouts','#BattersHit','#PitcherIntentionalWalks','#PitcherGroundOuts','#PitcherFlyOuts','#PitcherWildPitches','#Balks','#PitcherStolenBasesAllowed','#PitcherCaughtStealing','#PickoffAttempts','#Pickoffs','#TotalBattersFaced','#PitchesThrown','#PitcherGroundOutToFlyOutRatio','#PitcherOnBasePct','#PitcherSluggingPct','#PitcherOnBasePlusSluggingPct','#StrikeoutsPer9Innings','#WalksAllowedPer9Innings','#HitsAllowedPer9Innings','#StrikeoutsToWalksRatio','#PitchesPerInning','#InningsPlayed','#TotalChances','#FielderForceOuts','#FielderTagOuts','#FielderPutOuts','#Assists','#Errors','#FielderDoublePlays','#FielderTriplePlays','#FielderStolenBasesAllowed','#FielderCaughtStealing','#FielderStolenBasePct','#PassedBalls','#FielderWildPitches','#FieldingPct','#DefenceEfficiencyRatio','#OutsFaced','#Wins','#Losses','#WinPct','#GamesBack','#RunsFor','#RunsAgainst','#RunDifferential']

def normalize(teamStats, season):
    data = pd.read_csv('TeamStats' + season + '.csv')
    means = []
    stdevs = []
    normal = []
    for i in range(len(headers)):
        means.append(data[headers[i]].mean())
        stdevs.append(data[headers[i]].std())
    for j in range(len(headers)):
        normal.append( (teamStats[j+4] - means[j]) / stdevs[j])
    return normal


def subtractArrays(home, away):
    delta = []
    for i in range(len(home)):
        delta.append(home[i]-away[i])
    return delta


# def createWinList(season):


subtractArrays( normalize(choose_team(125, '2018'), '2018'),normalize(choose_team(136, '2018'), '2018'))
