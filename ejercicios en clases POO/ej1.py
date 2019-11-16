from Persona import Persona

print ("Prueba clase Persona")
p = Persona()
p.set_nombre("Mariano") 
p.set_edad(37)

#print (p.nombre +"edad:"+ str(p.edad))
print ("{0} edad: {1}".format(p.get_nombre(),p.get_edad()))
print(type(p))
