class Lampara:
    def __init__ (self, id,name, ip, status):
        self.id = id
        self.name = name
        self.ip = ip
        self.status = status

    @staticmethod
    def generar_lista_objeto(lista_de_diccionario):
        lista_obj=[]
        for item in lista_de_diccionario:
            for k,v in item.items():
                if k == "id":
                    valor_id = v
                if k == "name":
                    valor_name = v
                if k == "ip":
                    valor_ip = v
                if k == "state":
                    valor_state = v
            l = Lampara(valor_id,valor_name,valor_ip,valor_state)
            lista_obj.append(l)           
        return lista_obj
        
    @staticmethod #identifico cual lampara fue modificada ON, OFF
    def comparar_obj_de_lista(lis_act,lis_ant):
        lis =[]
        for item_act in lis_act:
            for item_ant in lis_ant:
                if item_act.id == item_ant.id:
                    if item_act.status!= item_ant.status:
                        print("Enviar:",item_act.status)
                        print(item_act.name)
                        #crear una lista de tuplas con la ip y estado
                        t=(item_act.ip,item_act.status)
                        lis.append(t)
        return lis                