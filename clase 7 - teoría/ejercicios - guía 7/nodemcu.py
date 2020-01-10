"""Este programita debe descargarse en la nodemcu"""
from machine import Pin
import network
import sys
import socket
import os


p0 = Pin(0,Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.isconnected()
wlan.ifconfig()

port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.1.107',port))
while True:
    data,addr = s.recvfrom(512)
    print('recibido:',data.decode('utf-8'),'desde',addr)
    if data.decode('utf-8')== 'OFF':
        p0.off()
    if data.decode('utf-8')== 'ON':
        p0.on()
    