import sqlite3

conn = sqlite3.connect('mydb.db3')
c = conn.cursor()

params = ("Ernesto","Gigliotti","ernestogigliotti@gmail.com",3)

c.execute('INSERT INTO Users (name,lastname,email,idJob) VALUES(?,?,?,?)',params)
conn.commit()


conn.close()


