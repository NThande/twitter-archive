# variables.py
# File containing necessary variables for SQLite twitter script.

from collections import OrderedDict

# Name of file with twitter credentials.
config_file = 'config.json'

# DB to store tweets in.
db_file = "sharkweek.db"

# Name of table to store tweets in.
table_name = "twitter"

# Hashtag/keywords in each tweet.
hashtag = "#sharkweek"

# Number of tweets for each search.
tweet_count = 10;

# Dictionary of column names from Twitter response and data type. Primary key is assigned here.
col_dict = OrderedDict([('id','integer PRIMARY KEY'),
                        ('text','text'),
                        ('created_at', 'text'),
                        ('retweet_count', 'integer'),
                        ('favorite_count','integer'),
                        ('possibly_sensitive', 'numeric'),
                        ('lang', 'text'),
                        ('source', 'text'),
                        ('id_str','text')
                       ])

# Print contents of each for testing.
# print(col_dict.keys())
# for item in col_dict:
#     print(item, col_dict[item])
