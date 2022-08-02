import imp
from flask import Flask
from routes.usuarios import usuarios
from routes.horarios import horarios
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models.usuariolog import Usuariolog
from models.usuario import Usuario

app = Flask(__name__)

app.secret_key = "secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:dan961030@localhost/studilydb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id_Usuario):
    user = Usuario.query.filter_by(id_Usuario=id_Usuario).first()
    nombre = user.nombre_apellido
    if user:
        return user
    else:
        return None


app.register_blueprint(usuarios)
app.register_blueprint(horarios)
