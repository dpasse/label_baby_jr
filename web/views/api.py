import os

from flask import Blueprint, jsonify
from ..services import ProjectService


api = Blueprint('api', __name__, template_folder='templates')

@api.route('/heartbeat', methods=['GET'])
def heartbeat():
    model = {
        'status': 'healthy'
    }

    return jsonify(model)

@api.route('/projects/', methods=['GET'])
def get_projects():
    projects = ProjectService(
        os.getenv('WORKSPACE_DIRECTORY')
    ).get()

    model = {
        'projects': projects,
    }

    return jsonify(model)
