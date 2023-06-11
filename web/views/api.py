import os

from flask import Blueprint, jsonify, request
from dependency_injector.wiring import inject, Provide
from http.client import HTTPException

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

    res = {
        'code': 500,
        'errorType': 'Internal Server Error',
        'errorMessage': e.message if hasattr(e, 'message') else 'Something went really wrong!'
    }
    
    return jsonify(res), 500

@api.route('/projects/', methods=['GET'])
@inject
def get_projects(project_service: WorkspaceService = Provide[ApiContainer.project_service]):
    model = {
        'projects': project_service.get_all_projects(),
    }

    return jsonify(model)


@api.route('/projects/', methods=['POST'])
@inject
def create_project(project_service: WorkspaceService = Provide[ApiContainer.project_service]):
    request_data = request.get_json(force=True)

    settings = project_service.create(
        request_data['name']
    )

    return jsonify(settings)


@api.route('/projects/', methods=['DELETE'])
@inject
def delete_project(project_service: WorkspaceService = Provide[ApiContainer.project_service]):
    request_data = request.get_json(force=True)
    project_service.delete(
        request_data['name']
    )

    return jsonify({
        'status': 'deleted'
    })
