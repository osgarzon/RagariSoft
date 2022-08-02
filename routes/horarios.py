
from flask import Blueprint
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required


horarios = Blueprint("horarios", __name__)

@horarios.route("/principal")
@login_required
def principal():
    return render_template("principal.html")