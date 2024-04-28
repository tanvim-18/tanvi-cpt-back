import json
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource
from datetime import datetime
#from auth_middleware import token_required

from model.scorey import Score

score_api = Blueprint('score_api', __name__, url_prefix='/api/score')

api = Api(score_api)

class ScoreAPI:
    class _CRUD(Resource):
        #@token_required
        def post(self, current_user):
            body = request.get_json()
            user_time = body.get('user_time')
            if user_time is None or len(user_time) < 1:
                return {'message': f'Time is missing, or is less than 1 characters'}, 400
            
            # Adjustments for score data
            id = body.get('id')
            name = request.get_json()            
            user_time = body.get('user_time')            
            feedback = body.get('feedback')

            # Create score object
            score_data = {
                'id': id,
                'name': name,
                'user_time': user_time,
                'feedback': feedback,

            }
            new_score_record = Score(**score_data)

            # Example: saving to database
            new_score_record.save()

            return jsonify({'message': 'Score data saved successfully'}), 201

        def get(self):#, current_user):
            # Example: Retrieving score data
            score_records = Score.query.all()
            json_ready = [record.serialize() for record in score_records]
            return jsonify(json_ready)

    api.add_resource(_CRUD, '/')



