import json
from LogDAO import LogDAO
from Log import Log
class ControllerLog:
    def __init__(self,app,request,db):
        self.app = app
        self.request = request
        self.db = db
    
    def get(self):
        log_dao =LogDAO(self.db)

        #obtengo parametros de la URL
        page = int(self.request.args.get('page','0'))
        #devuelve el valor predeterminado si los parametros no existen
        size = int(self.request.args.get('size','10'))
        #devuelve el valor predeterminado si los parametros no existen
        list_logs = log_dao.get_all(page,size)
        #transformo la lista en json
        json_data = json.dumps(list_logs,default = Log.encode_log)
        #contruyo respuesta y devuelvo
        response = self.app.response_class(
            response = json_data,
            status = 200,
            mimetype = 'aplication/json'
        )
        return response