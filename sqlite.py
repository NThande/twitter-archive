# sqlite.py
# Connects to the db specified in variables.py and creates a table. Adds new columns, if needed.

import variables
import twitterSQLite

conn = twitterSQLite.create_connection(variables.db_file)
twitterSQLite.create_table(conn, variables.table_name, variables.col_dict)
twitterSQLite.alter_table(conn, variables.table_name, variables.col_dict)
twitterSQLite.close_connection(conn)

