import json
import requests
from time import sleep
def cargar_data():
    return open("usuariosProcesados.json")
usuariosProcesados = []
usuariosArchivo = cargar_data()
usuarios = json.load(usuariosArchivo)
espera = 2
for data in usuarios:
    urlProvider = "http://127.0.0.1:5000/api/v1.0/users/"
    postDataRequest = requests.post(urlProvider, json = data)
    print("id: {0} Estado: {1}".format(data["id"], postDataRequest.status_code))
    sleep(espera)

    
