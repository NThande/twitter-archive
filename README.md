#Twitter Archive
#####Language: Python 3.6.1

Twitter-archive provides a library to interface Twitter responses to SQLite and MSSQL, 
and a basic method to retrieve tweets from Twitter and store them in a database.


Users will need to create their own Twitter App to generate a .json 
file (default name config.json) containing a consumer api key and 
consumer secret key in the format:

{
  "Consumer Key": "xxx",
  "Consumer Secret": "xxx"
}

Users will also need to store their MSSQL database information in a .json 
file (default name db_login.json) in the format: 

{
  "Server": "xxx",
  "User" : "xxx",
  "Password" : "xxx",
  "Port" : "xxx",
  "Source" : "xxx",
  "Driver" : xxx"
}

Specify search and column parameters in the variables.py file.

Python-Twitter API Wrapper:
https://github.com/geduldig/TwitterAPI