def CSVfilePathRead(pathConfig):
    with open (pathConfig,"r",encoding="UTF-8")as f:
        CSVFilepath = f.readline()
        
    return CSVFilepath

def ListCreate(pathConf):
    pathCSV = CSVfilePathRead(pathConf)    
    pathCSV = pathCSV.strip("\n")
    pathCSV = pathCSV.strip("\t")   
     
    with open(pathCSV,"r") as f:
        s = f.readline()
        #print(s)
        while True:
            s = f.readline()
            if s == "":
                break #sale porque llego al final del archivo
            s = s.strip("\n")
            s = s.split(",")
            id = s[0]
            nombre = s[1]
            compra = s[2]
            venta  = s[3] 
            print (id)
            print (nombre)
            print (compra)
            print (venta)
            #print (s)
    return s
l = ListCreate("config.txt")  
#print (l)      