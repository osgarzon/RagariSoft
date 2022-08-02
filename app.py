from flask import Flask
from routes.usuarios import usuarios
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key= "secret key"
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:dan961030@localhost/studilydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(usuarios)

