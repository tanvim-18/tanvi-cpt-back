import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource  # Add this import

score_api = Blueprint('score_api', __name__, url_prefix='/api/scores')
api = Api(score_api)

# Load highscores data from the JSON file
with open('highscores.json', 'r') as json_file:
    highscores_data = json.load(json_file)

class HighscoreAPI(Resource):  # Modify class name to match the imported Resource
    def post(self):
        body = request.get_json()
        user_time = body.get('user_time')
        if not user_time or not isinstance(user_time, int):
            return {'message': 'Invalid user time. Please provide a valid integer.'}, 400
        
        score = None
        for data in highscores_data:
            if data["user_time"] == user_time:
                score = data["score"]
                break
        
        if score is not None:
            return {'message': score}, 200
        else:
            return {'message': 'No score found for the provided user time.'}, 404

api.add_resource(HighscoreAPI, '/')  # Register the Resource with the Api

# You still need to register the blueprint with your Flask app
# app.register_blueprint(score_api)
