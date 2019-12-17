import requests

URL = "http://localhost:8080/cgi-bin/index.py"
PARAMS = {"clave1":"valor1","clave2":"valor2",} 

r = requests.get(url = URL, params = PARAMS) 

if r.status_code==200:
    print(r.text)
else:
    print("error code:"+str(r.status_code))

