# varMSSQL.py
# File containing necessary variables for twitter script.

from collections import OrderedDict

# Name of file with twitter credentials.
config_file = 'config.json'

# Name of file with database credentials.
db_file = 'db_login.json'

# Name of table to store tweets in.
table_name = "ncPOC_twitter_staging"

# Hashtag/keywords in each tweet.
hashtag = "#sharkweek"

# Number of tweets for each search.
tweet_count = 10;

# Dictionary of column names from Twitter response and data type. Primary key is assigned here.
col_dict = OrderedDict([('id_str','NVARCHAR(50) NOT NULL PRIMARY KEY'),
                        ('text','NVARCHAR(250) NOT NULL'),
                        ('name', 'NVARCHAR(50) NOT NULL'),
                        ('created_at','NVARCHAR(50) NOT NULL'),
                       ])

# Print contents of each for testing.
# print(col_dict.keys())
# for item in col_dict:
#     print(item, col_dict[item])
