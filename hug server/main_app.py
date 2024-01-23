import requests
import uuid
import datetime

myuuid =uuid.uuid1()
data = requests.get("http://localhost:8000/validar?num=" +  str(myuuid).split('-')[4])  
print(data.json())