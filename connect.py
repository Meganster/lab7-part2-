import MySQLdb
from MySQLdb.constants import FIELD_TYPE

db = MySQLdb.connect(host="localhost", db="ask_db", read_default_file="~/.my.cnf")
cursor=db.cursor()
cursor.execute("select * from department")
result = cursor.fetchall()

for x in result:
    print(x)
