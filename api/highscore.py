from flask import Flask, request, jsonify

app = Flask(__name__)

# Data structure to store game scores
scores = {}


# Endpoint to add a new game score
@app.route('/score', methods=['POST'])
def add_score():
    data = request.json
    game_id = data.get('game_id')
    player_name = data.get('player_name')
    score = data.get('score')

    if not game_id or not player_name or not score:
        return jsonify({'error': 'Missing data. Please provide game_id, player_name, and score.'}), 400

    if game_id not in scores:
        scores[game_id] = []

    scores[game_id].append({'player_name': player_name, 'score': score})

    return jsonify({'message': 'Score added successfully.'}), 201


# Endpoint to get all scores for a particular game
@app.route('/scores/<int:game_id>', methods=['GET'])
def get_scores(game_id):
    if game_id not in scores:
        return jsonify({'error': 'No scores found for the specified game ID.'}), 404

    return jsonify(scores[game_id])


if __name__ == '__main__':
    app.run(debug=True)

