#database settings, JWT secrets, credentials etc.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

class User(db.model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True, nullable = False)
    name = db.Column(db.String(40), unique = False, nullable = False)
    authProvider = db.Column()

