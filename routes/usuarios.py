from flask import Blueprint, render_template, request
from models.usuario import Usuario
from utils.db import db


usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/')
def home():
    return render_template('index.html')

@usuarios.route('/registro')
def dir_registro():
    return render_template('registro.html')

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

@usuarios.route('/borrar')
def del_usuario():
    return 'tarea guardada'