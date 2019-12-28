import json
from DeviceDAO import DeviceDAO
from Device import Device

class ControllerDevices:

    def __init__(self,app,request,db):
        self.app = app
        self.request = request
        self.db = db


    def get(self):
        #Creo DAO
        dev_dao = DeviceDAO(self.db)
        
        #Obtengo lista de obj Device
        list_devices = dev_dao.get_all() 

        #transformo lista en JSON
        json_data = json.dumps(list_devices,default=Device.encode_device)

        #Construyo respuesta y la devuelvo
        response = self.app.response_class(
            response=json_data,
            status=200,
            mimetype='application/json'
        )
        return response

