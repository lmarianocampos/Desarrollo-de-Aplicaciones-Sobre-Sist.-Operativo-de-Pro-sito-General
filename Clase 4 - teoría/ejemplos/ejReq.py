import requests

#https://www.mocky.io/

#URL = "http://localhost:8080/cgi-bin/index.py"
URL = "http://www.mocky.io/v2/5d797547320000600034ea2b"


r = requests.get(url = URL) 

if r.status_code==200:
    print(r.text)
else:
    print("error code:"+str(r.status_code))

