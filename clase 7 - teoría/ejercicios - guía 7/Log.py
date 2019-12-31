class Log:
    def __init__(self,idLog,id,status,ts):
        self.__idLog = idLog
        self.__id = id
        self.__status = status
        self.__ts = ts
    @staticmethod
    def encode_log(obj):
        return {"idLog":obj.__idLog,"id":obj.__id,"status":obj.__status,"timestamp":obj.__ts}
               