from Device import Device
class DevicesDAO:
    #esta clase va a tener todos los metodos que van a 
    #leer y escribir la base de datos 
    def __init__(self,db):
        self.db = db
        self.c = self.db.cursor()
    def get_all(self):
        self.c.execute('SELECT id,name,ip,status FROM Devices') 
        list_dev=[]
        for item in self.c:
            d = Device(item[0],item[1],item[2],item[3])
            list_dev.append(d)

        return list_dev
    def set_state(self,id_dev,state):
        if state =="0" or state=="1": 
            try:
                params = (state,id_dev,)
                self.c.execute('UPDATE Devices SET status=? WHERE id=?',params )
                self.db.commit()
                return True
            except:
                return False
        return False        
