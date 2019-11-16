class Persona:
    __nombre = ""
    __edad = 0

    def __init__(self, nombre, edad):
        self.set_nombre(nombre)
        self.set_edad(edad)

    def set_nombre(self,nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_edad(self,edad):
        if edad>=0 and edad<=99:
            self.__edad = edad

    def get_edad(self):
        return self.__edad

    def es_mayor_de_edad(self):
        if self.__edad>=18:
            return True
        else:
            return False
    def es_mayor_que(self,otraPersona):
        if self.__edad >otraPersona.get_edad():
            return True
        else:
            return False

    @staticmethod
    def es_mayor(per1,per2):
        if per1.get_edad() > per2.get_edad():
            return per1
        if per1.get_edad() == per2.get_edad():
            return 
        else:
            return per2

    @staticmethod
    def dump_csv(fileName,personList):
        if personList:#si no esta vacia la lista de persona devuelve TRUE
            with open(fileName,"w",encoding="UTF-8") as f:
                f.write("Nomre,edad\n")
                for item in personList:
                    s = "{0},{1}\n".format(item.get_nombre(),item.get_edad())
                    f.write(s)

    @staticmethod
    def load_csv(fileName):
        personList =[]
        with open(fileName,"r",encoding="UTF-8")as f:
            s = f.readline()
            while True:
                s=f.readline()
                if s=="":
                    break  #sale porque llego al final del archivo
                s = s.strip("\n")
                s = s.split(",") 
                name = s[0]
                age = int(s[1])
                p = Persona(name,age)
                personList.append(p)
        return personList
                #print(s)  

    def print_persona(self):
        print("Nombre: "+ self.__nombre + "\n Edad: "+str(self.__edad) )
