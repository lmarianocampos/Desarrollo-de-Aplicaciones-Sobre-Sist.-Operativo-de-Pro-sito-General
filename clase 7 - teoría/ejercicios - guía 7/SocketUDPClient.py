from socket import *
class ClientUDP:
    def __init__(self, ip, port):
        
        self.client_socket = socket(AF_INET,SOCK_DGRAM)
        self.server_address = (ip,port)
        self.client_socket.settimeout(1)

    def send_message(self,message):
        self.client_socket.sendto(message.encode('UTF-8'),self.server_address)
    
    def sock_close(self):
        self.client_socket.close()
             
        
