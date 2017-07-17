import json
import sqlite3
from TwitterAPI import TwitterAPI

# Function opens config.json containing Twitter oAuth keys and returns list with oAuth keys as strings.
def get_creds():
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
    return data

# Takes in oAuth keys and returns tweets containing #sharkweek as .json.
def get_tweets(hash, count):
    creds = get_creds()
    key = creds['Consumer Key']
    secret = creds['Consumer Secret']
    api = TwitterAPI(key, secret, auth_type='oAuth2')
    r = api.request('search/tweets', {'q': hash, 'count': count})
    return r

# Connects to db_file and returns connected variable.
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def create_cursor(connect):
    try:
        c = connect.cursor()
        return c;
    except sqlite3.Error as e:
        print(e)
    return None

#def auth():

# Authenticate to Twitter
results = get_tweets('#sharkweek', 100)

# r = results.json()
# print(type(r))
# print(type((r,)))

# Connect to db
my_db = "sharkweek.db"
conn = create_connection(my_db)
c = create_cursor(conn)

# Retrieve metadata for each tweet and add to db
for item in results.get_iterator():
    print(item['user']['screen_name'], item['text'], item['id'])
    # id = item['id']
    # user = item['user']['name']
    # screen_name = item['user']['screen_name']
    # text = item['text']
    # id_str = item['id_str']
    # retweeted = item['retweeted']
    # retweet_count = item['retweet_count']
    # favorited = item['favorited']
    # favorite_count = item['favorite_count']
    # if 'possibly_sensitive' in item:
    #     possibly_sensitive = item['possibly_sensitive']
    # else:
    #     possibly_sensitive = ''
    # lang = item['lang']
    # source = item['source']
    # created_at = item['created_at']
    #
    # # Add metadata to db
    # try:
    #     c.execute("INSERT into twitter VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
    #               [id, user, screen_name, text, id_str, retweeted, retweet_count, favorited,
    #                favorite_count, possibly_sensitive, lang, source, created_at])
    # except sqlite3.Error as e:
    #     print(e)

# Savve the changes
conn.commit()
conn.close()

# Connect to db
# my_db = "sharkweek.db"
# conn = create_connection(my_db)
#
# try:
#     c = conn.cursor()
#     c.execute("INSERT into twitter VALUES(?,?,?,?)", ['','','',r])
# except sqlite3.Error as e:
#     print(e)
# finally:
#     conn.commit()
#     conn.close()

#c.execute("INSERT into twitter VALUES(?,?,?,?)", ['','','',r])

# with open('tweets.json', 'w') as outfile:
#       json.dump(r, outfile)

# Print types and data entries to find fields for SQLite
# print(results.json())
# print(r.keys())
# rLay1 = r['statuses']
# rMeta = r['search_metadata']
# rLay2 = rLay1[-1]
# rLay3 = rLay2['user']
# rLay4 = rLay3['screen_name']
# print("Layer 1 is type:", type(rLay1))
# print("Layer 2 entries in Layer 1:", rLay1[0:-1])
# print("Layer 2 is type:", type(rLay2))
# print("Layer 3 entries in Layer 2:", rLay2.keys())
# print("Layer 3 is type:", type(rLay3))
# print("Layer 4 entries in Layer 3:", rLay3.keys())
# print("Layer 4 is type: ", type(rLay4))
# print("Layer 4 is the end layer")
# print("Metadata is type:", type(rMeta))
# print("Keys in Metadata:", rMeta.keys())


