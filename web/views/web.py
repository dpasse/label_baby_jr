import os
from flask import Blueprint, render_template, jsonify

from web.cache import cache


web = Blueprint('web', __name__, template_folder='templates')

@web.route('/', defaults={'path': ''}, methods=['GET'])
@web.route('/<path:path>', methods=['GET'])
@cache.cached(timeout=50)
def index(path: str) -> str:
    model = {
        'version': os.getenv('VERSION'),
        'path': path,
    }

    return render_template('index.html', model=model)

@web.route('/heartbeat', methods=['GET'])
def heartbeat():
    model = {
        'status': 'healthy'
    }

    return jsonify(model)
