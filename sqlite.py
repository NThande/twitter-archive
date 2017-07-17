from sqlite3 import Error
from sqlite3 import connect

def create_connection(db_file):
    try:
        conn = connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


def create_table(conn, table):
    try:
        c = conn.cursor()
        c.execute(table)
    except Error as e:
        print(e)
    finally:
        conn.commit()
        conn.close()
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
my_db = "sharkweek.db"
conn = create_connection(my_db)
create_table(conn, sql_create_twitter_table)
