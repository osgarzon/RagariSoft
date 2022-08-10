from flask import Flask
from routes.usuarios import usuarios
from routes.horarios import horarios
from routes.tareas import tareas
from routes.profesores import profesores
from routes.materias import materias
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models.usuariolog import Usuariolog
from models.usuario import Usuario

app = Flask(__name__)

app.secret_key = "secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://sergio:1234@localhost/studilydb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id_Usuario):
    user = Usuario.query.filter_by(id_Usuario=id_Usuario).first()
    if user:
        return user
    else:
        return None


app.register_blueprint(usuarios)
app.register_blueprint(tareas)
app.register_blueprint(profesores)
app.register_blueprint(materias)
app.register_blueprint(horarios)
