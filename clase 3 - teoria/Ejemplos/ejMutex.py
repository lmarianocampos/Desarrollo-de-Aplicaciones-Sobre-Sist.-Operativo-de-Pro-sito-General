#!/usr/bin/python3

import threading
import time

class MyThread (threading.Thread):

    varCompartida=0
    threadLock = threading.Lock()

    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter

    def run(self):
        print ("Comienza thread:"+self.name)
        while self.counter:
            time.sleep(1)
            
            MyThread.threadLock.acquire()
            MyThread.varCompartida+=1
            print ("%s: %s" % (self.name, MyThread.varCompartida))
            MyThread.threadLock.release()

            self.counter -= 1

        print ("Saliendo de:"+self.name)


    
# Creamos nuevos threads
thread1 = MyThread("Thread-1", 3)
thread2 = MyThread("Thread-2", 5)

# Iniciamos threads y esperamos que terminen
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Termino el proceso")

