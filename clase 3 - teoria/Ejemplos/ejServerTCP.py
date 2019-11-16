#!/usr/bin/python3

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(server_address[0],server_address[1]))

sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from {} {}'.format(client_address[0],client_address[1]))

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print(data)
            print(data.hex())
            if len(data)>0:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from {} {}'.format(client_address[0],client_address[1]))
                break

    finally:
        # Clean up the connection
        connection.close()

