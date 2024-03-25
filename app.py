from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.time_api import time_api

# Create Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fastest_times.db'  # Example SQLite URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy instance
db = SQLAlchemy(app)

# Register time API Blueprint
app.register_blueprint(time_api)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
