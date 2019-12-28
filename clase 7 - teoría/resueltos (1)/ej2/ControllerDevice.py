import json
from DeviceDAO import DeviceDAO


class ControllerDevice:

    def __init__(self,app,request,db):
        self.app = app
        self.request = request
        self.db = db


    def put(self,id_dev):
        #modifico estado de device
        
        dev_dao = DeviceDAO(self.db)

        state = self.request.form['state'] #leo body de PUT
        ret="ERROR"
        if dev_dao.set_state(id_dev,state):
            ret="OK"

        response = self.app.response_class(
            response=json.dumps({"state":ret}),
            status=200,
            mimetype='application/json'
        )
        return response


