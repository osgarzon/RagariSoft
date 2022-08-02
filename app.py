from flask import Flask
from routes.usuarios import usuarios
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models.usuariolog import Usuariolog

app = Flask(__name__)

app.secret_key= "secret key"
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:dan961030@localhost/studilydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(id_Usuario):
    print(id_Usuario)
    print('error')
    return Usuariolog.get_by_id(id_Usuario)

app.register_blueprint(usuarios)






