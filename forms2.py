from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    nombre = StringField('Nombre', [DataRequired()])
    apellido_p = StringField('Apellido Paterno', [DataRequired()])
    apellido_m = StringField('Apellido Materno', [DataRequired()])
    dia = IntegerField('Día', [DataRequired()])
    mes = IntegerField('Mes', [DataRequired()])
    anio = IntegerField('Año', [DataRequired()])
    sexo = RadioField('Sexo', choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], default='Masculino', validators=[DataRequired()])
