from multiprocessing import current_process
from flask import Blueprint
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required
from models.profesor import Profesor
from models.materia import Materia
from models.tarea import Tarea
from models.usuario import Usuario
from models.usuariolog import Usuariolog


horarios = Blueprint("horarios", __name__)


@horarios.route("/principal")
@login_required
def principal():
    user = Usuariolog.get_by_id
    print(" USUARIOOOO: ",user)
    profesoresdb = Profesor.query.all()
    materiasdb = Materia.query.all()
    tareasdb = Tarea.query.all()
    return render_template(
        "principal.html",
        profesoresdb=profesoresdb,
        materiasdb=materiasdb,
        tareasdb = tareasdb
    )

@horarios.route("/eliminar")
@login_required
def eliminaDato():
    tareasdb = Tarea.query.all()
    profesoresdb = Profesor.query.all()
    materiasdb = Materia.query.all()
    return render_template(
        "/eliminar.html",
        tareasdb=tareasdb,
        profesoresdb=profesoresdb,
        materiasdb=materiasdb,
    )

@horarios.route("/actualizar")
@login_required
def actualizaDato():
    tareasdb = Tarea.query.all()
    profesoresdb = Profesor.query.all()
    materiasdb = Materia.query.all()
    return render_template(
        "/actualizar.html",
        tareasdb=tareasdb,
        profesoresdb=profesoresdb,
        materiasdb=materiasdb,
    )


def status_401(error):
    flash("Acceso denegado")
    return redirect("/signin")

def status_404(error):
    flash("Página no encontrada")
    return redirect("/signin")

horarios.register_error_handler(401, status_401)
horarios.register_error_handler(404, status_404)
