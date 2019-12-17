def dump_csv(data_list,file_name):
    #Abrimos archivo usando open y la sentencia "with"
    # Ver https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    with open(file_name,"w",encoding="utf-8") as fp:
        fp.write("Name,Address,Age\n") #escribimos cabecera
        #escribimos lineas de datos
        for item in data_list:
            lin = "{0},{1},{2}\n".format(item[0],item[1],item[2])
            #print(lin)
            #escribir cada linea en el archivo
            fp.write(lin)


#Inicio de mi programa
data =  [('George', '4312 Abbey Road',22), ('John','54 LoveAve', 21)]

#Ejecuto la funcion
dump_csv(data,"archivo.csv")

