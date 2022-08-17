from flask import Blueprint
from flask import Blueprint, render_template, request, flash
from flask_login import login_required
from models.usuario import Usuario
from models.usuariolog import Usuariolog
from utils.db import db
from models.plato import Plato


platos = Blueprint("platos", __name__)


@platos.route("/principal")
@login_required
def principal():
    user = Usuariolog.get_by_id
    return render_template("principal.html")

    
@platos.route("/carrito", methods=["POST", "GET"])
@login_required
def carrito():
    burguer = request.form["burguer"]
    papas = request.form["papas"]
    ensalada = request.form["ensalada"]
    oreo = request.form["oreo"]
    if(burguer!=""):
         plato = Plato("Super combo familiar",burguer)
         db.session.add(plato)
    if(papas!=""):
         plato = Plato("Papas grandes",papas)
         db.session.add(plato)
    if(ensalada!=""):
         plato = Plato("Ensalada grande",ensalada)
         db.session.add(plato)
    if(oreo!=""):
         plato = Plato("Avalancha oreo",oreo)
         db.session.add(plato)

    db.session.commit()
    flash("Producto agregado al carrito")
    return render_template("pedir.html")

@platos.route("/obtenerCarrito", methods=["POST", "GET"])
@login_required
def obtenerCarrito():
    platosdb=Plato.query.all()
    a=0

    for i in platosdb:
        if(i.id_Plato == "Super combo familiar"):
            a = a + 39900*i.cantidad
        if(i.id_Plato == "Ensalada grande"):
            a = a + 5900*i.cantidad
        if(i.id_Plato == "Papas grandes"):
            a = a + 6500*i.cantidad
        if(i.id_Plato == "Avalancha oreo"):
            a = a + 6000*i.cantidad

    return render_template("carrito.html",platosdb=platosdb,a=a)

@platos.route("/pago", methods=["POST", "GET"])
@login_required
def obtenerpago():
    flash("Pago exitoso")
    return render_template("principal.html")


@platos.route("/elcorral", methods=["POST", "GET"])
@login_required
def corral():
    user = Usuariolog.get_by_id
    return render_template("principal.html")

@platos.route("/elcarnal", methods=["POST", "GET"])
@login_required
def carnal():
    user = Usuariolog.get_by_id
    return render_template("principal.html")

@platos.route("/jenos", methods=["POST", "GET"])
@login_required
def jenos():
    user = Usuariolog.get_by_id
    return render_template("principal.html")

@platos.route("/kfc", methods=["POST", "GET"])
@login_required
def kfc():
    user = Usuariolog.get_by_id
    return render_template("pedir.html")