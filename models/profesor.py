from utils.db import db


class Profesor(db.Model):
    id_profesor = db.Column(db.String(20), primary_key=True)
    descipcion = db.Column(db.Text)

    def __init__(self, id_profesor, descripcion):
        self.id_profesor = id_profesor
        self.descipcion = descripcion
