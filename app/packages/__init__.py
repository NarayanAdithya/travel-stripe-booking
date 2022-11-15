from flask import Blueprint

packages = Blueprint('package', __name__)

from . import routes, models