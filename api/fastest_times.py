# Import necessary modules
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy instance
db = SQLAlchemy()

# Define FastestTime model
class FastestTime(db.Model):
    __tablename__ = 'fastest_times'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    time = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, time):
        self.username = username
        self.time = time

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'time': self.time,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.to_dict()
        except Exception as e:
            db.session.rollback()
            print(f"Failed to create fastest time: {e}")
            return None
