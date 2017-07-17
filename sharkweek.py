import json
import sqlite3
from TwitterAPI import TwitterAPI

# Takes in oAuth keys from config.json and returns n tweets containing hash as an API response.
def get_tweets(hash, n):

    # Retrieve keys from config file
    with open('config.json') as json_data_file:
        creds = json.load(json_data_file)
    key = creds['Consumer Key']
    secret = creds['Consumer Secret']

    # Get tweets from Twitter
    api = TwitterAPI(key, secret, auth_type='oAuth2')
    r = api.request('search/tweets', {'q': hash, 'count': n})
    return r

# Connects to db_file and returns connected variable.
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

# Creates cursor object from connection object.
def create_cursor(connect):
    try:
        c = connect.cursor()
        return c;
    except sqlite3.Error as e:
        print(e)
    return None

# Closes the connection object.
def close_conn(connect):
    connect.commit()
    connect.close()
    return None

def update_database(response, meta, connect, table):
    for tweet in response.get_iterator():

def fill_database(connect, table, count):
    # Create the placeholders for each column
    if count <= 0:
        return None
    col_string = ""
    if count < 1:
        for i in range(count - 1):
            col_string+= "?,"
    col_string += "?"

    # Add metadata to db
    try:
        c.execute("INSERT into {} VALUES({})".format(table, col_string),
                  [id, user, screen_name, text])
    except sqlite3.Error as e:
        print(e)

# Get tweets
count = 10;
results = get_tweets('#sharkweek', count)

# Connect to db
my_db = "sharkweek.db"
conn = create_connection(my_db)
c = create_cursor(conn)

# Retrieve metadata for each tweet and add to db
for item in results.get_iterator():
    print(item['user']['screen_name'], item['text'], item['id'])
    id = item['id']
    user = item['user']['name']
    screen_name = item['user']['screen_name']
    text = item['text']

    # Add metadata to db
    try:
        c.execute("INSERT into twitter VALUES(?,?,?,?)",
                  ([id, user, screen_name, text]))
    except sqlite3.Error as e:
        print(e)

# Save the changes
close_conn(conn)

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

# Dump tweets to .json file
# r = results.json()
# print(type(r))
# print(type((r,)))
# with open('tweets.json', 'w') as outfile:
#       json.dump(r, outfile)

# Print types and data entries to find fields for SQLite debugging
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


