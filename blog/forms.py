from flask_wtf import FlaskForm
#                   optional      
from wtforms import BooleanField, PasswordField, StringField, SubmitField
#validatore
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """
    deve possedere 4 campi
    """
    username = StringField('Username', validators=[DataRequired()]) # nome campo / etichetta
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember-Me')
    submit = SubmitField('Login')

