from utils.db import db


class Materia(db.Model):
    id_materia = db.Column(db.String(20), primary_key=True)
    creditos = db.Column(db.Integer)

    def __init__(self, id_materia, creditos):
        self.id_materia = id_materia
        self.creditos = creditos
