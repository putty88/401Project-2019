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
        f = open(keyword+'.csv', "w", encoding='utf-8')
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


headers = ['#GamesPlayed','#AtBats','#Runs','#Hits','#SecondBaseHits','#ThirdBaseHits','#Homeruns','#UnearnedRuns','#RunsBattedIn','#EarnedRuns','#BatterWalks','#BatterSwings','#BatterStrikes','#BatterStrikesFoul','#BatterStrikesMiss','#BatterStrikesLooking','#BatterGroundBalls','#BatterFlyBalls','#BatterLineDrives','#LeftOnBase','#BatterStrikeouts','#BatterSplitters','#BatterCutters','#Batter4SeamFastballs','#BatterSinkers','#BatterChangeups','#Batter2SeamFastballs','#OpponentsLeftOnBase','#BatterSliders','#BatterCurveballs','#StolenBases','#CaughtBaseSteals','#BatterStolenBasePct','#BattingAvg','#BatterOnBasePct','#BatterSluggingPct','#BatterOnBasePlusSluggingPct','#BatterIntentionalWalks','#HitByPitch','#BatterSacrificeBunts','#BatterSacrificeFlies','#TotalBases','#ExtraBaseHits','#BatterDoublePlays','#BatterTriplePlays','#BatterTagOuts','#BatterForceOuts','#BatterPutOuts','#BatterGroundOuts','#BatterFlyOuts','#BatterGroundOutToFlyOutRatio','#PitchesFaced','#PlateAppearances','#OpponentAtBats','#EarnedRunAvg','#InningsPitched','#HitsAllowed','#SecondBaseHitsAllowed','#ThirdBaseHitsAllowed','#RunsAllowed','#EarnedRunsAllowed','#HomerunsAllowed','#PitcherWalks','#PitcherSwings','#PitcherStrikes','#PitcherStrikesFoul','#PitcherStrikesMiss','#PitcherStrikesLooking','#PitcherGroundBalls','#PitcherFlyBalls','#PitcherLineDrives','#Pitcher4SeamFastballs','#PitcherSinkers','#PitcherChangeups','#Pitcher2SeamFastballs','#PitcherSliders','#PitcherSacrificeBunts','#PitcherCurveballs','#PitcherSplitters','#PitcherCutters','#PitcherSacrificeFlies','#PitcherStrikeouts','#PitchingAvg','#WalksAndHitsPerInningPitched','#Shutouts','#BattersHit','#PitcherIntentionalWalks','#PitcherGroundOuts','#PitcherFlyOuts','#PitcherWildPitches','#Balks','#PitcherStolenBasesAllowed','#PitcherCaughtStealing','#PickoffAttempts','#Pickoffs','#TotalBattersFaced','#PitchesThrown','#PitcherGroundOutToFlyOutRatio','#PitcherOnBasePct','#PitcherSluggingPct','#PitcherOnBasePlusSluggingPct','#StrikeoutsPer9Innings','#WalksAllowedPer9Innings','#HitsAllowedPer9Innings','#StrikeoutsToWalksRatio','#PitchesPerInning','#InningsPlayed','#TotalChances','#FielderForceOuts','#FielderTagOuts','#FielderPutOuts','#Assists','#Errors','#FielderDoublePlays','#FielderTriplePlays','#FielderStolenBasesAllowed','#FielderCaughtStealing','#FielderStolenBasePct','#PassedBalls','#FielderWildPitches','#FieldingPct','#DefenceEfficiencyRatio','#OutsFaced','#Wins','#Losses','#WinPct','#GamesBack','#RunsFor','#RunsAgainst','#RunDifferential']

def normie(season):
    data = pd.read_csv('TeamStats' + season + '.csv')
    # data[headers[]].mean()

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
