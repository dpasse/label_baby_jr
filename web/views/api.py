import os

from flask import Blueprint, jsonify, request
from http.client import HTTPException

from ..services import ProjectService


api = Blueprint('api', __name__, template_folder='templates')

@api.route('/heartbeat', methods=['GET'])
def heartbeat():
    model = {
        'status': 'healthy'
    }

    return jsonify(model)

@api.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e

    res = {
        'code': 500,
        'errorType': 'Internal Server Error',
        'errorMessage': e.message if hasattr(e, 'message') else 'Something went really wrong!'
    }
    
    return jsonify(res), 500

@api.route('/projects/', methods=['GET'])
def get_projects():
    projects = ProjectService().get_all(
        os.getenv('WORKSPACE_DIRECTORY')
    )

    model = {
        'projects': projects,
    }

    return jsonify(model)

@api.route('/projects/', methods=['POST'])
def create_project():
    project_data = request.get_json(force=True)
    settings = ProjectService().create(
        os.getenv('WORKSPACE_DIRECTORY'),
        project_data['name']
    )

    return jsonify(settings)
