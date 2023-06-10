from flask import Blueprint, jsonify


api = Blueprint('api', __name__, template_folder='templates')

@api.route('/heartbeat', methods=['GET'])
def heartbeat():
    model = {
        'status': 'healthy'
    }

    return jsonify(model)
