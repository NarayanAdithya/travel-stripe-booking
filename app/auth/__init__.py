from flask import Blueprint
from oauthlib.oauth2 import WebApplicationClient
import os

auth = Blueprint('auth', __name__)
client = WebApplicationClient(os.environ.get('CLIENT_ID'))

from . import routes, models