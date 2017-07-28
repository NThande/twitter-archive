# varMSSQL.py
# File containing necessary variables for twitter script.

from collections import OrderedDict

# DB to store tweets in.
db_file = "sharkweek.db"

# Name of table to store tweets in.
table_name = "ncPOC_twitter_staging"

# Hashtag/keywords in each tweet.
hashtag = "#sharkweek"

# Number of tweets for each search.
tweet_count = 10;

# Dictionary of column names from Twitter response and data type. Primary key is assigned here.
col_dict = OrderedDict([('IdStr','text PRIMARY KEY'),
                        ('Text','text'),
                        ('Username', 'text'),
                        ('Created_at','integer'),
                       ])

# Print contents of each for testing.
# print(col_dict.keys())
# for item in col_dict:
#     print(item, col_dict[item])
