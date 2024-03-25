import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

score_api = Blueprint('score_api', __name__, url_prefix='/api/scores')
api = Api(score_api)

class HighscoreAPI:
    class _CRUD(Resource):
        def post(self):
            body = request.get_json()
            user_time = body.get('user_time')
            if not user_time or not isinstance(user_time, int):
                return {'message': 'Invalid user time. Please provide a valid integer.'}, 400
            
            if 1 <= user_time <= 10:
                return {'message': 'Amazing!'}, 200
            elif 11 <= user_time <= 20:
                return {'message': 'Very Good!'}, 200
            elif 21 <= user_time <= 30:
                return {'message': 'OK.'}, 200
            elif 31 <= user_time <= 40:
                return {'message': 'Good.'}, 200
            elif 41 <= user_time <= 50:
                return {'message': 'Improving.'}, 200
            elif 51 <= user_time <= 60:
                return {'message': 'Need Improvement.'}, 200
            else:
                return {'message': 'Your time is beyond the expected range.'}, 200

    api.add_resource(_CRUD, '/')
