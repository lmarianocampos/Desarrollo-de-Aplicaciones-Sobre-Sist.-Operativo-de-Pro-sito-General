from socket import *
from divisas import *
import time
import sys
from signal import *

class main:
    def __init__(self):
        pass
    def main(self):
        #definimos el manejador de la señal SIGINT
        signal(SIGINT,handler)
        # creamos un socket y especificamos el tipo de protocolo UDP
        clientSocket =  socket(AF_INET,SOCK_DGRAM)
        #establecemos ip y puerto del servidor    
        serverAddress = ('localhost',10000)

        while True:
                time.sleep(5)
                #leer el archivo mediante la función 
                #esto me devuelve una lista 
                divisa = Divisa.DivisaListCreate("config.txt")
                print ("leyendo archivo")
                #convierto la lista a JSON
                sendDivisas = Divisa.GenerateJson(divisa)
                # envío al servidor el mensaje
                try:
                    print(sendDivisas)
                    clientSocket.sendto(sendDivisas.encode('UTF-8'),serverAddress)        
                    #aqui quedara boqueado hasta recivir una respuesta del servidor
                    data, server = clientSocket.recvfrom(512)
                    print (data)
                except:
                    print("Closing socket")
                    clientSocket.close()
    #def handler()

m = main()
m.main()
