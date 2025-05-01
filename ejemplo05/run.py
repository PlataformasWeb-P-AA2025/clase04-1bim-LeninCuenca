import requests
import json

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    data = json.load(f)

base_datos = "tenis005"
url_base = f"http://127.0.0.1:5984/{base_datos}/"
headers = {'Content-Type': 'application/json'}

# Insertar cada documento individualmente
for doc in data['docs']: 
    response = requests.post(url_base, headers=headers, json=doc)
    print(f"Status: {response.status_code}, Response: {response.json()}")
