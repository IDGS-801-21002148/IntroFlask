from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email
 
class UserForm(Form):
    matricula = IntegerField('Matricula', [
        DataRequired(message='Campo requerido'),
        Length(min=3, max=10, message='La matricula debe tener entre 3 y 10 digitos')
    ])
    nombre = StringField('Nombre', [
        DataRequired(message='Campo requerido'),
        Length(min=3, max=50, message='El nombre debe tener entre 3 y 50 caracteres')
    ])
    apellido = StringField('Apellido', [
        DataRequired(message='Campo requerido'),
        Length(min=3, max=50, message='El apellido debe tener entre 3 y 50 caracteres')
    ])
    correo = EmailField('Correo', [
        DataRequired(message='Campo requerido'),
        Email(message='Correo invalido')
    ])