# sharkweek.py
# Retrieves tweets from twitter and adds their metadata to the a table in a db, using variables .py as a guide.
# Prints benign errors if it rereads the same tweet.

import varMSSQL
import twitter_MSSQL

results = twitter_MSSQL.get_tweets(varMSSQL.hashtag, varMSSQL.tweet_count, varMSSQL.config_file)
conn = twitter_MSSQL.create_trusted_connection(varMSSQL.db_file)
cur = twitter_MSSQL.create_cursor(conn)
twitter_MSSQL.populate_database(cur, varMSSQL.table_name, varMSSQL.col_dict, results)
twitter_MSSQL.print_table(cur, varMSSQL.table_name, 100)
twitter_MSSQL.close_connection(conn)