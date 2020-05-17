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
def register_blueprints(app):
    print('register_blueprints')
    from .controllers.user import user_api
    app.register_blueprint(user_api, url_prefix='/api/user')
def initialize_extensions(app):
    print('initialize_extensions')
    db.init_app(app)
    db.create_all(app=app)
    from .models.User import User
def setup(config):
    print('setup')
    app = create_app(config)
    register_blueprints(app)
    initialize_extensions(app)
    return app
