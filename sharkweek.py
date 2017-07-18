# sharkweek.py
# Retrieves tweets from twitter and adds their metadata to the a db table, using variables .py as a guide.

import variables
import twitterSQLite

# Get tweets
results = twitterSQLite.get_tweets(variables.hashtag, variables.tweet_count)

# Connect and populate db
my_db = variables.db_file
conn = twitterSQLite.create_connection(my_db)
c = twitterSQLite.create_cursor(conn)

twitterSQLite.populate_database(conn, variables.table_name, variables.col_dict, results)

# Save the changes
twitterSQLite.close_connection(conn)




