#!/usr/bin/python3

from threading import Thread
import time

class MyThread (Thread):

    def __init__(self, name, counter):
        super().__init__()  #Thread.__init__(self)
        self.name = name
        self.counter = counter

    def run(self):
        print ("Comienza thread:"+self.name)
        while self.counter:
            time.sleep(1)
            print ("%s: %s" % (self.name, time.ctime(time.time())))
            self.counter -= 1

        print ("Saliendo de:"+self.name)


    
# Creamos nuevos threads
thread1 = MyThread("Thread-1", 3)
thread2 = MyThread("Thread-2", 5)

# Iniciamos threads y esperamos que terminen
thread1.start()
thread2.start()

print("Espero finalizacion...")
thread1.join()
thread2.join()
print ("Termino el proceso")

