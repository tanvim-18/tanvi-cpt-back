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

    #def create(self):
     #   try:
      #      db.session.add(self)
       #     db.session.commit()
        #    return self
        #except IntegrityError:
         #   db.session.remove()
          #  return None
        
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

# Inserting data into the database
scores_data = [
    {"user_time": 1, "score": "Amazing"},
    {"user_time": 2, "score": "Amazing"},
    {"user_time": 3, "score": "Amazing"},
    {"user_time": 4, "score": "Amazing"},
    {"user_time": 5, "score": "Amazing"},
    {"user_time": 6, "score": "Amazing"},
    {"user_time": 7, "score": "Amazing"},
    {"user_time": 8, "score": "Amazing"},
    {"user_time": 9, "score": "Amazing"},
    {"user_time": 10, "score": "Very Good"},
    {"user_time": 11, "score": "Very Good"},
    {"user_time": 12, "score": "Very Good"},
    {"user_time": 13, "score": "Very Good"},
    {"user_time": 14, "score": "Very Good"},
    {"user_time": 15, "score": "Very Good"},
    {"user_time": 16, "score": "Very Good"},
    {"user_time": 17, "score": "Very Good"},
    {"user_time": 18, "score": "Very Good"},
    {"user_time": 19, "score": "Very Good"},
    {"user_time": 20, "score": "Very Good"},
    {"user_time": 21, "score": "Ok"},
    {"user_time": 22, "score": "Ok"},
    {"user_time": 23, "score": "Ok"},
    {"user_time": 24, "score": "Ok"},
    {"user_time": 25, "score": "Ok"},
    {"user_time": 26, "score": "Ok"},
    {"user_time": 27, "score": "Ok"},
    {"user_time": 28, "score": "Ok"},
    {"user_time": 29, "score": "Ok"},
    {"user_time": 30, "score": "Ok"},
    {"user_time": 31, "score": "Good"},
    {"user_time": 32, "score": "Good"},
    {"user_time": 33, "score": "Good"},
    {"user_time": 34, "score": "Good"},
    {"user_time": 35, "score": "Good"},
    {"user_time": 36, "score": "Good"},
    {"user_time": 37, "score": "Good"},
    {"user_time": 38, "score": "Good"},
    {"user_time": 39, "score": "Good"},
    {"user_time": 40, "score": "Good"},
    {"user_time": 41, "score": "Improving"},
    {"user_time": 42, "score": "Improving"},
    {"user_time": 43, "score": "Improving"},
    {"user_time": 44, "score": "Improving"},
    {"user_time": 45, "score": "Improving"},
    {"user_time": 46, "score": "Improving"},
    {"user_time": 47, "score": "Improving"},
    {"user_time": 48, "score": "Improving"},
    {"user_time": 49, "score": "Improving"},
    {"user_time": 50, "score": "Improving"},
    {"user_time": 51, "score": "Need Improvement"},
    {"user_time": 52, "score": "Need Improvement"},
    {"user_time": 53, "score": "Need Improvement"},
    {"user_time": 54, "score": "Need Improvement"},
    {"user_time": 55, "score": "Need Improvement"},
    {"user_time": 56, "score": "Need Improvement"},
    {"user_time": 57, "score": "Need Improvement"},
    {"user_time": 58, "score": "Need Improvement"},
    {"user_time": 59, "score": "Need Improvement"},
    {"user_time": 60, "score": "Need Improvement"}
]

# Inserting data into the database
for data in scores_data:
    user_time = data["user_time"]
    score = data["score"]
    highscore = Highscore(user_time=user_time, score=score)
    highscore.create()
