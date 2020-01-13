from flask import render_template, flash, redirect, url_for, abort, request # abort e request add to UPDATE POST
from flask_login import current_user, login_user, logout_user, login_required

from blog import db, app
from blog.models import Post, User
from blog.forms import LoginForm, PostForm
from blog.utils import title_slugfier, save_picture

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


# @app.route("/posts/<int:post_id>")
# def post_detail(post_id):
@app.route("/posts/<string:post_slug>")
def post_detail(post_slug):  # adesso accetta lo slug
    # post_instance = Post.query.get_or_404(post_id)
    post_instance = Post.query.filter_by(slug=post_slug).first_or_404()
    return render_template("post_detail.html", post=post_instance)

    
@app.route("/create-post", methods=["GET","POST"]) 
@login_required # in questo modo solo chi e' loggato puo' chiamarlo vedi anche import login_required
def post_create():
    form = PostForm()
    if form.validate_on_submit():
        slug = title_slugfier(form.title.data)
        new_post = Post(
            title=form.title.data, 
            body=form.body.data, 
            slug=slug,
            description=form.description.data,
            author=current_user)

        if  form.image.data:
            try : # try in caso di image corrotta 
                image = save_picture(form.image.data) # return path
                new_post.image = image
            except Exception:
                db.session.add(new_post)
                db.session.commit()
                flash("Si e' verifcato un problema con l'immagina caricata !!!")
                return redirect(url_for('post_update', post_id=new_post.id))

        db.session.add(new_post)
        db.session.commit()
        # return redirect(url_for("post_detail", post_id=new_post.id))
        return redirect(url_for("post_detail", post_slug=slug))
    # creare un nuovo post con un nuovo render html
    return render_template("post_editor.html", form=form)
    

@app.route("/posts/<int:post_id>/update", methods=["GET", "POST"])
@login_required  # in questo modo solo chi e' loggato puo' chiamarlo vedi anche import login_required
def post_update(post_id):
    post_instance = Post.query.get_or_404(post_id)
    #   verificare che l'user che ha creato il post e' lo stesso che sta 
    #   facendo la richiesta di aggiornamento, in caso negativo paginda di ERROR
    if post_instance.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post_instance.title = form.title.data
        post_instance.description = form.description.data
        post_instance.body = form.body.data

        if  form.image.data:
            try : # try in caso di image corrotta 
                print(form.image.data)
                image = save_picture(form.image.data) # return path
                post_instance.image = image
            except Exception:
                db.session.commit()
                flash("Si e' verifcato un problema con l'immagina caricata !!!")
                return redirect(url_for('post_update', post_id=post_instance.id))

        db.session.commit()
        # return redirect(url_for('post_detail', post_id=post_instance.id))
        return redirect(url_for('post_detail', post_slug=post_instance.slug))
    elif request.method == "GET" : 
        #   caso la pagina venga richiesta 
        #   e popolare il form
        form.title.data = post_instance.title
        form.description.data = post_instance.description
        form.body.data = post_instance.body
    return render_template("post_editor.html", form=form)


# tolto GET method perche' non abbiamo nessun maschera da mostrare
#       e la riechiesta POST e' sicuramente la piu' appropriata
@app.route("/posts/<int:post_id>/delete", methods=["POST"])
@login_required  # in questo modo solo chi e' loggato puo' chiamarlo vedi anche import login_required
def post_delete(post_id):
    post_instance = Post.query.get_or_404(post_id)
    if post_instance.author != current_user:
        abort(403)
    db.session.delete(post_instance)
    db.session.commit()
    return redirect(url_for('homepage'))

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
