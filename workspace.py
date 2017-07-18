import variables
col_string = "?"
for i in range(10):
    col_string += "?,"
# col_string += "?"
print(col_string)

conv = {"id":"", "test": ""}
conv["id"] = 123
conv["id"] = 2323
conv["test"] = conv["id"]
print(conv)
print(conv.keys())
print(type(conv.keys()))
print(dir(variables))
print(variables.hashtag)
cool = (1,2,3,4)
print(cool)

# # Metadata to extract.
# metaList = ['id', 'name', 'screen_name', 'text']
#
# # Data type for each piece of metadata.
# typeList = ['integer', 'text', 'text', 'text']
#
# # Dictionary combining the typeList and the metaList.
# metaDict = dict(zip(metaList, typeList))

# print(metaDict.items())
# metaDict.pop('id')
# print(metaDict.items())
# metaDict.setdefault('id','name')
# print(metaDict.items())
# metaDict.pop('name')
# print(metaDict.items())
# metaDict.setdefault('name','text')
# print(metaDict.items())

# Name of table to store
# for item in results.get_iterator():
#     print(item['user']['screen_name'], item['text'], item['id'])
#     # id = item['id']
#     # user = item['user']['name']
#     # screen_name = item['user']['screen_name']
#     # text = item['text']
#     # id_str = item['id_str']
#     # retweeted = item['retweeted']
#     # retweet_count = item['retweet_count']
#     # favorited = item['favorited']
#     # favorite_count = item['favorite_count']
#     # if 'possibly_sensitive' in item:
#     #     possibly_sensitive = item['possibly_sensitive']
#     # else:
#     #     possibly_sensitive = ''
#     # lang = item['lang']
#     # source = item['source']
#     # created_at = item['created_at']
#     #
#     # # Add metadata to db
#     # try:
#     #     c.execute("INSERT into twitter VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
#     #               [id, user, screen_name, text, id_str, retweeted, retweet_count, favorited,
#     #                favorite_count, possibly_sensitive, lang, source, created_at])
#     # except sqlite3.Error as e:
#     #     print(e)
#
# sql_create_twitter_table = '''CREATE TABLE IF NOT EXISTS twitter (
#                               id integer PRIMARY KEY,
#                               user text,
#                               screen_name text,
#                               text text,
#                               id_str text,
#                               retweeted numeric,
#                               retweet_count integer,
#                               favorited numeric,
#                               favorite_count integer,
#                               possibly_sensitive numeric,
#                               lang text,
#                               source text,
#                               created_at text);
#                            '''

# # Creates the SQlite query to create database table with name table_name and columns corresponding to col_dict.
# def create_columns(table_name, col_dict):
#     table_string = "CREATE TABLE IF NOT EXISTS {} (".format(table_name)
#
#     # Iterate through metaDict to construct query
#     for item in col_dict:
#         if (item != list(col_dict.keys())[-1]):
#             table_string += "{} {}, ".format(item, col_dict[item])
#         else:
#             table_string += "{} {});".format(item, col_dict[item])
#
#     return table_string



# sql_create_twitter_table = create_columns(variables.table, variables.metaDict)
# print(sql_create_twitter_table)

# sql_create_twitter_table = '''CREATE TABLE IF NOT EXISTS twitter (
#                               id integer PRIMARY KEY,
#                               user text,
#                               screen_name text,
#                               text text);
#                            '''
# print(sql_create_twitter_table)
# Connect to db
# my_db = "sharkweek.db"
# conn = create_connection(my_db)
#
# try:
#     c = conn.cursor()
#     c.execute("INSERT into twitter VALUES(?,?,?,?)", ['','','',r])
# except sqlite3.Error as e:
#     print(e)
# finally:
#     conn.commit()
#     conn.close()

#c.execute("INSERT into twitter VALUES(?,?,?,?)", ['','','',r])

# # Dump tweets to .json file
# r = results.json()
# print(type(r))
# print(type((r,)))
# with open('tweets.json', 'w') as outfile:
#       json.dump(r, outfile)

# # Print types and data entries to find fields for SQLite debugging
# print(results.json())
# print(r.keys())
# rLay1 = r['statuses']
# rMeta = r['search_metadata']
# rLay2 = rLay1[-1]
# rLay3 = rLay2['user']
# rLay4 = rLay3['screen_name']
# print("Layer 1 is type:", type(rLay1))
# print("Layer 2 entries in Layer 1:", rLay1[0:-1])
# print("Layer 2 is type:", type(rLay2))
# print("Layer 3 entries in Layer 2:", rLay2.keys())
# print("Layer 3 is type:", type(rLay3))
# print("Layer 4 entries in Layer 3:", rLay3.keys())
# print("Layer 4 is type: ", type(rLay4))
# print("Layer 4 is the end layer")
# print("Metadata is type:", type(rMeta))
# print("Keys in Metadata:", rMeta.keys())

# # Retrieve metadata for each tweet and add to db
# for item in results.get_iterator():
#     print(item['user']['screen_name'], item['text'], item['id'])
#     id = item['id']
#     user = item['user']['name']
#     screen_name = item['user']['screen_name']
#     text = item['text']
#
#     # Add metadata to db
#     try:
#         c.execute("INSERT into twitter VALUES(?,?,?,?)",
#                   ([id, user, screen_name, text]))
#     except sqlite3.Error as e:
#         print(e)

# # Takes in oAuth keys from config.json and returns n tweets containing hash as an API response.
# def get_tweets(hash, n):
#
#     # Retrieve keys from config file
#     with open('config.json') as json_data_file:
#         creds = json.load(json_data_file)
#     key = creds['Consumer Key']
#     secret = creds['Consumer Secret']
#
#     # Get tweets from Twitter
#     api = TwitterAPI(key, secret, auth_type='oAuth2')
#     r = api.request('search/tweets', {'q': hash, 'count': n})
#     return r

# # Connects to db_file and returns connected variable.
# def create_connection(db_file):
#     try:
#         conn = sqlite3.connect(db_file)
#         return conn
#     except sqlite3.Error as e:
#         print(e)
#     return None
#
# # Creates cursor object from connection object.
# def create_cursor(conn):
#     try:
#         c = conn.cursor()
#         return c;
#     except sqlite3.Error as e:
#         print(e)
#     return None
#
# # Closes the connection object.
# def close_conn(conn):
#     conn.commit()
#     conn.close()
#     return None
#
# def update_database(response, meta, cursor, table, count):
#
#     # Create the placeholders for each column
#     if count <= 0:
#         return None
#     col_string = ""
#     if count > 1:
#         for i in range(count - 1):
#             col_string += "?,"
#     col_string += "?"
#
#     # Extract metadata from tweets
#     for tweet in response.get_iterator():
#         tweet_data = []
#         for i in range(count):
#             entry = meta[i]
#             if entry in tweet:
#                 tweet_data.append(tweet[entry])
#             else:
#                  tweet_data.append('')
#         print(tweet_data)
#
#         # Add metadata to db
#         try:
#             cursor.execute("INSERT into {} VALUES({})".format(table, col_string),
#                            tweet_data)
#         except sqlite3.Error as e:
#             print(e)


# # Connects to an SQLite DB file.
# def create_connection(db_file):
#     try:
#         conn = connect(db_file)
#         return conn
#     except Error as e:
#         print(e)
#     return None
#
# def close_connection(conn):
#     try:
#         conn.commit()
#         conn.close()
#     except Error as e:
#         print(e)
#
# # Creates table with name table_name and columns in col_dict in database connected by conn. col_dict must contain
# # col_name: col_type format.
# def create_table(conn, table_name, col_dict):
#
#     # Iterate through metaDict to construct query
#     table_string = "CREATE TABLE IF NOT EXISTS {} (".format(table_name)
#     for item in col_dict:
#         if (item != list(col_dict.keys())[-1]):
#             table_string += "{} {}, ".format(item, col_dict[item])
#         else:
#             table_string += "{} {});".format(item, col_dict[item])
#
#     # Execute table creation
#     try:
#         c = conn.cursor()
#         c.execute(table_string)
#     except Error as e:
#         print(e)
#
# # Deletes table with table_name from database connected by conn.
# def drop_table(conn, table_name):
#     try:
#         c = conn.cursor()
#         c.execute("DROP TABLE {}".format(table_name))
#     except Error as e:
#         print(e)
#
# # Adds columns from col_dict to table with table_name in database connected by conn.
# def alter_table(conn, table_name, col_dict):
#     try:
#         c = conn.cursor()
#         for item in col_dict:
#             try:
#                 c.execute("ALTER TABLE {} ADD COLUMN {} {}".format(table_name, item, col_dict[item]))
#             except Error as e:
#                 print(e)
#     except Error as e:
#         print(e)