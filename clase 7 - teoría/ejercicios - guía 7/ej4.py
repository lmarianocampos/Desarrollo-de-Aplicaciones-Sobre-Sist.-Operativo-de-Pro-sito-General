from Lampara import Lampara
from SocketUDPClient import ClientUDP
import requests
import time
import json
import signal
import threading



class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.shutdwon_flag = threading.Event()
    def run(self):

        URL="http://localhost:5000/devices"
        r_anterior = requests.get(url=URL)
        if r_anterior.status_code == 200:
            #obtengo una lista de diccionario
            l_anterior = json.loads(r_anterior.text)
        l = []
        while not self.shutdwon_flag.is_set():
            URL="http://localhost:5000/devices"
            r_actual = requests.get(url=URL)
            if r_actual.status_code == 200:
                #obtengo una lista de diccionario
                l_actual = json.loads(r_actual.text)
                #verifico si se realizaron cambios de estados en las lamparas
                if l_actual == l_anterior:
                    print("No hay modificación")
                else:
                    print("Se modifico el estado de una lampara")
                    # debo identificar que lampara cambio de estado 
                    # genero una lista de objetos Lamparas               
                    lis_ant = Lampara.generar_lista_objeto(l_anterior)
                    lis_act = Lampara.generar_lista_objeto(l_actual)
                    l = Lampara.comparar_obj_de_lista(lis_act,lis_ant)
                    if l:
                        
                        for item in l:
                            print (item[0])#es la ip
                            print (item[1])
                            client_udp = ClientUDP(item[0],80)
                            if item[1] == 1:
                                client_udp.send_message("ON")
                                print("Encender lampara")
                            if item[1] == 0:
                                client_udp.send_message("OFF")
                                print("Apagar lampara")
                            # aqui deberia esperar una respuesta del servidor 
                            client_udp.sock_close() 
                            #print (type(item[0]))
                            #print (type(item[1]))
                            
                            
                    #recorrer la lista de tuplas  "l" y enviar los paquetes UDP
                    
                l_anterior = l_actual    
            else:
                print("error code:"+str(r_actual.status_code))
            self.shutdwon_flag.wait(1)
class ServiceExit(Exception):
    pass

def service_shutdwon(signal_receive,frame):
    print("Señal capturada Ctrl+c:%d"%signal_receive)
    raise ServiceExit()

def main():
    signal.signal(signal.SIGINT,service_shutdwon)
    print("Comienzo del programa Main()")
    try: 
        t1 = MyThread()
        t1.start()
        while True:
            time.sleep(0.5)
    except ServiceExit:
        t1.shutdwon_flag.set()
        t1.join()
    print("finalizando el programa Main()")
main()