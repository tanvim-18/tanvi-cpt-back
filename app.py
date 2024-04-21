from flask import Flask
from model.scorey import db
from api.score import score_api

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scores.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy instance
db.init_app(app)

# Register API blueprints
app.register_blueprint(score_api)

if __name__ == '__main__':
    app.run(debug=True)