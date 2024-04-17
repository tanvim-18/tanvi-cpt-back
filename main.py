from flask import Flask
from model import db
from model.scores import Highscore
import json

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///highscores.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy instance
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

    # Read data from highscores.json and insert into the database
    with open('highscores.json', 'r') as json_file:
        highscores_data = json.load(json_file)

    for data in highscores_data:
        user_time = data["user_time"]
        score = data["score"]
        highscore = Highscore(user_time=user_time, score=score)
        db.session.add(highscore)

    db.session.commit()
