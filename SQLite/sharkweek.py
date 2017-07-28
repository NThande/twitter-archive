# sharkweek.py
# Retrieves tweets from twitter and adds their metadata to the a table in a db, using variables .py as a guide.
# Prints benign errors if it rereads the same tweet.

import variables
import twitterSQLite

results = twitterSQLite.get_tweets(variables.hashtag, variables.tweet_count)
conn = twitterSQLite.create_connection(variables.db_file)
twitterSQLite.populate_database(conn, variables.table_name, variables.col_dict, results)
twitterSQLite.close_connection(conn)




