from sqlite3 import Error
from sqlite3 import connect
from TwitterAPI import TwitterAPI

# Connects to an SQLite DB file.
def create_connection(db_file):
    try:
        conn = connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def close_connection(conn):
    try:
        conn.commit()
        conn.close()
    except Error as e:
        print(e)

# Creates table with name table_name and columns in col_dict in database connected by conn. col_dict must contain
# col_name: col_type format.
def create_table(conn, table_name, col_dict):

    # Iterate through metaDict to construct query
    table_string = "CREATE TABLE IF NOT EXISTS {} (".format(table_name)
    for item in col_dict:
        if (item != list(col_dict.keys())[-1]):
            table_string += "{} {}, ".format(item, col_dict[item])
        else:
            table_string += "{} {});".format(item, col_dict[item])

    # Execute table creation
    try:
        c = conn.cursor()
        c.execute(table_string)
    except Error as e:
        print(e)

# Deletes table with table_name from database connected by conn.
def drop_table(conn, table_name):
    try:
        c = conn.cursor()
        c.execute("DROP TABLE {}".format(table_name))
    except Error as e:
        print(e)

# Adds columns from col_dict to table with table_name in database connected by conn.
def alter_table(conn, table_name, col_dict):
    try:
        c = conn.cursor()
        for item in col_dict:
            try:
                c.execute("ALTER TABLE {} ADD COLUMN {} {}".format(table_name, item, col_dict[item]))
            except Error as e:
                print(e)
    except Error as e:
        print(e)

# Takes in oAuth keys from config.json and returns n tweets containing hash as an API response.
def get_tweets(hash, n):

    # Retrieve keys from config file
    with open('config.json') as json_data_file:
        creds = json.load(json_data_file)
    key = creds['Consumer Key']
    secret = creds['Consumer Secret']

    # Get tweets from Twitter
    api = TwitterAPI(key, secret, auth_type='oAuth2')
    r = api.request('search/tweets', {'q': hash, 'count': n})
    return r

# Connects to db_file and returns connected variable.
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

# Creates cursor object from connection object.
def create_cursor(conn):
    try:
        c = conn.cursor()
        return c;
    except sqlite3.Error as e:
        print(e)
    return None

# Closes the connection object.
def close_conn(conn):
    conn.commit()
    conn.close()
    return None

def update_database(response, meta, cursor, table, count):

    # Create the placeholders for each column
    if count <= 0:
        return None
    col_string = ""
    if count > 1:
        for i in range(count - 1):
            col_string += "?,"
    col_string += "?"

    # Extract metadata from tweets
    for tweet in response.get_iterator():
        tweet_data = []
        for i in range(count):
            entry = meta[i]
            if entry in tweet:
                tweet_data.append(tweet[entry])
            else:
                 tweet_data.append('')
        print(tweet_data)

        # Add metadata to db
        try:
            cursor.execute("INSERT into {} VALUES({})".format(table, col_string),
                           tweet_data)
        except sqlite3.Error as e:
            print(e)