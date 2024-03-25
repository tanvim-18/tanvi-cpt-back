# model/highscores.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MemoryHighScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    completion_time = db.Column(db.Float, nullable=False)

    def __init__(self, username, completion_time):
        self.username = username
        self.completion_time = completion_time

    def to_dict(self):
        return {
            'username': self.username,
            'completion_time': self.completion_time
        }
