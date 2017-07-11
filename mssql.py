import pymssql

server = "dctzqpdb04.us.dci.discovery.com"
db_user = "gocuser"
db_pass = "GOCuser_2012"
db_port = "2704"
db_source = "gocreporting"

connect = pymssql.connect(server=server, port=db_port, user=db_user, password=db_pass, database=db_source)
connect.close()
