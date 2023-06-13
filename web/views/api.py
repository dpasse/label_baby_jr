from flask import Blueprint, jsonify, request
from dependency_injector.wiring import inject, Provide
from http.client import HTTPException

from ..common.exceptions import NotFoundError
from ..containers import ApiContainer
from ..services import WorkspaceService


api = Blueprint('api', __name__, template_folder='templates')

@api.route('/heartbeat', methods=['GET'])
def heartbeat():
    model = {
        'status': 'healthy'
    }

    return jsonify(model)

@api.errorhandler(Exception)
def handle_exception(e):
    print(e)

    if isinstance(e, HTTPException):
        return e
    
    code = 500
    if isinstance(e, NotFoundError):
        code = 404
    
    message = e.message if hasattr(e, 'message') else 'Something went really wrong!'

    res = {
        'code': code,
        'errorMessage': message
    }
    
    return jsonify(res), code

@api.route('/projects/<identifier>/', methods=['GET'])
@inject
def get_project(identifier: str, project_service: WorkspaceService = Provide[ApiContainer.project_service]):
    model = project_service.get_project(identifier)
    if model is None:
        raise NotFoundError(message="Project not found")

    return jsonify(model)

@api.route('/projects/', methods=['POST'])
@inject
def create_project(project_service: WorkspaceService = Provide[ApiContainer.project_service]):
    request_data = request.get_json(force=True)

    settings = project_service.create(
        request_data['name']
    )

    return jsonify(settings)

@api.route('/projects/', methods=['GET'])
@inject
def get_projects(project_service: WorkspaceService = Provide[ApiContainer.project_service]):
    return jsonify(
        project_service.get_all_projects()
    )

@api.route('/projects/<identifier>/', methods=['DELETE'])
@inject
def delete_project(identifier: str, project_service: WorkspaceService = Provide[ApiContainer.project_service]):
    project_service.delete(identifier)

    return jsonify({
        'status': 'deleted'
    })
