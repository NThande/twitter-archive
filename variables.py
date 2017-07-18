from collections import OrderedDict

# File containing necessary variables for twitter script.
# Hashtag/keywords in each tweet.
hashtag = "#sharkweek"

# Number of tweets for each search.
tweet_count = 100;

metaDict = OrderedDict([('id','integer PRIMARY KEY'), ('text','text'), ('retweeted','numeric')])
metaList = list(metaDict.keys())
print(metaList)

for item in metaDict:
    print(item, metaDict[item])

# Name of table to store tweets in.
table = "twitter"

# Number of columns in table.
col_count = len(metaList)

