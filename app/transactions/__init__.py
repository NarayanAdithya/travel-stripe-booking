from flask import Blueprint
import stripe
import os

stripe_keys={
    "secret_key":os.environ.get('STRIPE_SECRET_KEY'),
    "publishable_key":os.environ.get('STRIPE_PUBLISHABLE_KEY')
}

stripe.api_key=stripe_keys['secret_key']
transaction = Blueprint('transaction', __name__)

from . import routes, models