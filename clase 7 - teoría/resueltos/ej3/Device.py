import json
class Device:

    def __init__(self,id,name,ip,state):
        self.__id = id
        self.__name = name
        self.__ip = ip
        self.__state = state

    @staticmethod
    def encode_device(obj):
        return {"id":obj.__id,"name":obj.__name,"ip":obj.__ip,"state":obj.__state}