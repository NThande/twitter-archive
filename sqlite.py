# from sqlite3 import Error
# from sqlite3 import connect
import variables
import twitterSQLite

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


conn = twitterSQLite.create_connection(variables.db_file)
# twitterSQLite.drop_table(conn, variables.table_name)
twitterSQLite.create_table(conn, variables.table_name, variables.col_dict)
twitterSQLite.alter_table(conn, variables.table_name, variables.col_dict)
twitterSQLite.close_connection(conn)

