
"""
    - Here we init ours DB
    - 
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# "render_as_batch" per andare incontro ai limiti di sqlite ( clone in caso di change )
with app.app_context():
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)
    else: 
        migrate.init_app(app, db)

from blog import models, routes
"""
    1. flask db init
    2. flask db migrate -m "Creazione Tabelle Post e User"
    3. flask db upgrade
    to explre DB use DB Browser for SQLite
    per annullare <opzionale> flask db downgrade
"""

