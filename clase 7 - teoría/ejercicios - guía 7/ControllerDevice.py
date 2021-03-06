import json
from DevicesDAO import DevicesDAO
from LogDAO import LogDAO
class ControllerDevice:
    def __init__(self,app,request,db):
        self.app = app
        self.request = request
        self.db = db
    
    def put(self,id_dev):
        #modifico el estado de un dispositivo
        dev_dao = DevicesDAO(self.db)
        log_dao = LogDAO(self.db)

        state = self.request.form['state']# leo el cuerpo del mensaje del request
        print(type(state))
        print (state)
        ret="ERROR"
        if dev_dao.set_state(id_dev,state):
            ret="OK"
            log_dao.add_log(id_dev,state)
        response = self.app.response_class(
            response=json.dumps({"state":ret}),
            status=200,
            mimetype='application/json'
        )
        return response


