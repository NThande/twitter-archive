Twitter-archive provides a library to interface Twitter resposnes to SQLite, and a basic method to retrieve tweets from Twitter and store them in a local SQLite database.

Language: Python 3.6.1

Users will need to have their own Twitter account to generate a .json 
file containing a consumer api key and consumer secret key in the format:

{
  "Consumer Key": "xxx",
  "Consumer Secret": "xxx"
}

Users will also need to have their database information in a .json 
file in the format:

{
  "Server": "xxx",
  "User" : "xxx",
  "Password" : "xxx",
  "Port" : "xxx",
  "Source" : "xxx",
  "Driver" : xxx"
}
 
The names of these .json's is not hard-coded. Specify them in the variables.py file.
Python-Twitter API Wrapper:
https://github.com/geduldig/TwitterAPI