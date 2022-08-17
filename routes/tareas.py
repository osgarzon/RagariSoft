from flask import Blueprint
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required
from models.tarea import Tarea
from models.profesor import Profesor
from models.materia import Materia
from models.usuario import Usuario
from routes.horarios import horarios
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
    return redirect(url_for("horarios.principal"))


@tareas.route("/eliminarTarea", methods=["POST"])
@login_required
def delete():
    tarea = request.form["tarea"]
    print("LA TAREA ES:   ",tarea)
    tarea = Tarea.query.get(tarea)
    db.session.delete(tarea)
    db.session.commit()

    flash("Tarea eliminada")
    return redirect(url_for("horarios.principal"))

@tareas.route("/actualizarTarea", methods=["POST"])
@login_required
def update():
    comprobador = False
    tarea = request.form["nombre"]
    tarea = Tarea.query.get(tarea)
    fecha = request.form["fecha"]
    hora = request.form["hora"]
    descripcion = request.form["descripcion"]
    profesor = request.form["profesor"]
    materia = request.form["materia"]

    if(fecha!=""):
        tarea.fecha=fecha
        comprobador = True
    if(hora!=""):
        tarea.hora=hora
        comprobador = True
    if(descripcion!=""):
        tarea.descripcion=descripcion
        comprobador = True
    if(profesor!=""):
        tarea.id_profesor=profesor
        comprobador = True
    if(materia!=""):
        tarea.id_materia=materia
        comprobador = True

    if(comprobador):
        flash("Tarea actualizada")
        db.session.commit()
    else:
        flash("Tarea sin cambios")

        

    return redirect(url_for("horarios.principal"))