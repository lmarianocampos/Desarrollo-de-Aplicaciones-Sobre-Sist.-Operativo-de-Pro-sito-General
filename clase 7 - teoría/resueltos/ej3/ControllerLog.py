from LogDAO import LogDAO
from Log import Log
import json

class ControllerLog:


    def __init__(self,app,request,db):
        self.app = app
        self.request = request
        self.db = db


    def get(self):
        log_dao = LogDAO(self.db)

        #obtengo parametros de URL
        page = int(self.request.args.get('page', '0'))
        size = int(self.request.args.get('size', '10'))

        list_logs = log_dao.get_all(page,size)

        #transformo lista en JSON
        json_data = json.dumps(list_logs,default=Log.encode_log)

        #Construyo respuesta y la devuelvo
        response = self.app.response_class(
            response=json_data,
            status=200,
            mimetype='application/json'
        )
        return response

