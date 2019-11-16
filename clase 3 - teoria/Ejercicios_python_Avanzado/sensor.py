from datetime import datetime
class Sensor:
    def __init__(self,n):
        self.setNSensor(n)
    
    def read_file(self,filePath):
        with open (filePath,"r") as f:
            s = f.read()
            value = float (s)
            return value
    def setNSensor(self,n):
        if n >= 0:
           self.__nSensor = n
    def getNSensor(slef):
        return slef.__nSensor

    def get_value(self):
        return 0

    @staticmethod    
    def logFileWrite(sensorL):
        i=0
        with open("/tmp/log_sensores.txt","a+",encoding="UTF-8")as f:
            timestamp = 1545730073 
            f.seek(0,2)
            tst = str(datetime.fromtimestamp(timestamp))
            f.write(tst)
            f.write(" ")
            for item in sensorL:
                value = item.get_value()
                if i <4:
                    s = str(value)+","
                else:
                     s = str(value)+"\n"
                     i=0
                i+=1        
                f.seek(0,1)
                f.write(s)


class SensorTemp(Sensor):
    def __init__(self,n):
        super().__init__(n)

    def get_value(self):
        filePath = "/tmp/temp{}.data".format(self.getNSensor())
        value = self.read_file(filePath)
        if value < 0:
            value = 0
        return value

class SensorHum(Sensor):
    def __init__(self,n):
        super().__init__(n)

    def get_value(self):
        filePath ="/tmp/hum{}.data".format(self.getNSensor())
        value = self.read_file(filePath)
        value = float(value)/10
        return value    
