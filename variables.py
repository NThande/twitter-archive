# File containing necessary variables for twitter script.

from collections import OrderedDict

# DB to store tweets in.
db_file = "sharkweek.db"

# Name of table to store tweets in.
table_name = "twitter"

# Hashtag/keywords in each tweet.
hashtag = "#sharkweek"

# Number of tweets for each search.
tweet_count = 100;

# Dictionary of column names from Twitter response and data type. Primary key is assigned here.
col_dict = OrderedDict([('id','integer PRIMARY KEY'), ('text','text'), ('retweeted','numeric')])

# Print contents of each for testing.
# print(metaList)
for item in col_dict:
    print(item, col_dict[item])



