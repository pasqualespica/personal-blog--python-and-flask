from flask import Flask

app = Flask(__name__)

"""
export FLASK_APP=hello_flask/application.py

export FLASK_ENV=development

"""

# qui utizziamo un decoratore a diferenza di Django
@app.route("/")
def homepage():
    return "<h1 style='color:black'>Hello Flask World!<h1>"

# un altra funzione view
@app.route("/contatti")
def contatti():
    return "Contattaci!"
