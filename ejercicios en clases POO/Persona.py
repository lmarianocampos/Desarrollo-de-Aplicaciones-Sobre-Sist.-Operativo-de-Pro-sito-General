class Persona:
    def __init__(self):
        self.__nombre = ""
        self.__edad = 0

    def set_nombre(self,nombre):
        self.__nombre = nombre   

    def get_nombre (self): 
        return self.__nombre

    def set_edad(self,edad):
        self.__edad = edad    

    def get_edad(self):
        return self.__edad  

    def es_mayor_de_edad(self):
        if self.__edad >= 18:
            return True
        else:
            return False

    def imprimir_mayores_menores(self,lista_persona) 
