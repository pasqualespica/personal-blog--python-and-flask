"""
Questo file contiene delle classi particolari/modelli che rappresantano
le tabelle cbe verranno aggoiunte al nostro DB
"""

from datetime import datetime
# UserMixIn contains : is active, is auth, .... 
from flask_login import UserMixin
# used for pwd-crypt
from werkzeug.security import check_password_hash, generate_password_hash
from blog import db, login_manager

# definire una funzione specificate per il funzinamento di flask_login
# per tenere traccia dell'utente attualmente connesso
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# classe Utente

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    username = db.Column(db.String(12), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    # campo relazionale NON rappresente un campo/colonna della tabella
    # relazione INVERSA
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        # return super().__repr__()
        return f"User('{self.id}', '{self.username}', '{self.email}')"

    def set_password_hash(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # ref-key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(240))
    body = db.Column(db.Text(), nullable=False) # no string limits

    def __repr__(self):
        # return super().__repr__()
        return f"Post('{self.id}', '{self.title}')"
