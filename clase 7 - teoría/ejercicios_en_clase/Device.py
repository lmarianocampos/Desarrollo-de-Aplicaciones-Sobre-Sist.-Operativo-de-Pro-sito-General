class Device:

    def __init__(self,id,name,ip,state):
        self.__id=id
        self.__name=name
        self.__ip=ip
        self.__state=state
     

    @staticmethod
    def dev_to_dict(obj):
        return {"id":obj.__id,"name":obj.__name,"ip":obj.__ip,"state":obj.__state}


    