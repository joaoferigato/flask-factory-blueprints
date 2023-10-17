from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()

# Flask extension objects instantiation
# db = SQLAlchemy()
# executor = Executor()

# Application Factory
def create_app():
    app = Flask(__name__)

    # Configure the flask app instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)

    # Register blueprints
    register_blueprints(app)

    # Initialize flask extension objects
    initialize_extensions(app)

    # Configure logging
    configure_logging(app)

    # Register error handlers
    register_error_handlers(app)

    return app


### Helper Functions ###
def register_blueprints(app):
    from app.main import main_blueprint
    from app.functionality import functionality_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(functionality_blueprint, url_prefix='/functionality')


def initialize_extensions(app):
    # executor.init_app(app)
    pass


def register_error_handlers(app):
    # 400 - Bad Request
    @app.errorhandler(400)
    def bad_request(error):
        return ''

    # 403 - Forbidden
    @app.errorhandler(403)
    def forbidden(error):
        return ''

    # 404 - Page Not Found
    @app.errorhandler(404)
    def page_not_found(error):
        return ''

    # 405 - Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(error):
        return ''

    # 500 - Internal Server Error
    @app.errorhandler(500)
    def server_error(error):
        return ''


def configure_logging(app):
    from app.logs import initialize_log
    import logging

    initialize_log()
    log = logging.getLogger('app_log')
    log.info('Starting Application')
