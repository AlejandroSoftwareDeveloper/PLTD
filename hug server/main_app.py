import requests
import uuid
import datetime


myuuid = str(uuid.uuid1()).split('-')[4]

data = requests.get("http://localhost:8000/validar?uuid=" + myuuid)  
print(data.json())