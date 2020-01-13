import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # utilizzate per la generazion del token per la sicurezza dei nostri FORM
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "blog.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "static/img/posts"
