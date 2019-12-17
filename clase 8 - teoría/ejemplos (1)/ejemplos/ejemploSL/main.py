from ctypes import CDLL

mylib = CDLL("./libbiblioteca.so")

resultado = mylib.bib_calcularSuma(10,45)

print(resultado)

