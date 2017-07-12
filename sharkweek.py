import json
import sqlite3
from TwitterAPI import TwitterAPI

# Function opens config.json containing Twitter oAuth keys and returns list with oAuth keys as strings.
def get_creds():
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
    return data

# Takes in oAuth keys and returns tweets containing #sharkweek as .json.
def get_tweets(consumer_key, consumer_secret):
    api = TwitterAPI(consumer_key, consumer_secret, auth_type='oAuth2')
    r = api.request('search/tweets', {'q': '#sharkweek'})
    return r

# Connects to db_file and returns connected variable.
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

# Get tweets and store in results
creds = get_creds()
key = creds['Consumer Key']
secret = creds['Consumer Secret']

results = get_tweets(key, secret)

# Print tweets for viewing
print(type(results.json()))
for item in results.get_iterator():
    print(item) #['user']['screen_name'], item['text'], item['id'])

with open('tweets.json', 'w') as outfile:
    json.dump(results.json(), outfile)
# Connect to db
# my_db = "sharkweek.db"
# conn = create_connection(my_db)
# try:
#     c = conn.cursor()
#     c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')")
# except sqlite3.Error as e:
#     print(e)
# finally:
#     conn.close()


