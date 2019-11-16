class Gpio:
    def __init__(self,n):
        self.__nPin = n
    
    def set_nPin(self,n):
        if n>=0:
            self.__nPin = n   
    def get_nPin(self):
        return self.__nPin

    def set_state (self,b):
        with open("/tmp/gpio_"+str(self.__nPin)+".data","w",encoding="UTF-8")as f:
            if b == False:
                f.write("0\n")
            if b == True:
                f.write("1\n")  
    def get_state(self):
        with open("/tmp/gpio_"+str(self.__nPin)+".data","r",encoding="UTF-8")as f:  
            
            s = f.readline()
            s = s.strip("\n")

            if s == "1":
                return True
            if s == "0":
                return False


