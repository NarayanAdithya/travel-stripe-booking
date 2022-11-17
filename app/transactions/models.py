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
    package=db.relationship("Package",backref="associated_bookings")
    user=db.relationship("User",backref="associated_bookings")
    passengers=db.relationship("Passenger",backref="package")

class Passenger(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120))
    package_id=db.Column(db.Integer, db.ForeignKey('booking.id'),nullable=False)
    age=db.Column(db.Integer)
    sex=db.Column(db.String(50))
    def __repr__(self):
        return f"{self.name}"
