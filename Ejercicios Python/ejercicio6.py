def generateFile_csv (dataList,nameFile):
    with open (nameFile,"w",encoding = "UTF-8") as f:
        f.write("Name,Address,Age\n")
        for item in dataList:
            lin = "{0},{1},{2}\n".format(item[0],item[1],item[2])
            f.write(lin)

list =[('George', '4312 Abbey Road',22),('John','54 LoveAve', 21),('Mariano','gorriti 480',37)]
generateFile_csv(list,"file.csv")
 