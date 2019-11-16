def receiveString( message, c):
    return message.replace(" ",c)

mess = input("Ingrese un Mensaje: ")
character = input("Ingrese un Caracter: ")
messa = receiveString(mess, character)
print (messa)