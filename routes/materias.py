from pyexpat import model
from flask import Blueprint
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required
from models.materia import Materia
from models.tarea import Tarea
from routes.horarios import horarios
from utils.db import db



materias = Blueprint("materia", __name__)


@materias.route("/creamateria")
@login_required
def creaMateria():
    return render_template("/crearmateria.html")


@materias.route("/obtenerMateria", methods=["POST"])
@login_required
def registrar():
    id_materia = request.form["id_materia"]
    creditos = request.form["creditos"]

    materia = Materia(id_materia, creditos)
    db.session.add(materia)
    db.session.commit()

    flash("materia creada")
    return redirect(url_for("horarios.principal"))


@materias.route("/eliminarMateria", methods=["POST"])
@login_required
def delete():
    materia = request.form["materia"]
    materia = Materia.query.get(materia)
    db.session.delete(materia)
    db.session.commit()

    flash("Materia eliminada")
    return redirect(url_for("horarios.principal"))

@materias.route("/actualizarMateria", methods=["POST"])
@login_required
def update():
    tarea = request.form["tarea"]
    print("TAREA ES:     ",tarea)
    tarea = Tarea.query.get(tarea)

    tarea.id_materia = request.form["materia"]
    
    db.session.commit()

    flash("Actualización exitosa")
    return redirect(url_for("horarios.principal"))