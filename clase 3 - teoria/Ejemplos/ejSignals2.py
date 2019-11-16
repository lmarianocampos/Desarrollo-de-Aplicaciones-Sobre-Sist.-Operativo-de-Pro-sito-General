#!/usr/bin/python3
import signal  
import time
import traceback


class Main:

    def main(self):
        signal.signal(signal.SIGINT, self.handler)  # hacerlo en el thread ppal. El handler siempre se ejecuta en el thread ppal.

        while True:  
            print("Press ctrl + c")  # Espera por SIGINT  
            time.sleep(10) 

    def print_msg(self):
        print("Hola")

    def handler(self,sig, frame):  # define the handler  
        print("Signal Number:", sig, " Frame: ", frame)  
        traceback.print_stack(frame)	
        self.print_msg()


#Inicio del programa
m = Main()
m.main()


  
  

