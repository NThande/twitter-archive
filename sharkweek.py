import json
import sqlite3
import variables
from TwitterAPI import TwitterAPI
import twitterSQLite

# # Takes in oAuth keys from config.json and returns n tweets containing hash as an API response.
# def get_tweets(hash, n):
#
#     # Retrieve keys from config file
#     with open('config.json') as json_data_file:
#         creds = json.load(json_data_file)
#     key = creds['Consumer Key']
#     secret = creds['Consumer Secret']
#
#     # Get tweets from Twitter
#     api = TwitterAPI(key, secret, auth_type='oAuth2')
#     r = api.request('search/tweets', {'q': hash, 'count': n})
#     return r

# # Connects to db_file and returns connected variable.
# def create_connection(db_file):
#     try:
#         conn = sqlite3.connect(db_file)
#         return conn
#     except sqlite3.Error as e:
#         print(e)
#     return None
#
# # Creates cursor object from connection object.
# def create_cursor(conn):
#     try:
#         c = conn.cursor()
#         return c;
#     except sqlite3.Error as e:
#         print(e)
#     return None
#
# # Closes the connection object.
# def close_conn(conn):
#     conn.commit()
#     conn.close()
#     return None
#
# def update_database(response, meta, cursor, table, count):
#
#     # Create the placeholders for each column
#     if count <= 0:
#         return None
#     col_string = ""
#     if count > 1:
#         for i in range(count - 1):
#             col_string += "?,"
#     col_string += "?"
#
#     # Extract metadata from tweets
#     for tweet in response.get_iterator():
#         tweet_data = []
#         for i in range(count):
#             entry = meta[i]
#             if entry in tweet:
#                 tweet_data.append(tweet[entry])
#             else:
#                  tweet_data.append('')
#         print(tweet_data)
#
#         # Add metadata to db
#         try:
#             cursor.execute("INSERT into {} VALUES({})".format(table, col_string),
#                            tweet_data)
#         except sqlite3.Error as e:
#             print(e)

# Get tweets
results = twitterSQLite.get_tweets(variables.hashtag, variables.tweet_count)

# Connect and populate db
my_db = variables.db_file
conn = twitterSQLite.create_connection(my_db)
c = twitterSQLite.create_cursor(conn)

twitterSQLite.populate_database(conn, variables.table_name, variables.col_dict, results)

# Save the changes
twitterSQLite.close_connection(conn)




