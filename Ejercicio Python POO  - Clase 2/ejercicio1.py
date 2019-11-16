from persona import Persona

p1 = Persona("Mariano",37)
p2 = Persona("Patricio",27)
p1.print_persona() 
p2.print_persona() 

if p1.es_mayor_de_edad():
    print(p1.get_nombre()+" Es Mayor de Edad\n")
else:
    print(p1.get_nombre()+" No es Mayor de Edad\n ")  

if p2.es_mayor_de_edad():
    print(p2.get_nombre()+" Es Mayor de Edad\n")
else:
    print(p2.get_nombre()+" No es Mayor de Edad\n  ")  

if p1.es_mayor_que(p2):
    print (p1.get_nombre()+" Es Mayor que "+p2.get_nombre())
else:
    print (p1.get_nombre()+"No Es Mayor que"+p2.get_nombre())

pMayor = Persona.es_mayor(p1,p2)
print(pMayor.get_nombre()+" Es Mayor  ")
personas =[]
personas.append(p1)
personas.append(p2)
personas.append(Persona("juan",34))
personas.append(Persona("carlos",16))
personas.append(Persona("Ernesto",39))
#print(personas)
Persona.dump_csv("personas.csv",personas)
pList = Persona.load_csv("personas.csv")
print(pList)
