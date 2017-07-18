# Simple script to drop the current db table.
import twitterSQLite
import variables

conn = twitterSQLite.create_connection(variables.db_file)
twitterSQLite.drop_table(conn, variables.table_name)
twitterSQLite.close_connection(conn)