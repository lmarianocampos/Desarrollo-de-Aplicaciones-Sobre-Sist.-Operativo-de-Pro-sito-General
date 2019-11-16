#!/usr/bin/python3

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(server_address[0],server_address[1]))

sock.connect(server_address)

try:

    # Send data
    message = bytearray()
    message.append(0x02)
    message.append(0x30)
    message.append(0x31)
    message.append(0xFF)

    print(message.hex())
    sock.sendall(message)

    # Look for the response
    data = sock.recv(1024)
    print(type(data))
    print(data.hex())

finally:
    print('closing socket')
    sock.close()
