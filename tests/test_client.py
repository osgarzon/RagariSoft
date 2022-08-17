from flask import Flask, url_for
from routes.usuarios import usuarios

def test_app():
    app = Flask(__name__)
    app.register_blueprint(usuarios, url_prefix='/')

    web = app.test_client()
    print("SI SIRVIO")
    rv = web.get('/')
    response = url_for(rv)