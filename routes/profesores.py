from flask import Blueprint
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required
from models.profesor import Profesor
from models.tarea import Tarea
from routes.horarios import horarios
from utils.db import db


profesores = Blueprint("profesor", __name__)


@profesores.route("/creaprofesor")
@login_required
def creaProfesor():
    return render_template("/crearprofesor.html")


@profesores.route("/obtenerProfesor", methods=["POST"])
def registrar():
    id_profesor = request.form["id_profesor"]
    descripcion = request.form["descripcion"]

    profesor = Profesor(id_profesor, descripcion)
    db.session.add(profesor)
    db.session.commit()

    flash("profesor registrado")
    return redirect(url_for("horarios.principal"))

@profesores.route("/eliminarProfesor", methods=["POST"])
@login_required
def delete():
    profesor = request.form["profesor"]
    print("LA TAREA ES:   ",profesor)
    profesor = Profesor.query.get(profesor)
    db.session.delete(profesor)
    db.session.commit()

    flash("Profesor eliminado")
    return redirect(url_for("horarios.principal"))

@profesores.route("/actualizarProfesor", methods=["POST"])
@login_required
def update():
    tarea = request.form["tarea"]
    tarea = Tarea.query.get(tarea)

    tarea.id_profesor = request.form["profesor"]
    
    db.session.commit()

    flash("Actualización exitosa")
    return redirect(url_for("horarios.principal"))