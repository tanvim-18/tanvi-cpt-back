from flask import Flask
from model.scores import db
from api.scores import memory_highscores_api

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///highscores.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy instance
db.init_app(app)

# Register API blueprints
app.register_blueprint(memory_highscores_api)

if __name__ == '__main__':
    app.run(debug=True)