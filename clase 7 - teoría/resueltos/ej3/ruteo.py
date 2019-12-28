from flask import Flask, json, request
from ControllerDevices import ControllerDevices
from ControllerDevice import ControllerDevice
from ControllerLog import ControllerLog
from flask import g
import sqlite3

app = Flask(__name__)

#*************** Manejo de DB ***************************
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


#*************** Ruteo ***************************
@app.route('/devices',methods=['GET'])
def devices():
    cont = ControllerDevices(app,request,get_db())
    return cont.get()


@app.route('/device/<id_dev>',methods=['PUT'])
def set_state_device(id_dev):
    cont = ControllerDevice(app,request,get_db())
    return cont.put(id_dev)

@app.route('/log',methods=['GET'])
def log():
    cont = ControllerLog(app,request,get_db())
    return cont.get()


#________________________________________________________




if __name__ == '__main__':
	app.debug = True
	app.run()
