import sqlite3
import time

conn = sqlite3.connect('mydb.db3')
c = conn.cursor()

params = ("Juan","Perez","ernestogigliotti@gmail.com",3)

print("insertando...")
for i in range(1,10000):
	try:
		c.execute('INSERT INTO Users (name,lastname,email,idJob) VALUES(?,?,?,?)',params)
		conn.commit()
		#time.sleep(0.01)
	except:
		print("la base esta bloqueada")
		break
print("fin.")

conn.close()

