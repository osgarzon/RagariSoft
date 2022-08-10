from utils.db import db


class Tarea(db.Model):
    id_tarea = db.Column(db.String(20), primary_key=True)
    id_Usuario = db.Column(db.String(20), db.ForeignKey("usuario.id_Usuario"))
    id_materia = db.Column(db.String(20), db.ForeignKey("materia.id_materia"))
    id_profesor = db.Column(db.String(20), db.ForeignKey("profesor.id_profesor"))
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)
    descripcion = db.Column(db.Text)

    def __init__(
        self, id_tarea, id_Usuario, id_materia, id_profesor, fecha, hora, descripcion
    ):
        self.id_tarea = id_tarea
        self.id_Usuario = id_Usuario
        self.id_materia = id_materia
        self.id_profesor = id_profesor
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion
