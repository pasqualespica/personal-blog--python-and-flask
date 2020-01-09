from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user

from blog import app
from blog.models import Post, User
from blog.forms import LoginForm

"""
    views : riceve un richiesta HTTP ed elabora una risposta
"""


@app.route("/")
def homepage():
    # return "<h1>Hello BLOG!<h1>"

    # posts = [ {"title" : "primo post", "body" : "random body1"},
    #           {"title": "secondo post", "body": "random body2"}, ]
    # some_bool_flag = False
    # return render_template("homepage.html",
    #                        posts=posts,
    #                        boolean_fg=some_bool_flag)

    # posts = Post.query.all()
    posts = Post.query.order_by(Post.created_at.desc()).all()
    # passare queste variabili come "context" dei nostri templates
    return render_template("homepage.html",  posts=posts)

@app.route("/posts/<int:post_id>")
def post_detail(post_id):
    post_instance = Post.query.get_or_404(post_id)
    return render_template("post_detail.html", post=post_instance)

@app.route("/about")
def about():
    return render_template('about_page.html')


@app.route("/login", methods=["GET","POST"]) 
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('username and password non combaciono')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('homepage'))
    # se sta semplicemente la pagina per la prima volta
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homepage'))
