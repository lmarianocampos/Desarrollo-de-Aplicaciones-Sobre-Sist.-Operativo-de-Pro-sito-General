from DeviceDAO import DeviceDAO
from Device import Device
import json

class ControllerDevices:


    def __init__(self,app,requests,db):
        self.app = app
        self.requests = requests
        self.db = db

    def get(self):
        #c = self.db.cursor()
        #c.execute("SELECT * FROM Devices")
        #return "data:"+str(c.fetchall())
        dev_dao = DeviceDAO(self.db)
        
        list_devices = dev_dao.get_all()      

        data_json = json.dumps(list_devices,default=Device.dev_to_dict)

        response = self.app.response_class(
            response=data_json,
            status=200,
            mimetype='application/json'
        )
        return response