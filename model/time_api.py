# Import necessary modules
from flask import Blueprint, request, jsonify
from model.fastest_times import FastestTime

# Create Blueprint for time API
time_api = Blueprint('time_api', __name__, url_prefix='/api/fastest_times')

# Define API endpoints
@time_api.route('/', methods=['GET', 'POST'])
def fastest_times():
    if request.method == 'POST':
        # Read data from JSON body
        data = request.get_json()
        username = data.get('username')
        time = data.get('time')

        # Validate data
        if not username or not time:
            return jsonify({'message': 'Username and time are required'}), 400

        # Create new fastest time entry
        new_fastest_time = FastestTime(username=username, time=time)
        created_time = new_fastest_time.create()

        if created_time:
            return jsonify(created_time), 201
        else:
            return jsonify({'message': 'Failed to create fastest time'}), 500

    elif request.method == 'GET':
        # Retrieve all fastest times
        fastest_times = FastestTime.query.all()
        fastest_times_json = [time.to_dict() for time in fastest_times]
        return jsonify(fastest_times_json)

# Import API in your Flask application
# from api.time_api import time_api
# app.register_blueprint(time_api)
