from wtforms import Form
from wtforms import StringField,SelectField,RadioField,EmailField,IntegerField
from wtforms import validators

class UserForm(Form):

    nombre= StringField('nombre',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4,max=10,message='ingresa nombre valido')
    ])
    apaterno= StringField('apaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4,max=10,message='ingresa apallido paterno valido')
    ])
    amaterno= StringField('amaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4,max=10,message='ingresa apellido materno valido')
    ])
    edad= IntegerField('edad',[
        validators.number_range(min=1,max=20,message='valor no valido')
    ])

    correo= EmailField('correo',[
        validators.Email(message='Ingresa un correo valido'),
    ])

class UserForm2(Form):
    id = IntegerField('id')
    nombre= StringField('nombre',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4,max=10,message='ingresa nombre valido')
    ])
    apepaterno= StringField('apepaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4,max=10,message='ingresa apallido paterno valido')
    ])
    email= EmailField('correo',[
        validators.Email(message='Ingresa un correo valido'),
    ])

    # nombre=StringField('nombre')
    # apaterno=StringField('apaterno')
    # amaterno=StringField('amaterno')
    # edad=IntegerField('edad')
    # correo=EmailField('correo')
