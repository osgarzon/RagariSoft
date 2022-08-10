from flask import Blueprint
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required
from models.profesor import Profesor
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
    return render_template("/principal.html")
