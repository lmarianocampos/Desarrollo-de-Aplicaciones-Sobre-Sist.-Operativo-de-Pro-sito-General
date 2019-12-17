"""
	Ejemplo archivos
	https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
"""

import io

try:
	with open("archivoBin.txt","wb") as f: #si pongo wb, puedo pasarle un bytearray
		ba = bytearray()
		ba.append(0x30)
		ba.append(0x31)
		ba.append(0x32)
		f.write(ba)
	#el archivo se cierra al terminar el bloque with aunque exista una exception


	with open("archivoText.txt","w",encoding="utf-8") as f: #si pongo w, puedo pasarle un string
		s="012"
		f.write(s)
	#el archivo se cierra al terminar el bloque with aunque exista una exception


	with open("archivoBin.txt","rb") as f:
		#ba = f.read(64)
		ba = f.read() #leo todo
		print(ba)
	#el archivo se cierra al terminar el bloque with aunque exista una exception


	with open("archivoText.txt","r",encoding="utf-8") as f:
		#s = f.read()
		s = f.readline()
		print(s)
	#el archivo se cierra al terminar el bloque with aunque exista una exception



except io.UnsupportedOperation as e:
	print("No tengo permisos de escritura")
	print(e)
except FileNotFoundError as e:
	print("Archivo no existe")
	print(e)
