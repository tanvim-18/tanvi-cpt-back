from flask import Flask, render_template, request
from flask_cors import CORS
from flask.cli import AppGroup
from model.users import initUsers
from model.players import initPlayers
from model.highscores import db
from api.highscores import memory_highscores_api

app = Flask(__name__)

# Enable CORS
CORS(app)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///highscores.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

# Register API blueprint
app.register_blueprint(memory_highscores_api)

@app.route('/')
def index():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Define a command to generate data
custom_cli = AppGroup('custom', help='Custom commands')

@custom_cli.command('generate_data')
def generate_data():
    initUsers()
    initPlayers()

# Register the custom command group
app.cli.add_command(custom_cli)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
