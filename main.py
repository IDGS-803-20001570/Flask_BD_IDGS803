from flask import Flask,render_template,request,Response
from flask_wtf.csrf import CSRFProtect
from flask import redirect
from flask import flash
from config import DevelopmentConfig
from flask import g

import forms
from models import db
from models import Alumnos


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route("/alumnos",methods=["GET","POST"])
def alum():
    
    nom=""
    ama=""
    apa=""
    alum_form=forms.UserForm(request.form)
    if request.method == 'POST' and alum_form.validate():
        nom=alum_form.nombre.data
        apa=alum_form.apaterno.data
        ama=alum_form.amaterno.data

        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)

        print("Nombre: {}".format(nom))
        print("apepaterno: {}".format(apa))
        print("apematerno: {}".format(ama))

    return render_template("alumnos.html",form=alum_form,nom=nom,ama=ama,apa=apa)

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
