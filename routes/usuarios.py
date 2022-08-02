from flask import Blueprint, render_template, request, redirect
from models.usuario import Usuario
from utils.db import db


usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/ingreso')
def home():
    usuariosdb = Usuario.query.all()
    return render_template('registro.html', usuariosdb = usuariosdb)

@usuarios.route('/principal')
def principal():
    return render_template('index.html')

@usuarios.route('/registro')
def dir_registro():
    return redirect('registro.html')

@usuarios.route('/obtenerRegistro', methods=['POST'])
def add_usuario():
    nusuario = request.form['usuario']
    nombre = request.form['nombre']
    correo = request.form['correo']
    contraseña = request.form['contraseña']

    usuario = Usuario(nusuario, nombre, correo, contraseña)

    print(usuario)

    db.session.add(usuario)
    db.session.commit()
    
    return "registrado"


@usuarios.route('/actualizarUsuario')
def act_usuario():
    return 'tarea guardada'

@usuarios.route('/borrar/<id>')
def del_usuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()

    print(usuario)
    return redirect('/ingreso')