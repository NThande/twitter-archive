from collections import OrderedDict

# File containing necessary variables for twitter script.

# DB to store tweets in.
db_file = "sharkweek.db"

# Name of table to store tweets in.
table = "twitter"
# Hashtag/keywords in each tweet.
hashtag = "#sharkweek"

# Number of tweets for each search.
tweet_count = 100;

metaDict = OrderedDict([('id','integer PRIMARY KEY'), ('text','text'), ('retweeted','numeric')])
metaList = list(metaDict.keys())

# Print contents of each for testing.
print(metaList)
for item in metaDict:
    print(item, metaDict[item])

# Number of columns in table.
col_count = len(metaList)



