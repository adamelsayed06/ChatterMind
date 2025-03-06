#database settings, JWT secrets, credentials etc.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True, nullable = False)
    name = db.Column(db.String(40), unique = False, nullable = False)
    authProvider = db.Column()

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    zoom_meeting_id = db.Column(db.String(50), nullable = False, unique = True)
    topic = db.Column(db.String(255))

class Transcript(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    meeting_id = db.Column(db.Integer, db.ForeignKey('meeting.id'), nullable = False) #every transcript paired to a meeting
    transcript_text = db.Column(db.Text(500))

    #potentially add relationship between Transcript/Meeting w/back_populates so u can pull transcript of specific meeting, or meeting of specific transcript easily

class Summary(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    meeting_id = db.Column(db.Integer, db.ForeignKey('meeting.id'), nullable = False) #every meeting needs a summary
    summary_text = db.Column(db.Text(500))