# File containing necessary variables for twitter script.
# Hashtag/keywords in each tweet.
var_hashtag = "#sharkweek"

# Number of tweets for each search.
var_count = 100;

for item in results.get_iterator():
    print(item['user']['screen_name'], item['text'], item['id'])
    # id = item['id']
    # user = item['user']['name']
    # screen_name = item['user']['screen_name']
    # text = item['text']
    # id_str = item['id_str']
    # retweeted = item['retweeted']
    # retweet_count = item['retweet_count']
    # favorited = item['favorited']
    # favorite_count = item['favorite_count']
    # if 'possibly_sensitive' in item:
    #     possibly_sensitive = item['possibly_sensitive']
    # else:
    #     possibly_sensitive = ''
    # lang = item['lang']
    # source = item['source']
    # created_at = item['created_at']
    #
    # # Add metadata to db
    # try:
    #     c.execute("INSERT into twitter VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
    #               [id, user, screen_name, text, id_str, retweeted, retweet_count, favorited,
    #                favorite_count, possibly_sensitive, lang, source, created_at])
    # except sqlite3.Error as e:
    #     print(e)

sql_create_twitter_table = '''CREATE TABLE IF NOT EXISTS twitter (
                              id integer PRIMARY KEY,
                              user text,
                              screen_name text,
                              text text,
                              id_str text,
                              retweeted numeric,
                              retweet_count integer,
                              favorited numeric,
                              favorite_count integer,
                              possibly_sensitive numeric,
                              lang text,
                              source text,
                              created_at text);
                           '''