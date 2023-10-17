from flask import Blueprint

functionality_blueprint = Blueprint('functionality', __name__, template_folder='templates')

from . import views