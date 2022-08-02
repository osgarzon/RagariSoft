from flask import Blueprint, render_template, request, redirect, flash, url_for
from models.usuario import Usuario
from models.usuariolog import Usuariolog
from utils.db import db
from flask_login import login_user, logout_user, login_required



usuarios = Blueprint('usuarios', __name__)



@usuarios.route('/signup')
def signup():
    usuariosdb = Usuario.query.all()
    return render_template('registro.html', usuariosdb = usuariosdb)

@usuarios.route('/signin', methods=['POST', 'GET'])
def signin():

    if request.method=='POST':
        nusuario = request.form['usuario']
        contraseña = request.form['contraseña']
        
        user=Usuariolog.login(nusuario, contraseña)
        if user=='Contraseña incorrecta':
            flash(user)
            return redirect('/signin')
        elif user=='Usuario inexistente':
            flash(user)
            return redirect('/signin')
        else:
            login_user(user)
            return render_template('/principal.html')
    #else:
    return render_template('/index.html')

@usuarios.route('/registro')
def dir_registro():
    return redirect('registro.html')

@usuarios.route('/obtenerRegistro', methods=['POST'])
def add_usuario():

    nusuario = request.form['usuario']
    nombre = request.form['nombre']
    correo = request.form['correo']
    contraseña = request.form['contraseña']

    user=Usuario.query.filter_by(id_Usuario = request.form['usuario']).first()
    if user:
        flash('Usuario ya existe', 'warning')
        return redirect('/signup')

    usuario = Usuario(nusuario, nombre, correo, contraseña)

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