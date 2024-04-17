""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from model import db

''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

# Define the drinks class to manage actions in the 'drinks' table
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Drink represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Score(db.Model):
    __tablename__ = 'scores'  # table name is plural, class name is singular

    # Define the Drink schema with "vars" from object! Javascript!
    _scoreName = db.Column(db.String(255), primary_key=True)
    _calories = db.Column(db.Integer, unique=False, nullable=False)

    # constructor of a Drink object, initializes the instance variables within object (self)
    def __init__(self, scoreName, calories):
        self._scoreName = scoreName    # variables with self prefix become part of the object, 
        self._calories = calories


    # a drinkName getter method, extracts drinkName from object
    @property
    def scoreName(self):
        return self._scoreName
    
    # a setter function, allows drinkName to be updated after initial object creation
    @scoreName.setter
    def scoreName(self, scoreName):
        self._scoreName = scoreName
    
    # a getter method, extracts calories from object
    @property
    def calories(self):
        return self._calories
    
    # a setter function, allows calories to be updated after initial object creation
    @calories.setter
    def calories(self, calories):
        self._calories = calories
          
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    #CREATE
    def create(self):
        try:
            # creates a drink object from Drink(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist drink object to drinks table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "scoreName": self.scoreName,
            "calories": self.calories
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, scoreName="", calories=0):
        """only updates values with length"""
        if len(scoreName) > 0:
            self.scoreName = scoreName
        if calories >= 0:
            self.calories = calories
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing """


# Builds working data for testing
def initScores():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        #d1 = Drink(drinkName='Coke', calories=10)
        #d2 = Drink(drinkName='Pepsi', calories=20)

        scorestoadd = []
        try:
            with open(r'scores.json','r') as json_file:
                data = json.load(json_file)
        except Exception as error:
            print("failed")

        for item in data:
            # print(item)
            d_toadd = Score(scoreName=item['scoreName'], calories=item['calories'])
            scorestoadd.append(d_toadd)

        """Builds sample user/note(s) data"""
        for d in scorestoadd:
            try:
                d.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {d.scorestoadd}")
            
