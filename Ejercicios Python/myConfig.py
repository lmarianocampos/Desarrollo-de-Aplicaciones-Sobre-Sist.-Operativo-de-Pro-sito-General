def readFileConfig(nameFile):
    with open (nameFile,"r", encoding="UTF-8") as f:
        while True:
            s = f.readline()
            if s == "":
                break
            s = s.strip("\n")
            print (s)

def writeFileConfig(nameFile, s):
    with open (nameFile,"a",encoding="UTF-8") as f:
        f.write(s+"\n")