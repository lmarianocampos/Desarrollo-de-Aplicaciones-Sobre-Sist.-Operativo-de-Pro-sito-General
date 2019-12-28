from flask import Flask, request
import sqlite3
from flask import g
from ControllerDevices import ControllerDevices

app = Flask(__name__)

#************** Manejo de DB ****************************
DATABASE = 'devices.db3'

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



@app.route('/devices')
def devices():
	#db = get_db()
	#c = db.cursor()
	#c.execute("SELECT * FROM Devices")
	#return "data:"+str(c.fetchall())
        cont = ControllerDevices(app,request,get_db())
        return cont.get()


if __name__ == '__main__':
	app.debug = True
	app.run()
