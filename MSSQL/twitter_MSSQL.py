# twitter_MSSQL.py
# Function library to interface SQLite with the TwitterAPI, using the Python-TwitterAPI wrapper.
# Twitter API: https://github.com/geduldig/TwitterAPI

from TwitterAPI import TwitterAPI
import json
import pyodbc

# Connects to a MSSQL Database using SQL credentials from db_file.json and returns the created connection object.
def create_connection(db_file):
    with open(db_file) as json_data_file:
        creds = json.load(json_data_file)

    try:
        conn = pyodbc.connect(driver = creds["Driver"],
                              server = creds["Server"],
                              database = creds["Source"],
                              port = creds["Port"],
                              uid = creds["User"],
                              pwd = creds["Password"]
                              )
        return conn
    except Exception as e:
        print(e)
    return None

# Connects to a MSSQL Database using Windows credentials from db_file.json and returns the created connection object.
def create_trusted_connection(db_file):
    with open(db_file) as json_data_file:
        creds = json.load(json_data_file)

    try:
        conn = pyodbc.connect(driver = creds["Driver"],
                              server = creds["Server"],
                              database = creds["Source"],
                              port = creds["Port"],
                              trusted_connection = 'yes'
                              )
        return conn
    except Exception as e:
        print(e)
    return None

# Saves changes to db connected by conn and closes conn.
def close_connection(conn):
    try:
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

# Creates cursor object from connection object.
def create_cursor(conn):
    try:
        cur = conn.cursor()
        return cur;
    except Exception as e:
        print(e)
    return None

# Creates table with name table_name and columns in col_dict in database with cursor cur. Returns an error if table
#   already exissts.
def create_table(cur, table_name, col_dict):
    table_string = "CREATE TABLE {} (".format(table_name)
    for item in col_dict:
        if (item != list(col_dict.keys())[-1]):
            table_string += "{} {}, ".format(item, col_dict[item])
        else:
            table_string += "{} {});".format(item, col_dict[item])

    # Create table in db
    try:
        cur.execute(table_string)
    except Exception as e:
        print(e)

# Deletes table with table_name from database with cursor cur. Returns an error if table does not exist.
#   USE WITH CAUTION!
def drop_table(cur, table_name):
    try:
        cur.execute("DROP TABLE {}".format(table_name))
    except Exception as e:
        print(e)

# Adds columns from col_dict to table with table_name in database with cursor cur.
def alter_table(cur, table_name, col_dict):
    for item in col_dict:
        try:
            cur.execute("ALTER TABLE {} ADD {} {}".format(table_name, item, col_dict[item]))
        except Exception as e:
            print(e)

# Reads the top row_count rows in table table_name with columns in col_dict from database with cursor cur.
def print_table(cur, table_name, row_count):
    rows = cur.execute("SELECT TOP ({}) * FROM {}".format(row_count, table_name)).fetchall()
    for entry in rows:
        print(entry)

# Takes in oAuth keys from config.json and returns tweet_count tweets containing hash as an API response.
def get_tweets(hashtag, tweet_count, config_file):
    with open(config_file) as json_data_file:
        creds = json.load(json_data_file)
    key = creds['Consumer Key']
    secret = creds['Consumer Secret']

    # Get tweets from Twitter
    api = TwitterAPI(key, secret, auth_type='oAuth2')
    r = api.request('search/tweets', {'q': hashtag, 'count': tweet_count})
    return r

# Populates table table_name in db with cursor cur and with tweet info from TwitterAPI response tweet_response. col_dict
# determines which columns of metadata are added to the db.
def populate_database(cur, table_name, col_dict, tweet_response):
    col_list = list(col_dict.keys())
    count = len(col_list)

    # Create the "?" placeholders for each column
    if count <= 0:
        return None
    col_string = ""
    if count > 1:
        for i in range(count - 1):
            col_string += "?,"
    col_string += "?"

    # Extract metadata from tweets
    for tweet in tweet_response.get_iterator():
        tweet_data = []
        for i in range(count):
            entry = col_list[i]
            if entry in tweet:
                tweet_data.append(tweet[entry])
            elif entry in tweet['user']:
                tweet_data.append((tweet['user'])[entry])
            else:
                tweet_data.append('')

    # Prints tweet data as it populates the table.
    #     print(tweet_data)

        # Add metadata to db
        try:
            cur.execute("INSERT into {} VALUES({})".format(table_name, col_string),
                           tweet_data)
        except Exception as e:
            print(e)