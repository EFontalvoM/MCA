import json
from cryptography.fernet import Fernet

def genera_clave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)
def cargar_clave():
    return open("clave.key","rb").read()

def cargar_data():
    return open("usuarios.json")
usuariosProcesados = []

clave = cargar_clave()
cifradoAES = Fernet(clave)
usuariosArchivo = cargar_data()
usuarios = json.load(usuariosArchivo)

#tarjeta = cargar_tarjeta()
#mensaje = tarjeta.encode()

for i in usuarios:
    i["credit_card_num_cypher"] = cifradoAES.encrypt(str(i["credit_card_num"]).encode()).decode()
    i["cuenta_numero"] = cifradoAES.encrypt(str(i["cuenta_numero"]).encode()).decode()
    i["foto_dni"] = cifradoAES.encrypt(str(i["foto_dni"]).encode()).decode()
    i["geo_latitud"] = cifradoAES.encrypt(str(i["geo_latitud"]).encode()).decode()
    i["geo_longitud"] = cifradoAES.encrypt(str(i["geo_longitud"]).encode()).decode()
    i["user_name"] = cifradoAES.encrypt(str(i["user_name"]).encode()).decode()
    del i["credit_card_ccv"]
    del i["credit_card_num"]
    usuariosProcesados.append(i)

with open('usuariosProcesados.json', 'w') as f:
    json.dump(usuariosProcesados, f)

    

#encriptar = f.encrypt(tarjeta)
#print(tarjeta.decode())
#desencriptar = f.decrypt(tarjeta)
#print(desencriptar.decode())