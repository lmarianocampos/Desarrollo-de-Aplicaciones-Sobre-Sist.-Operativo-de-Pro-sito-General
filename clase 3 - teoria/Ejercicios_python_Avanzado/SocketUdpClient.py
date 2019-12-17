from socket import *

class ClientUDP():
    
    def __init__(self,port):
        # creamos un socket y especificamos el tipo de protocolo UDP
        self.client_socket =  socket(AF_INET,SOCK_DGRAM)
        #establecemos ip y puerto del servidor    
        self.server_address = ('localhost',port)
        self.client_socket.settimeout(1)

    def send__message(self,message):
        self.client_socket.sendto(message.encode('UTF-8'),self.server_address)
        
    def receive_message(self):    
        value = False
        try:
            #aqui quedara boqueado hasta recivir una respuesta del servidor
            data, server = self.client_socket.recvfrom(128)
            data = data.decode('utf-8')
            if data == "OK":
                value = True
        except timeout:
            print ("REQUEST TIMED OUT")
        return value
    def sock_close(self):
        self.client_socket.close()
        