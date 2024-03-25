# api/memory_highscores.py
from flask import Blueprint, request, jsonify
from model.highscores import MemoryHighScore, db

memory_highscores_api = Blueprint('memory_highscores_api', __name__, url_prefix='/api/memory_highscores')

@memory_highscores_api.route('/', methods=['POST'])
def submit_memory_highscore():
    data = request.get_json()
    username = data.get('username')
    completion_time = data.get('completion_time')

    if not username or not completion_time:
        return jsonify({'message': 'Username or completion time is missing'}), 400

    highscore_entry = MemoryHighScore(username=username, completion_time=completion_time)
    db.session.add(highscore_entry)
    db.session.commit()

    return jsonify({'message': 'High score submitted successfully'}), 201

@memory_highscores_api.route('/', methods=['GET'])
def get_top_memory_highscores():
    top_highscores = MemoryHighScore.query.order_by(MemoryHighScore.completion_time).limit(10).all()
    highscores_data = [score.to_dict() for score in top_highscores]
    return jsonify(highscores_data)
