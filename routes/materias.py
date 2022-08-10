from flask import Blueprint
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required
from models.materia import Materia
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
    return render_template("/principal.html")
