import threading
import time
import signal
from divisas import Divisa
from socket import *

class PService(threading.Thread):
    def __init__(self):
        super().__init__()
        self.shutdown_flag = threading.Event()
       
    def run(self):
         # creamos un socket y especificamos el tipo de protocolo UDP
        clientSocket =  socket(AF_INET,SOCK_DGRAM)
        #establecemos ip y puerto del servidor    
        serverAddress = ('localhost',10000)
        
        print('Thread Socket Client#%s started' % self.ident)
        
        while not self.shutdown_flag.is_set():
            time.sleep(5)
            #leer el archivo mediante la función 
            #esto me devuelve una lista 
            divisa = Divisa.DivisaListCreate("config.txt")
            print ("leyendo archivo")
            #convierto la lista a JSON
            sendDivisas = Divisa.GenerateJson(divisa)
            # envío al servidor el mensaje
            print(sendDivisas)
            try:
                clientSocket.sendto(sendDivisas.encode('UTF-8'),serverAddress)        
                #aqui quedara boqueado hasta recivir una respuesta del servidor
                data, server = clientSocket.recvfrom(512)
                print (data)
            except:
                raise ServiceExit()
                #clientSocket.close()
        print ("Socket Cliente Closed")
        clientSocket.close()    
        print('Thread Socket Client#%s Stopped' % self.ident)

class ServiceExit(Exception):
    pass

def ServiceShutdown(signalReceive,frame):
    print ("Señal Capurada(Crtl+C):%d"% signalReceive)
    raise ServiceExit()

def main():
    signal.signal(signal.SIGINT,ServiceShutdown)
    print ("Iniciando el programa Main()")

    try:
        pS1= PService()
        pS1.start()

        while True:
            time.sleep(0.5)
    except ServiceExit:

        pS1.shutdown_flag.set()
        pS1.join()
        
    print ("Finalizando el programa Main()")
main()
    