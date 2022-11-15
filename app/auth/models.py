from app import db, app, login
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from app.transactions.models import Booking


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# User:
# id - String PK
# first_name - String
# last_name - String
# phone - String
# email - URL Field
# sex  - String
# profile_img - String
# password - String
# registered_trips: Callback to registrations FK  Array


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(128))
    email=db.Column(db.String(120),index=True,unique=True)
    phone=db.Column(db.String(120),unique=True)
    isOAuth=db.Column(db.Boolean)
    password_hash=db.Column(db.String(128))
    isAdmin=db.Column(db.Boolean)
    sex=db.Column(db.String(10))
    profimg=db.Column(db.String(256))
    def __repr__(self):
        return '<Name:{} Id:{}>'.format(self.name,self.id)
    def set_password(self,password):
        self.password_hash=generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
