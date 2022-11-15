import os
from dotenv import load_dotenv
print(load_dotenv())

class config(object):
    SECRET_KEY= os.environ.get('SECRET_KEY') or '334nadnj&&89Ydau89YAd98adbszmdi3*&&923kln'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'sqlite:///'+os.getcwd()+'/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    GOOGLE_CLIENT_ID=os.environ.get('CLIENT_ID')
    GOOGLE_CLIENT_SECRET=os.environ.get('CLIENT_SECRET')
    FLASK_ADMIN_SWATCH='cerulean'