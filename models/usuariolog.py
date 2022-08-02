from flask import flash
from models.usuario import Usuario

class Usuariolog:

    @classmethod
    def login(self, nusuario, contraseña):
        user=Usuario.query.filter_by(id_Usuario = nusuario).first()
        if user:
            if user.contraseña==contraseña:
                return user
            else:
                return ('Contraseña incorrecta')   
        else:
            return ('Usuario inexistente')
    

    def get_by_id(self, nusuario):
        print(nusuario)
        user=Usuario.query.filter_by(id_Usuario = nusuario).first()
        nombre=user.nombre_apellido
        if user:
            return nombre
        else:
            return None