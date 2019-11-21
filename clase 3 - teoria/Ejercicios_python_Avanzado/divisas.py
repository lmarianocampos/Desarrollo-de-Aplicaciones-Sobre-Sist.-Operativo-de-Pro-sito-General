import json

class Divisa:
    def __init__(self, id, divisaName,buy,sale):
        self.setId(id)
        self.setDivisaName(divisaName)
        self.setBuy(buy)
        self.setSale(sale)

    def setId(self,id):
        if id > 0:
            self.__id = id

    def setDivisaName(self,divisaName):
        self.__divisaName = divisaName
    
    def setBuy(self,buy):
        self.__buy = buy

    def setSale (self,sale):
        self.__sale = sale
    def getId(self):
        return self.__id

    def getDivisaName(self):
        return self.__divisaName

    def getBuy(self):
        return self.__buy

    def getSale(self):
        return self.__sale

    def getPathFileCSV(pathFileConfig):
        with open (pathFileConfig,"r",encoding="UTF-8")as f:
            CSVFilepath = f.readline()
            CSVFilepath = CSVFilepath.strip("\n")
            CSVFilepath =CSVFilepath.strip("\t")
        return CSVFilepath

    @staticmethod
    def DivisaListCreate(pathFileConfig):
        #pathFileCSV = getPathFileCSV(pathFileConfig)
        with open (pathFileConfig,"r",encoding="UTF-8")as f:
            CSVFilepath = f.readline()
            CSVFilepath = CSVFilepath.strip("\n")
            CSVFilepath =CSVFilepath.strip("\t")
        divisas = []
        with open(CSVFilepath,"r",encoding="UTF-8")as f:
            s = f.readline()
            while True:
                s = f.readline()
                if s =="":
                    break # llego al final del archivo
                s = s.strip("\n")
                s = s.split(",")
                d = Divisa(int(s[0]),s[1],s[2],s[3])# creo un objeto divisa
                divisas.append(d)
        return divisas

    @staticmethod 
    def GenerateJson(divisasList):
        key =['id','value1','value2','name']
        dvsList = []
        for item in divisasList:
            d = {}
           
            k = key[0]
            v = int(item.getId())
            d[k]=v
            
            k = key[1]
            v = float(item.getBuy())
            d[k]=v

            k = key[2]
            v = float(item.getSale())
            d[k]=v

            k = key[3]
            v = item.getDivisaName()
            d[k]=v
            dvsList.append(d)
        dvs =json.dumps(dvsList)
        return dvs 

"""
divisa = Divisa.DivisaListCreate("config.txt")
print (divisa)
print("\n")
sendDivisas = Divisa.GenerateJson(divisa)
print (sendDivisas)
print(type(sendDivisas))
"""
