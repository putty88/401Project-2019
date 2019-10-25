import base64
import requests
import json
#from ohmysportsfeedspy import MySportsFeeds
#msf = MySportsFeeds(version="2.0")
api_key = "e0c4e5ec-08d5-414d-88ce-9b392f"
pswrd = "MYSPORTSFEEDS"
#msf.authenticate(api_key, pswrd)
#output = msf.msf_get_data(league='mlb',season='latest',feed='team_stats_totals',format='json')
#print(output)
#print("aids")
def send_request():
   # Request
   try:
       response = requests.get(
           url="https://api.mysportsfeeds.com/v2.1/pull/mlb/latest/games.json",
           params={
               "fordate": "20161121"
           },
           headers={
               "Authorization": "Basic " + base64.b64encode('{}:{}'.format(api_key,pswrd).encode('utf-8')).decode('ascii')
           }
       )
       print('Response HTTP Status Code: {status_code}'.format(
           status_code=response.status_code))
       print('Response HTTP Response Body: {content}'.format(
           content=response.content))
   except requests.exceptions.RequestException:
       print('HTTP Request failed')

# send_request()




def getData(teamA, teamB, keyword, season):
    pull_url = 'https://api.mysportsfeeds.com/v2.1/pull/mlb/' + season + '-regular/games.json'
    try:
       response = requests.get(
           url=pull_url,
           params={
               "fordate": "20161121"
           },
           headers={
               "Authorization": "Basic " + base64.b64encode('{}:{}'.format(api_key,pswrd).encode('utf-8')).decode('ascii')
           }
       )
    #    print('Response HTTP Status Code: {status_code}'.format(
    #        status_code=response.status_code))
    #    print('Response HTTP Response Body: {content}'.format(content=response.content))
       datastore = json.loads(response.content)
    except requests.exceptions.RequestException:
       print('HTTP Request failed')
    return(datastore)


print(len(getData('','', 'games', '2019')['games']))

for i in range(len(getData('','', 'games', '2019')['games'])):
    if(getData('','', 'games', '2019')['games'][i]['schedule']['homeTeam']['id'] == 125):
        print(getData('', '', 'games', '2019')['games'][i]['score'])
    print('')

print(getData('Astros', 'Dodgers', 'games', '2019')['games'][0]['score'])

# print(type(json.loads(getData('Astros', 'Dodgers', 'games', '2019'))))