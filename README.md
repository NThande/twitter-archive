# Twitter-Archive
#### Language: Python 3.6.1

Twitter-Archive provides a function library to interface Twitter responses to SQLite and MSSQL, 
and a basic method to retrieve tweets from Twitter and store them in a database. Supports searching
Twitter using one term (i.e. #sharkweek) and setting the number of tweets to retrieve. Note that Twitter
will rate-limit requests for an excessive amount of tweets.

To get started, download the repository using the Green "Clone or Download" button in the top right.

### Requirements
Python-Twitter API Wrapper: (https://github.com/geduldig/TwitterAPI)
```
pip install TwitterAPI
```
Twitter API Keys: (https://apps.twitter.com/)
1. Login into your Twitter Account
2. Create a new App or access an existing one
3. Retrieve keys from "Keys and Access Tokens" Section of App

### Setup
1. Clone the repository using the green "Clone or Download" button in the top right, or use the following:
```
git clone https://github.discovery.com/nthande/Twitter-Archive.git
```
2. Populate config.json with your App's Twitter API keys.
```
{
  "Consumer Key": "some_gibberish",
  "Consumer Secret": "more_gibberish"
}
```
3. For MSSQL users, populate db_login.json with your MSSQL database information.
```
{
  "Server": "servername",
  "User" : "username",
  "Password" : "pw",
  "Port" : "8080",
  "Source" : "dbname",
  "Driver" : "ODBC Driver 13 for SQL Server"
}
```
4. Set the desired parameters in the variables.py file
```
# Name of file with twitter credentials.
config_file = 'config.json'

# Name of file with database credentials.
db_file = 'db_login.json'

# Name of table to store tweets in.
table_name = "tweet_table"

# Hashtag/keywords in each tweet.
hashtag = "#example"

# Number of tweets for each search.
tweet_count = 100;

# Dictionary of column names from Twitter response and data type. Primary key is assigned here.
col_dict = OrderedDict([('id_str','NVARCHAR(50) NOT NULL PRIMARY KEY'),
                        ('text','NVARCHAR(250) NOT NULL'),
                        ('name', 'NVARCHAR(50) NOT NULL'),
                        ('created_at','NVARCHAR(50) NOT NULL'),
                       ])
```

### Testing
init_MSSQL.py/init_SQLite.py: Tests table creation/manipulation tools.

sharkweek.py: Tests the end-to-end process of accessing and storage of tweets.

Run each test by running the corresponding script. Uncomment lines of code to test each feature.

For a successful test, this message should appear: 
```
Process finished with exit code 0
```
SQL error messages may also appear in the command window. These are benign and can be ignored.

### Notes
The Twitter API returns information as fields of a larger data object. These fields should be used to determine
the column names for a table for storing tweets. A reference can be found here: https://dev.twitter.com/overview/api/tweets

This version of Twitter-Archive must be run manually. There are no plans for automated scheduling at this time.

### License
Licensed under the Unlicense. See LICENSE for more details.
