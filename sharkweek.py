import json

from TwitterAPI import TwitterAPI


def get_creds():
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
    return data


def get_tweets(consumer_key, consumer_secret):
    api = TwitterAPI(consumer_key, consumer_secret, auth_type='oAuth2')
    r = api.request('search/tweets', {'q': '#sharkweek'})
    return r

creds = get_creds()
key = creds['Consumer Key']
secret = creds['Consumer Secret']

results = get_tweets(key, secret)

for item in results.get_iterator():
    print(item['user']['screen_name'], item['text'])


