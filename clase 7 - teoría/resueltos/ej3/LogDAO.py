from Log import Log

class LogDAO:

    def __init__(self,db):
        self.db = db
        self.c = self.db.cursor()


    def get_all(self,page,size):
        self.c.execute("SELECT id,id_dev,status,ts FROM log LIMIT ?,?",(page*size,size))
        list_log = []
        for i in self.c:
            d = Log(i[0],i[1],i[2],i[3])
            list_log.append(d)
        return list_log


    def add_log(self,id_dev,new_state):
        self.c.execute("INSERT INTO log (id_dev,status,ts) VALUES(?,?,datetime())",(id_dev,new_state))
        self.db.commit()
        return True



