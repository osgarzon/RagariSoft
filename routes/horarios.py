from flask import Blueprint
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required
from models.profesor import Profesor
from models.materia import Materia


horarios = Blueprint("horarios", __name__)


@horarios.route("/principal")
@login_required
def principal():
    profesoresdb = Profesor.query.all()
    materiasdb = Materia.query.all()
    return render_template(
        "principal.html",
        profesoresdb=profesoresdb,
        materiasdb=materiasdb,
    )


def status_401(error):
    flash("Acceso denegado")
    return redirect("/signin")


horarios.register_error_handler(401, status_401)
