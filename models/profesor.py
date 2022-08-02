from utils.db import db


class Tarea(db.Model):
    id_tarea = db.Column(db.Integer, primary_key=True)
    id_Usuario = db.Column(db.String(20), db.ForeignKey('usuario.id_Usuario'))
    fecha = db.Column(db.Integer)
    mes = db.Column(db.Integer)
    dia = db.Column(db.String(50))
    hora = db.Column(db.String(50))

    def __init__(self, id_Usuario):
        self.id_Usuario = id_Usuario