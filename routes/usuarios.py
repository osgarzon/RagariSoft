from flask import Blueprint, render_template, request, redirect, flash, url_for
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
    
    flash('usuario creado')
    return redirect(url_for("usuarios.home"))


@usuarios.route('/actualizarUsuario/<id>', methods=['POST', 'GET'])
def act_usuario(id):
    usuario = Usuario.query.get(id)
    if request.method == 'POST':
        usuario.id_Usuario = request.form['usuario']
        usuario.nombre_apellido = request.form['nombre']
        usuario.correo = request.form['correo']
        usuario.contraseña = request.form['contraseña'] 
        db.session.commit()
        
        return redirect('/registro.html')
        
    return render_template('registro.html', usuario=usuario)

@usuarios.route('/borrar/<id>')
def del_usuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()

    print(usuario)
    return redirect('/ingreso')