# import pymssql
import pyodbc

db_server = "dctzqpdb04.us.dci.discovery.com"
db_user = "gocuser"
db_pass = "GOCuser_2012"
db_port = "2704"
db_source = "gocreporting"
db_driver = 'ODBC Driver 13 for SQL Server'

print(pyodbc.drivers())
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=mine;UID=me;PWD=pwd')
# connect = pyodbc.connect(server=server, port=db_port, user=db_user, password=db_pass, database=db_source)
# cnxn = pyodbc.connect('''DRIVER={};
#                       SERVER={};DATABASE={};
#                       UID={};
#                       PWD={}
#                       '''.format(db_driver, db_server, db_source, db_user, db_pass))
cnxn = pyodbc.connect(driver = db_driver,
                      server = db_server,
                      database = db_source,
                      port = db_port,
                      # uid = db_user,
                      # pwd = db_pass,
                      trusted_connection = 'yes')
cur = cnxn.cursor();
cur.execute("SELECT * FROM ncPOC_twitter_staging")
test_rows = cur.fetchall()
for row in test_rows:
     print(row)
# for row in cur.columns(table='gocreporting.dbo.ncPOC_twitter'):
#     print(row.column_name)
#     for field in row:
#         print(field)
# print(test_rows)
# print(cur.columns(table = 'gocreporting.dbo.ncPOC_twitter'))
cnxn.close()
