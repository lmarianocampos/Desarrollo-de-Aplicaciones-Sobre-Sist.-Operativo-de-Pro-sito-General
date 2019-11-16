def generateDictionary(fileName):
    d ={}
    with open(fileName,"r", encoding = "UTF-8") as f:
        while True:
            s = f.readline()

            if s == "":
                break # es el final del archivo
            s = s.strip ("\n")
            s = s.split("=")
            k = s[0]
            v = s[-1]
            d[k]=v
           # print (s)
           # print (k)
           # print (v)
           # print (d)
    return d
print(generateDictionary("config.txt"))
