#!/usr/bin/env python3
import json

class sensor:
    def __init__ (self,n,tipo):
        self.set_sensor_n(n)
        self.set_sensor_type(tipo)

    def set_sensor_n(self,n):
        self.__n_sensor = n

    def set_sensor_type(self,tipo):
        self.__type_sensor = tipo

    def get_sensor_type(self,tipo):
        return self.__type_sensor 

    def set_sensor_n(self,n):
        return self.__n_sensor 
    
    @staticmethod
    def file_read(path_file):  
        sensor = []
        key = ['temp','humedad']
        try:
            with open(path_file,"r",encoding= "UTF-8") as f:
                while True:
                    s = f.readline()
                    d={}
                    if s == "":
                        break # llego al final o el archivo esta vacio
                    #print (s)
                    s = s.strip("\n")
                    s = s.split(",")

                    k = key[0]
                    v = s[0]
                    d[k] =v       
                   
                    k = key[1]
                    v = s[1]
                    d[k] =v
                    sensor.append(d)
                
                ssr = json.dumps(sensor)
                print(ssr)                                 
        except IOError:
            print("error accessing file sensores.data")    
print("Content-Type: text/html\n")# para mostrar en el navegador

sensor.file_read("/tmp/sensores.data")  



