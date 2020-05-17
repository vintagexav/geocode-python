from flask import Flask
from .models.db import db
from .utils.error import error_404

# ======
# APP
# ======
def create_app(config_file=None):
    print('create_app')
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    @app.errorhandler(404)
    def handler_error_404(error):
        return error_404('main', error)
    return app
def initialize_extensions(app):
    print('initialize_extensions')
    db.init_app(app)
    db.create_all(app=app)
    from .models.User import User
def setup(config):
    print('setup')
    app = create_app(config)
    initialize_extensions(app)
    return app
