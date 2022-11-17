from app import db, app, login
from app.transactions.models import Booking
from flask_login import UserMixin
from datetime import datetime



class Package(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(256))
    contact=db.Column(db.String(256))
    location=db.Column(db.String(256))
    cost=db.Column(db.Float(2))
    small_description=db.Column(db.String(256))
    details_file=db.Column(db.String(512))
    stripe_id=db.Column(db.String(200),nullable=False,unique=True)
    activities=db.relationship('Activities',backref='package',lazy=True)
    image=db.Column(db.String(512))
    users=db.relationship("User",secondary="booking",viewonly=True)
    def __repr__(self):
        return f"<Package {self.name} {self.id}>"

    def __str__(self):
        return f"The {self.name} Package at {self.location} consists of the following activities {','.join([act.name for act in self.activities])} at the cost of {self.cost} per person."
        

class Activities(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(120), nullable=False)
    small_desc=db.Column(db.String(120))
    package_id=db.Column(db.Integer, db.ForeignKey('package.id'),nullable=False)
    def __repr__(self) :
        return f"<Activity id:{self.id} name:{self.name}>"
    def __str__(self):
        return f"{self.name}"
