from utils.db import db

class Usuario(db.Model):
    id_Usuario = db.Column(db.String(20), primary_key=True)
    nombre_apellido = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    contraseña = db.Column(db.String(10))

    def __init__(self, id_Usuario, nombre_apellido, correo, contraseña):
        self.id_Usuario = id_Usuario
        self.nombre_apellido = nombre_apellido
        self.correo = correo
        self.contraseña = contraseña