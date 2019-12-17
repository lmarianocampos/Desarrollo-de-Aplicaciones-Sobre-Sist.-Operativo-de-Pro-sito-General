from flask import Flask
import sqlite3
from flask import g

app = Flask(__name__)

#************** Manejo de DB ****************************
DATABASE = 'mydb.db3'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
#________________________________________________________



@app.route('/')
def hello_world():
	db = get_db()
	c = db.cursor()
	c.execute("SELECT * FROM Users")
	return "data:"+str(c.fetchall())




if __name__ == '__main__':
	app.debug = True
	app.run()
