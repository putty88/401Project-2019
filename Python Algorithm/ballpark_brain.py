# Install the Python Requests library:
# `pip install requests`

import base64
import requests

season = '2018-2019-regular'
apikey_token = 'e0c4e5ec-08d5-414d-88ce-9b392f'
# apikey_token = 'Xx_thomas_xX'
password = 'ilikevike'
# MYSPORTSFEED = 0
for_date = '20150606'
# pull_url = 'https://api.mysportsfeeds.com/v1.0/pull/mlb/current_season.json?fordate=' + for_date
pull_url = 'https://api.mysportsfeeds.com/v1.2/pull/mlb/2015-2016-regular/cumulative_player_stats.json'

# pull_url = 'https://api.mysportsfeeds.com/v1.0/pull/mlb/2015-2016-regular/daily_player_stats.json?fordate=' + for_date


def send_request():
    # Request

    try:
        response = requests.get(
            url=pull_url,
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format(apikey_token,password).encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


send_request()