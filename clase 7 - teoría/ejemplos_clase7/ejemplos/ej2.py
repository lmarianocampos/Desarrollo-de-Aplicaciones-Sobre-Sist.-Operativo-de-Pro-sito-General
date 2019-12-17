import sqlite3

conn = sqlite3.connect('mydb.db3')
c = conn.cursor()

params = (3,)   #tupla

c.execute('SELECT * FROM Users WHERE idJob=?',params)

for row in c:
	print(row)


conn.close()


