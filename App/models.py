from . import db

class Persona(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(100))
    contraseña=db.Column(db.String(100))
    email=db.Column(db.String(100))

class Entrada(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    titulo=db.Column(db.String(100))
    contenido=db.Column(db.String(2000))
    autor=db.Column(db.String(100))