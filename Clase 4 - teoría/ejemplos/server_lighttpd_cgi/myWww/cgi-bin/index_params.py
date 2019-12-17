import cgi

#probar: http://localhost:8080/cgi-bin/index_params.py?p1=hola&p2=mundo

arguments = cgi.FieldStorage()
for i in arguments.keys():
    print(arguments[i].value)

