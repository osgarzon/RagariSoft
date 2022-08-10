from flask import Blueprint
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required
from models.tarea import Tarea
from models.profesor import Profesor
from models.materia import Materia
from models.usuario import Usuario
from utils.db import db
import tkinter as tk
from flask_login import current_user


tareas = Blueprint("tareas", __name__)


@tareas.route("/creatarea")
@login_required
def creaTarea():
    usuariosdb = Usuario.query.all()
    profesoresdb = Profesor.query.all()
    materiasdb = Materia.query.all()
    return render_template(
        "/creartarea.html",
        usuariosdb=usuariosdb,
        profesoresdb=profesoresdb,
        materiasdb=materiasdb,
    )


@tareas.route("/obtenerTarea", methods=["POST"])
@login_required
def obtenerTarea():
    nombre = request.form["nombre"]
    usuario = current_user.id_Usuario
    fecha = request.form["fecha"]
    hora = request.form["hora"]
    descripcion = request.form["descripcion"]
    profesor = request.form["profesor"]
    materia = request.form["materia"]

    tarea = Tarea(nombre, usuario, materia, profesor, fecha, hora, descripcion)
    db.session.add(tarea)
    db.session.commit()

    flash("Tarea creada")
    return render_template("/principal.html")
