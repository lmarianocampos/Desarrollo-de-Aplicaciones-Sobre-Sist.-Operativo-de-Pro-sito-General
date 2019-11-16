def calcularCuadrado(x):
	return x*x

numeros = range(0,10000000)
salida = []

#for n in numeros:
#	salida.append(calcularCuadrado(n))
salida = map(calcularCuadrado,numeros)


#print(numeros)
#for n in salida:
#	print(n)



