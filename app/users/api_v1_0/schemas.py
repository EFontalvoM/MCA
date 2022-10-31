from marshmallow import fields

from app.ext import ma


class usersSchema(ma.Schema):
    auto = fields.String()
    auto_color = fields.String()
    auto_modelo = fields.Integer()
    auto_tipo = fields.Integer()
    avatar = fields.String()
    cantidad_compras_realizadas = fields.Integer()
    codigo_zip = fields.String()
    color_favorito = fields.Integer()
    credit_card_num_cypher = fields.String()
    cuenta_numero = fields.String()
    direccion = fields.String()
    fec_alta = fields.String()
    fec_birthday = fields.String()
    foto_dni = fields.String()
    geo_latitud = fields.String()
    geo_longitud = fields.String()
    ip = fields.String()
    user_name = fields.String()
    id = fields.Integer(dump_only=True)

class agentSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    email = fields.String()
    apiKey = fields.Integer(dump_only=True)
    perfil = fields.String()

class perfiles(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombrePerfil = fields.String()
    

