""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

class Score(db.Model):
    __tablename__ = 'score'
    #_id = db.Column(db.Integer, primary_key=True)
    #_name = db.Column(db.String(255), nullable=False)
    _user_time = db.Column(db.Float, nullable=False, primary_key=True)
    _feedback = db.Column(db.String(255), nullable=False)


    def __init__(self, user_time, feedback):
        #self._id = id
        #self._name = name
        self._user_time = user_time
        self._feedback = feedback

    """
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    """

    @property
    def user_time(self):
        return self._user_time

    @property
    def feedback(self):
        return self._feedback

    def serialize(self):
        return {
            #"id": self._id, 
            #"name": self._name,
            "user_time": self._user_time,
            "feedback": self._feedback,
        }
    

    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None
        
def read(self):
        return {
            #"id": self.id,
          #  "name": self.name,
            "user_time": self.user_time,
            "feedback": self.feedback,
            # "posts": [post.read() for post in self.posts]
        }

def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

    
def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False

def initScorey():
    with app.app_context():
        db.create_all()
        # Add initialization data if needed
        
        scorestoadd = []
        try:
            with open(r'scores.json','r') as json_file:
                data = json.load(json_file)
        except Exception as error:
            print("failed")

        for item in data:
            # print(item)
             s_toadd = Score(
                 #id = item['id'],
                 #name = item['name'],
                 user_time=item['user_time'], 
                 feedback=item['feedback'])
             scorestoadd.append(s_toadd)
            
        """Builds sample user/note(s) data"""
        for s in scorestoadd:
            try:
                s.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {s.scorestoadd}")