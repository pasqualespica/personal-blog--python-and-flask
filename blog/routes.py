from flask import render_template
from blog import app

"""
    views : riceve un richiesta HTTP ed elabora una risposta
"""


@app.route("/")
def homepage():
    # return "<h1>Hello BLOG!<h1>"
    posts = [ {"title" : "primo posrt", "body" : "random body1"},
              {"title": "secondo posrt", "body": "random body2"}, ]

    some_bool_flag = False


    # passare queste variabili come "context" dei nostri templates
    return render_template("homepage.html", 
                            posts=posts, 
                            boolean_fg=some_bool_flag)

