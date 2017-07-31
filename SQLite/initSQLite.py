# initSQLite.py
# Basic script to create a table from the parameters from the variables.py file.
from SQLite import twitter_SQLite
from SQLite import variables

conn = twitter_SQLite.create_connection(variables.db_file)
cur = twitter_SQLite.create_cursor(conn)
twitter_SQLite.create_table(cur, variables.table_name, variables.col_dict)
# twitter_SQLite.alter_table(cur, variables.table_name, variables.col_dict)
# twitter_SQLite.drop_table(cur, variables.table_name)
twitter_SQLite.close_connection(conn)

