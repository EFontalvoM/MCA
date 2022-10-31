# MCA
Meli Challenge API

#Autor: Eder Fontalvo Melendez

Requerimientos de instalacion: Python 3.7 o superior

Librerias necesarias: pip3 -r requirements.txt

la base de datos ya esta inicializada, pero en caso de requerir prueba desde cero, borrar carpetas: migrations, instance

y ejecutar los siguientes comandos:

flask db init

flask db migrate -m "Initial_db"

flask db upgrade

flask run

El endpoint del API sera publicado en: http://127.0.0.1:5000/api/v1.0/users/
