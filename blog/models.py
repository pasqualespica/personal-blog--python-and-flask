"""
Questo file contiene delle classi particolari/modelli che rappresantano
le tabelle cbe verranno aggoiunte al nostro DB
"""

from datetime import datetime
from blog import db

# classe Utente

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    username = db.Column(db.String(12), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    # campo relazionale NON rappresente un campo/colonna della tabella
    # relazione INVERSA
    post = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        # return super().__repr__()
        return f"User('{self.id}', '{self.username}', '{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # ref-key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    title = db.Column(db.String(120))
    body = db.Column(db.Text(), nullable=False) # no string limits

    def __repr__(self):
        # return super().__repr__()
        return f"Post('{self.id}', '{self.title}')"
