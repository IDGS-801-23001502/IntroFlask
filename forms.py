from wtforms import Form, StringField,IntegerField,PasswordField,FloatField,EmailField,validators

class UserForm(Form):
    matricula = IntegerField("Matricula",[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100,max=1000,message="Ingrese valor valido")
    ])
    nombre = StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10,message="Ingrese nombre valido")
    ])
    apaterno=StringField("Apaterno",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10,message="Ingrese apellido valido")
    ])
    amaterno=StringField("Amaterno",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10,message="Ingrese apellido valido")
    ])
    correo=EmailField("Correo",[
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingresa correo valido")
    ])

