import requests
import time
import json
from Lampara import Lampara


URL="http://localhost:5000/devices"
r_anterior = requests.get(url=URL)
if r_anterior.status_code == 200:
    #obtengo una lista de diccionario
    l_anterior = json.loads(r_anterior.text)
    while True:
        URL="http://localhost:5000/devices"
        r_actual = requests.get(url=URL)
        if r_actual.status_code == 200:
            #obtengo una lista de diccionario
            l_actual = json.loads(r_actual.text)
             
            if l_actual == l_anterior:
                print("No hay modificación")
            else:
                print("Se modifico el estado de una lampara")
                # debo identificar que lampara cambio de estado 
                # genero una lista de objetos Lamparas               
                lis_ant = Lampara.generar_lista_objeto(l_anterior)
                lis_act = Lampara.generar_lista_objeto(l_actual)
                Lampara.comparar_obj_de_lista(lis_act,lis_ant)
            l_anterior = l_actual    
        else:
            print("error code:"+str(r_actual.status_code))
        time.sleep(1)