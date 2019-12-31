from Log import Log
class LogDAO:
    def __init__(self,db):
        self.db = db
        self.c = self.db.cursor()
   
    def get_all(self,page,size):
        self.c.execute('SELECT idLog,id,status,ts FROM logs LIMIT ?,?',(page*size,size))
        list_log = []
        for i in self.c:
            d = Log(i[0],i[1],i[2],i[3])
            list_log.append(d)
        return list_log
    
    def add_log(self,id_dev,new_status):
        try:
            self.c.execute('INSERT INTO logs (id,status,ts) VALUES (?,?,datetime())',(id_dev,new_status))
            #last_idlog = self.c.lastrowid # me devuelve el ultimo ID autoincremental
            #self.c.execute('INSERT INTO tiene (id,idLog) VALUES (?,?)',(id_dev,last_idlog))
            self.db.commit()
            return True
        except:
            print("\n Error al agregar un registro log")
            return False   