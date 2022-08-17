from flask import Flask,render_template,redirect,url_for,make_response,session
from routes.usuarios import usuarios
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, DateField, EmailField
from wtforms.validators import DataRequired, Email
from routes.horarios import horarios
from routes.tareas import tareas
from routes.profesores import profesores
from routes.materias import materias
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models.usuariolog import Usuariolog
from models.usuario import Usuario
import unittest

app = Flask(__name__)

app.secret_key = "secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://sergio:1234@localhost/studilydb"
#"mysql://sergito:sergito1234@85.10.205.173/studilydb"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)
login_manager_app = LoginManager(app)


class LoginFormSignIn(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')

@login_manager_app.user_loader
def load_user(id_Usuario):
    user = Usuario.query.filter_by(id_Usuario=id_Usuario).first()
    if user:
        return user
    else:
        return None

@app.route('/hiking')
def test_form():
    return render_template("index.html")


@app.cli.command()
def test():
    tests= unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)




@app.route('/hiworld', methods=['GET', 'POST'])
def hiworld():
    user_ip = session.get('user_ip')

    login_form = LoginFormSignIn()

    username = session.get('username')
    password = session.get('password')

    session['username'] = username
    session['password'] = password

    context = {
        'user_ip': user_ip,
        'login_form': login_form,
        'username': login_form.username.data,
        'password': login_form.password.data
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        session['username'] = username
        session['password'] = password
        return redirect('/hiking')

    return render_template('index.html', **context)

app.register_blueprint(usuarios)
app.register_blueprint(tareas)
app.register_blueprint(profesores)
app.register_blueprint(materias)
app.register_blueprint(horarios)
