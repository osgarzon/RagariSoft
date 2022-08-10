from flask_login import UserMixin
from utils.db import db
from werkzeug.security import check_password_hash, generate_password_hash


class Usuario(db.Model, UserMixin):
    id_Usuario = db.Column(db.String(20), primary_key=True)
    nombre_apellido = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    contraseña = db.Column(db.String(10))

    def __init__(self, id_Usuario, nombre_apellido, correo, contraseña):
        self.id_Usuario = id_Usuario
        self.nombre_apellido = nombre_apellido
        self.correo = correo
        self.contraseña = contraseña

    @classmethod
    def check_pass(self, hashpass, password):
        return check_password_hash(hashpass, password)

    def get_id(self):
        return self.id_Usuario
