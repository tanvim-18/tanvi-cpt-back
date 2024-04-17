import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
#from auth_middleware import token_required

# Create a SQLAlchemy object
db = SQLAlchemy()

from model.scores import Score

score_api = Blueprint('score_api', __name__,
                   url_prefix='/api/scores')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(score_api)

class ScoreyAPI:        
    class _CRUD(Resource):  # User API operation for Create, Read.  THe Update, Delete methods need to be implemeented
        def post(self): # Create method
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate drinkName
            scoreName = body.get('scoreName')
            if scoreName is None or len(scoreName) < 2:
                return {'message': f'scoreName is missing, or is less than 2 characters'}, 400
            # validate uid
            calories = body.get('calories')
            if calories is None or calories < 0 :
                return {'message': f'calories has to be positive number'}, 400

            ''' #1: Key code block, setup USER OBJECT '''
            newScore = Score(scoreName=scoreName, 
                      calories=calories)
            
            ''' #2: Key Code block to add user to database '''
            # create drink in database
            just_added_score = newScore.create()
            # success returns json of user
            if just_added_score:
                return jsonify(just_added_score.read())
            # failure returns error
            return {'message': f'Processed {scoreName}, either a format error or it is duplicate'}, 400
    
        def get(self): # Read Method
            scores = scores.query.all()    # read/extract all users from the database
            json_ready = [score.read() for score in scores]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
        
        def delete(self):  # Delete method
            body = request.get_json()
            del_score = body.get('scoreName')
            result = Score.query.filter(Score._scoreName == del_score).first()
            if result is None:
                 return {'message': f'score {del_score} not found'}, 404
            else:
                result.delete()
                print("delete")
            
           # del_found = Score.query.get(del_drink)
            # print(del_found)
            # if del_found is None:
            #     return {'message': f'drink {del_drink} not found'}, 404
            # else:
            #     del_found.delete()
    
    
    class _get(Resource):
        
        def get(self, lname=None):  # Updated method with lname parameter
            #lname="'" + lname + "'"
            print(lname)
            if lname:
                result = Score.query.filter_by(_scoreName=lname).first()
                #result = Drink.query.filter(Drink._drinkName == lname).first()
                #result = Drink.query.first_or_404(lname)  # Adjust this based on your model attributes
                print(result)
                if result:
                    print(result)
                    return jsonify([result.read()])  # Assuming you have a read() method in your DrinkyApi model
                else:
                    return jsonify({"message": "Score not found"}), 404


    # class _update(Resource):
    #     def put(self, id):  # Update method
    #         ''' Read data for json body '''
    #         body = request.get_json()

    #         ''' Find user by ID '''
    #         user = User.query.get(id)
    #         if user is None:
    #             return {'message': f'User with ID {id} not found'}, 404

    #         ''' Update fields '''
    #         name = body.get('name')
    #         if name:
    #             user.name = name
                
    #         uid = body.get('uid')
    #         if uid:  
    #             user.uid = uid
                
    #         user.server_needed = body.get('server_needed')

    #         user.active_classes = body.get('active_classes')
    #         user.archived_classes = body.get('archived_classes')

    #         ''' Commit changes to the database '''
    #         user.update()
    #         return jsonify(user.read())
    
   
  
    # class _Security(Resource):
    #     def post(self):
    #         try:
    #             body = request.get_json()
    #             if not body:
    #                 return {
    #                     "message": "Please provide user details",
    #                     "data": None,
    #                     "error": "Bad request"
    #                 }, 400
    #             ''' Get Data '''
    #             uid = body.get('uid')
    #             if uid is None:
    #                 return {'message': f'User ID is missing'}, 400
    #             password = body.get('password')
                
    #             ''' Find user '''
    #             user = User.query.filter_by(_uid=uid).first()
    #             if user is None or not user.is_password(password):
    #                 return {'message': f"Invalid user id or password"}, 400
    #             if user:
    #                 try:
    #                     token = jwt.encode(
    #                         {"_uid": user._uid},
    #                         current_app.config["SECRET_KEY"],
    #                         algorithm="HS256"
    #                     )
    #                     resp = Response("Authentication for %s successful" % (user._uid))
    #                     resp.set_cookie("jwt", token,
    #                             max_age=3600,
    #                             secure=True,
    #                             httponly=True,
    #                             path='/',
    #                             samesite='None'  # This is the key part for cross-site requests

    #                             # domain="frontend.com"
    #                             )
    #                     return resp
    #                 except Exception as e:
    #                     return {
    #                         "error": "Something went wrong",
    #                         "message": str(e)
    #                     }, 500
    #             return {
    #                 "message": "Error fetching auth token!",
    #                 "data": None,
    #                 "error": "Unauthorized"
    #             }, 404
    #         except Exception as e:
    #             return {
    #                     "message": "Something went wrong!",
    #                     "error": str(e),
    #                     "data": None
    #             }, 500

            
    # building RESTapi endpoint
    api.add_resource(_CRUD, '/')
    api.add_resource(_get, '/<string:lname>')
    #api.add_resource(_Security, '/authenticate')
    
    