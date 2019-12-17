import sqlite3

#conn = sqlite3.connect('file:mydb.db3?mode=ro', uri=True) #read only no cambia el bloqueo
conn = sqlite3.connect('mydb.db3')
c = conn.cursor()

params = (3,)

it = c.execute('SELECT * FROM Users WHERE idJob=?',params)

for row in it:
	print(row)


conn.close()
