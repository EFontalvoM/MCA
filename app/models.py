import email
from app.db import db, BaseModelMixin

class UsersPrv(db.Model, BaseModelMixin):
    """Modelo para los datos importados desde el proveedor de servicios con el endpoint ajustado para el cumplimiento de seguridad"""
    auto = db.Column(db.String)
    auto_color = db.Column(db.String)
    auto_modelo = db.Column(db.Integer)
    auto_tipo = db.Column(db.Integer)
    avatar = db.Column(db.String)
    cantidad_compras_realizadas = db.Column(db.Integer)
    codigo_zip = db.Column(db.String)
    color_favorito = db.Column(db.Integer)
    credit_card_num_cypher = db.Column(db.String)
    cuenta_numero = db.Column(db.String)
    direccion = db.Column(db.String)
    fec_alta = db.Column(db.String)
    fec_birthday = db.Column(db.String)
    foto_dni = db.Column(db.String)
    geo_latitud = db.Column(db.String)
    geo_longitud = db.Column(db.String)
    ip = db.Column(db.String)
    user_name = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, users):
        self.auto = users["auto"]
        self.auto_color = users["auto_color"]
        self.auto_modelo = users["auto_modelo"]
        self.auto_tipo = users["auto_tipo"]
        self.avatar = users["avatar"]
        self.cantidad_compras_realizadas = users["cantidad_compras_realizadas"]
        self.codigo_zip = users["codigo_zip"]
        self.color_favorito = users["color_favorito"]
        self.credit_card_num_cypher = users["credit_card_num_cypher"]
        self.cuenta_numero = users["cuenta_numero"]
        self.direccion = users["direccion"]
        self.fec_alta = users["fec_alta"]
        self.fec_birthday = users["fec_birthday"]
        self.foto_dni = users["foto_dni"]
        self.geo_latitud = users["geo_latitud"]
        self.geo_longitud = users["geo_longitud"]
        self.user_name = users["user_name"]
        self.id = users["id"]

    def __repr__(self) -> str:
        return f'UsersPrv({self.cantidad_compras_realizadas})'

    def __str__(self) -> str:
        return f'{self.cantidad_compras_realizadas}'

class agent(db.Model, BaseModelMixin):
    """Modelo para la tabla de los agentes que pueden consumir el API con datos publicos y datos privados en MAC"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, index=True, unique=True)
    apiKey = db.Column(db.String)
    perfil = db.Column(db.Integer, db.ForeignKey('perfiles.id'))

class perfiles(db.Model, BaseModelMixin):
    """Modelo para la tabla de los perfiles de los agentes que pueden consumir el API con datos publicos y datos privados en MAC"""
    id = db.Column(db.Integer, primary_key=True)
    nombrePerfil = db.Column(db.String, nullable=False)
    agentId= db.relationship('agent', backref='nombrePerfil', lazy='dynamic')

