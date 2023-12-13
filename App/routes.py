from flask import Blueprint, render_template, request, redirect
from .models import db, Persona, Entrada
import bcrypt
import base64

loged=False

main = Blueprint('main',__name__)

@main.route('/')
def index():
    entradas=Entrada.query.all()
    return render_template('index.html',entradas=entradas)

@main.route('/leer/<int:entrada_id>')
def leer(entrada_id):
    entrada = Entrada.query.get_or_404(entrada_id)
    return render_template('leer.html', entrada=entrada)

@main.route('/cuenta')
def cuenta():
    global loged, user_loged
    if loged:
        entradas = Entrada.query.filter(Entrada.autor == user_loged).all()
        return render_template('cuenta.html',entradas=entradas, user_loged=user_loged)
    else:
        return redirect('/iniciarss')
    
@main.route('/escribir')
def escribir():
    global loged, user_loged
    if loged:
        return render_template('escribir.html')
    else:
        return redirect('/iniciarss')

@main.route('/registro')
def registro():
    return render_template('registro.html')

@main.route('/submit_reg',methods=['POST'])
def submit_reg():
    usuario= request.form.get('usuario')
    email=request.form.get('email')
    contraseña= request.form.get('contraseña')
    usuarios=Persona.query.all()
    for i in usuarios:
        if i.email==email:
            return render_template('reg_error.html')
    precode=bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())
    password=base64.b64encode(precode).decode('utf-8')
    nueva_persona=Persona(nombre=usuario,contraseña=password,email=email)
    db.session.add(nueva_persona)
    db.session.commit()
    return render_template('reg_exito.html')

@main.route('/iniciarss')
def iniciarss():
    return render_template('iniciarss.html')

@main.route('/submit_log',methods=['POST'])
def submit_log():
    global loged, user_loged
    email=request.form.get('email')
    contraseña= request.form.get('contraseña')
    usuarios=Persona.query.all()
    for i in usuarios:
        if i.email==email:
            precode=base64.b64decode(i.contraseña.encode('utf-8'))
            if bcrypt.checkpw(contraseña.encode('utf-8'), precode):
                loged=True
                user_loged=i.nombre
                return render_template('cuenta.html')
            else:
                return render_template('login_error.html')
    return render_template('login_error.html')

@main.route('/submit_ent',methods=['POST'])
def submit_ent():
    global loged, user_loged
    titulo= request.form.get('titulo')
    contenido=request.form.get('contenido')
    entradas=Entrada.query.all()
    nueva_entrada=Entrada(titulo=titulo,contenido=contenido,autor=user_loged)
    db.session.add(nueva_entrada)
    db.session.commit()
    return render_template('cuenta.html')

@main.route('/borrar/<int:entrada_id>', methods=['POST', 'DELETE'])
def borrar(entrada_id):
    entrada = Entrada.query.get_or_404(entrada_id)
    db.session.delete(entrada)
    db.session.commit()
    return redirect('/cuenta')

@main.route('/logout', methods=['POST'])
def logout():
    global loged, user_loged
    loged = False
    user_loged = None
    return redirect('/iniciarss')