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
    urlProvider = "https://635c5873f0bc26795bfd88d1.mockapi.io/api/v2/usuarios"
    postDataRequest = requests.post(urlProvider, json = data)
    print("id: {0} Estado: {1}".format(data["id"], postDataRequest.status_code))
    sleep(espera)

    
