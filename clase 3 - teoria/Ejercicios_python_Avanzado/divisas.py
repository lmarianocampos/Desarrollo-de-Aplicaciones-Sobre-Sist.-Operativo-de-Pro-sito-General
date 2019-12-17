import json

class Divisa:
    def __init__(self, id, divisa_name,buy,sale):
        self.set_id(id)
        self.set_divisa_name(divisa_name)
        self.set_buy(buy)
        self.set_sale(sale)

    def set_id(self,id):
        if id > 0:
            self.__id = id

    def set_divisa_name(self,divisa_name):
        self.__divisa_name = divisa_name
    
    def set_buy(self,buy):
        self.__buy = buy

    def set_sale (self,sale):
        self.__sale = sale
    def get_id(self):
        return self.__id

    def get_divisa_name(self):
        return self.__divisa_name

    def get_buy(self):
        return self.__buy

    def get_sale(self):
        return self.__sale

    @staticmethod 
    def get_path_file_csv(path_file_config):
        try:
            with open (path_file_config,"r",encoding="UTF-8")as f:
                csv_file_path = f.readline()
                csv_file_path = csv_file_path.strip("\n")
                csv_file_path = csv_file_path.strip("\t")
        except IOError:
            print("error accessing file Config.txt")
        return csv_file_path

    @staticmethod
    def divisa_list_create(path_file_config):
        divisas = []
        csv_file_path = Divisa.get_path_file_csv(path_file_config)
        try :
            with open(csv_file_path,"r",encoding="UTF-8")as f:
                s = f.readline()
                while True:
                    s = f.readline()
                    if s =="":
                        break # llego al final del archivo
                    s = s.strip("\n")
                    s = s.split(",")
                    d = Divisa(int(s[0]),s[1],s[2],s[3])# creo un objeto divisa
                    divisas.append(d)
        except IOError:
            print("error accessing file file.csv")
        return divisas

    @staticmethod 
    def generate_json(divisas_list):
        key =['id','value1','value2','name']
        dvs_list = []
        for item in divisas_list:
            d = {}
           
            k = key[0]
            v = int(item.get_id())
            d[k]=v
            
            k = key[1]
            v = float(item.get_buy())
            d[k]=v

            k = key[2]
            v = float(item.get_sale())
            d[k]=v

            k = key[3]
            v = item.get_divisa_name()
            d[k]=v
            dvs_list.append(d)
        dvs =json.dumps(dvs_list)
        return dvs 


