import os
from typing import cast, Optional
from flask import Flask
from dotenv import load_dotenv
from web.cache import cache
from web.views.web import web


basedir = os.path.abspath(os.path.dirname(__file__))

def create_app(config: Optional[dict] = None) -> Flask:
    lb_app = Flask(__name__)

    if not config:
        config = cast(dict, lb_app.env)

    ## lb_app.register_blueprint(api, url_prefix='/api')
    lb_app.register_blueprint(web)

    cache.init_app(app=lb_app)

    return lb_app

load_dotenv()
app = create_app(cast(dict, os.environ))