from flask import Flask,request
import sqlite3
from flask import g
from controllerDevices import ControllerDevices
from ControllerDevice import ControllerDevice

app = Flask(__name__)

#************** Manejo de DB ****************************
DATABASE = 'devices.db3'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        try: 
            db = g._database = sqlite3.connect(DATABASE)
            return db
        except:
            print("\n Error al conectar la BD..")
    

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
#________________________________________________________



@app.route('/devices',methods = ['GET'])
def divaces():
	#db = get_db()
	#c = db.cursor()
	#c.execute("SELECT * FROM Devices")
	#return "data:"+str(c.fetchall())
    cont = ControllerDevices(app,request,get_db())
    return cont.get()
@app.route('/device/<id_dev>',methods = ['PUT'])
def set_state_device(id_dev):
        cont = ControllerDevice(app,request,get_db())
        return cont.put(id_dev)


if __name__ == '__main__':
	app.debug = True
	app.run()
