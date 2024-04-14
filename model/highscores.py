from __init__ import db
import json

class Highscore(db.Model):
    __tablename__ = 'highscores'

    id = db.Column(db.Integer, primary_key=True)
    user_time = db.Column(db.Integer, nullable=False)
    score = db.Column(db.String(50), nullable=False)

    def __init__(self, user_time, score):
        self.user_time = user_time
        self.score = score

    @property
    def time(self):
        return self.user_time

    @time.setter
    def time(self, user_time):
        self.user_time = user_time

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __repr__(self):
        return f"Highscore({self.user_time}, '{self.score}')"

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def read(self):
        return {
            "user_time": self.user_time,
            "score": self.score
        }

    def update(self, user_time=None, score=None):
        if user_time is not None:
            self.user_time = user_time
        if score is not None:
            self.score = score
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

# Read data from highscores.json and insert into the database
with open('highscores.json', 'r') as json_file:
    highscores_data = json.load(json_file)

for data in highscores_data:
    user_time = data["user_time"]
    score = data["score"]
    highscore = Highscore(user_time=user_time, score=score)
    highscore.create()
