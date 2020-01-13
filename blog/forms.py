from flask_wtf import FlaskForm
# add to use image
from flask_wtf.file import FileField, FileAllowed 
#                   optional      
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
#validatore
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    """
    deve possedere 4 campi
    """
    username = StringField('Username', validators=[DataRequired("CAMPO OBBLIGATORIO !!!")])  # nome campo / etichetta
    password = PasswordField('Password', validators=[DataRequired("CAMPO OBBLIGATORIO !!!")])
    remember_me = BooleanField('Remember-Me')
    submit = SubmitField('Login')

class PostForm(FlaskForm): # deve rispecchiare i campi del "model" Psot
    title = StringField("Title", 
        validators=[DataRequired("CAMPO OBBLIGATORIO !!!"), Length(min=3, max=120, message="deve contenet almeno 3 e al max 120")])
    description = TextAreaField("Description", 
        validators=[Length(max=240, message="massimo 140 caratteri")])
    body = TextAreaField("Content-body", validators=[DataRequired("CAMPO OBBLIGATORIO !!!")])
    image = FileField('Copertina Articolo', validators=[FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField('Publish-it')
