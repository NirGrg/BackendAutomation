import mysql.connector

# host, database, user, password
conn = mysql.connector.connect(host='localhost', database='APIDevelop',
                        user='root', password='root')

print(conn.is_connected())

curse = conn.cursor()

curse.execute('select * from ALL_TABLES')

row = curse.fetchall()