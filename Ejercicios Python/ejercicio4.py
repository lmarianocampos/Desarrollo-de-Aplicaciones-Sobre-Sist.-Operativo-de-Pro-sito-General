def esPar(valor):
    if ((valor % 2) == 0):
        return True
    else:
        return False

numero = input("Ingre un número: ")
#print (numero)
num = int(numero)
#par = esPar(num)
if esPar(num):
    print(numero + " Es par")
else: 
    print (numero + " Es Impar") 


