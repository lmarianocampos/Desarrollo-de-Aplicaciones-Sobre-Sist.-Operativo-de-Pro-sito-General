#!/usr/bin/python3
import signal  
import time
import traceback


def handler(sig, frame):  # define the handler  
    print("Signal Number:", sig, " Frame: ", frame)  
    traceback.print_stack(frame)	

  
signal.signal(signal.SIGINT, handler)  # hacerlo en el thread ppal. El handler siempre se ejecuta en el thread ppal.
  
while True:  
    print("Press ctrl + c")  # Espera por SIGINT  
    time.sleep(10) 

