# initSQLite.py
# Basic script to create a table from the parameters from the variables.py file.
from MSSQL import twitter_MSSQL
from MSSQL import variables

conn = twitter_MSSQL.create_connection(variables.db_file)
cur = twitter_MSSQL.create_cursor(conn)
# twitter_MSSQL.create_table(cur, variables.table_name, variables.col_dict)
# twitter_MSSQL.alter_table(cur, variables.table_name, variables.col_dict)
# twitter_MSSQL.drop_table(cur, variables.table_name)
twitter_MSSQL.close_connection(conn)

