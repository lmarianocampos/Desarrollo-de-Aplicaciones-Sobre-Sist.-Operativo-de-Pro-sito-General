import threading
import time
import signal
from divisas import Divisa
from SocketUdpClient import ClientUDP

class PService(threading.Thread):
    def __init__(self):
        super().__init__()
        self.shutdown_flag = threading.Event()
       
    def run(self):
        c_sock = ClientUDP(10000)     
        print('Thread Socket Client #%s started' % self.ident)
        
        while not self.shutdown_flag.is_set():            
            #leer el archivo mediante la función 
            #esto me devuelve una lista 
            divisa = Divisa.divisa_list_create("config.txt")
            #convierto la lista a JSON
            send_divisas = Divisa.generate_json(divisa)
            #envío al servidor el mensaje
            c_sock.send__message(send_divisas)
            value = c_sock.receive_message() 
            if value == True:
                print("OK")
            self.shutdown_flag.wait(30)  
           
        print ("Socket Cliente Closed")
        c_sock.sock_close()
        print('Thread Socket Client #%s Stopped' % self.ident)

class ServiceExit(Exception):
    pass

def service_shutdown(signal_receive,frame):
    print ("captured signal(Crtl+C):%d"% signal_receive)
    raise ServiceExit()

def main():
    signal.signal(signal.SIGINT,service_shutdown)
    print ("starting the main program")

    try:
        pS1= PService()
        pS1.start()

        while True:
            time.sleep(0.5)
    except ServiceExit:

        pS1.shutdown_flag.set()
        pS1.join()
        
    print ("finishing the main program")
main()
    