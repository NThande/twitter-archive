# sharkweek.py
# Retrieves tweets from twitter and adds their metadata to the a table in a db, using variables.py as a guide.
# Prints benign errors if it rereads the same tweet.

from MSSQL import variables

from MSSQL import twitter_MSSQL

results = twitter_MSSQL.get_tweets(variables.hashtag, variables.tweet_count, variables.config_file)
conn = twitter_MSSQL.create_trusted_connection(variables.db_file)
cur = twitter_MSSQL.create_cursor(conn)
twitter_MSSQL.populate_database(cur, variables.table_name, variables.col_dict, results)
# twitter_MSSQL.print_table(cur, variables.table_name, 100)
twitter_MSSQL.close_connection(conn)