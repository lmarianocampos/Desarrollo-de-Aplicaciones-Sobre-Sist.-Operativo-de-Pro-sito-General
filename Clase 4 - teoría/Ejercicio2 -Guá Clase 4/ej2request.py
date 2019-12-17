import requests
import time
while True:
    URL = "http://localhost:8001/cgi-bin/sensors.py"
    r = requests.get(url = URL)
    if r.status_code == 200:
        print(r.text)
    else: 
        print ("error code:"+str(r.status_code))    
    time.sleep(5)