from flask import Flask
from .models.db import db
from .utils.error import error_404
from .models.User import User
from .models.Vehicle import Vehicle
from .models.Booking import Booking
from .controllers.user import user_api
from .controllers.vehicle import vehicle_api
from .controllers.booking import booking_api
from .controllers.files import files

# ======
# APP
# ======
def create_app(config_file=None):
    print('create_app')
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    @app.errorhandler(404)
    def handler_error_404(error):
        return error_404('main', error), 400
    return app
def register_blueprints(app):
    print('register_blueprints')
    api = '/api'
    app.register_blueprint(user_api, url_prefix='%s/user' % api)
    app.register_blueprint(vehicle_api, url_prefix='%s/vehicle' % api)
    app.register_blueprint(booking_api, url_prefix='%s/booking' % api)
    app.register_blueprint(files, url_prefix='/files')
def initialize_extensions(app):
    print('initialize_extensions')
    db.init_app(app)
    db.create_all(app=app)
def setup(config):
    print('setup')
    app = create_app(config)
    register_blueprints(app)
    initialize_extensions(app)
    return app
