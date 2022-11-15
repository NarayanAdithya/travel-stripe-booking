from app import db
from flask_login import UserMixin
from datetime import datetime



class Booking(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    package_id=db.Column(db.Integer,db.ForeignKey('package.id'))
    numOfAccompanying=db.Column(db.Integer,nullable=False)
    Cost=db.Column(db.Float(2),nullable=False)
    Status=db.Column(db.String(20),nullable=False)
    checkout_id=db.Column(db.String(512),nullable=False)
    Accompanying=db.Column(db.PickleType(),nullable=False)
    package=db.relationship("Package",backref="associated_user")
    user=db.relationship("User",backref="associated_package")