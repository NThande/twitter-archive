# sharkweek.py
# Retrieves tweets from twitter and adds their metadata to the a table in a db, using variables .py as a guide.
# Prints benign errors if it rereads the same tweet.

from SQLite import variables
from SQLite import twitter_SQLite

results = twitter_SQLite.get_tweets(variables.hashtag, variables.tweet_count)
conn = twitter_SQLite.create_connection(variables.db_file)
cur = twitter_SQLite.create_cursor(conn)
twitter_SQLite.populate_database(cur, variables.table_name, variables.col_dict, results)
# twitter_SQLite.print_table(cur, variables.table_name, 100)
twitter_SQLite.close_connection(conn)




