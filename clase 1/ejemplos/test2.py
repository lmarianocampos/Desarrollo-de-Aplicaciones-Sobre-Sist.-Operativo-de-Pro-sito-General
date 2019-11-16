class Usuario:
	def __init__(self,nombre,dni):
		self.nombre=nombre
		self.dni=dni


users = []
for i in range(0,1000000):
	users.append(Usuario("Ernesto",33263106))


