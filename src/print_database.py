import sqlite3 as lite

con = lite.connect('storage/users.sqlite3')
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM data")
    row = cur.fetchone()
    while row != None:
        print(row)
        break
