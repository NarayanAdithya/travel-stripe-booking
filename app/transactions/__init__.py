from flask import Blueprint
import razorpay
import os

client = razorpay.Client(auth=(os.enviorn.get('RAZORPAY_ID'),os.environ.get('RAZORPAY_SECRET_KEY')))

transaction = Blueprint('transaction', __name__)

from . import routes, models