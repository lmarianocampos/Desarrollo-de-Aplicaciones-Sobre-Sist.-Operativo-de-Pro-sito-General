import sqlite3
from Device import Device

class DeviceDAO:

    def __init__(self,db):
        self.db = db
        self.c = self.db.cursor()

    def get_all(self):
        self.c.execute("SELECT id,name,ip,status FROM devices")
        list_devices = []
        for i in self.c:
            d = Device(i[0],i[1],i[2],i[3])
            list_devices.append(d)
        return list_devices

    def add_device(self,name,ip,state):
        try:
            params = (name,ip,state,)
            self.c.execute("INSERT INTO devices (name,ip,status) VALUES(?,?,?)",params)
            self.db.commit()
            return True
        except:
            return False

    def set_state(self,id_dev,state):
        try:
            params = (state,id_dev,)
            self.c.execute("UPDATE devices SET status=? WHERE id=?",params)
            self.db.commit()
            return True
        except:
            return False
