def generateFile(dictionary, fileName):

    with open(fileName,"w", encoding="UTF-8") as f:
        for k, v in dictionary.items():
            f.write(k +"="+ v+"\n")

d = {'Mariano': '37','Patricio' : '27', 'Jack': '4098'}
generateFile(d, "Archivo_Diccionario.txt")

