from flask_login import UserMixin
from utils.db import db
from werkzeug.security import check_password_hash, generate_password_hash


class Plato(db.Model, UserMixin):
    id_Plato = db.Column(db.String(20), primary_key=True)
    cantidad = db.Column(db.Integer)

    def __init__(self, id_Plato,cantidad):
        self.id_Plato = id_Plato
        self.cantidad = cantidad
