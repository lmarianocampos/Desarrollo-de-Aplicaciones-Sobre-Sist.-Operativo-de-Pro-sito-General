from Device import Device

class DeviceDAO:

    def __init__(self,db):
        self.db = db
        self.c = self.db.cursor()


    def get_all(self):
        self.c.execute("SELECT id,name,ip,status FROM Devices")

        list_devices=[]
        for item in self.c:
            d = Device(item[0],item[1],item[2],item[3])
            list_devices.append(d)            

        return list_devices

    def set_state(self,id_device,state):
        params = (state,id_device)
        self.c.execute("UPDATE Devices SET status=? WHERE id=?",params)
        self.db.commit()
        