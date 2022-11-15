from flask import Flask, redirect, url_for
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

## general configs
app=Flask(__name__)
app.config.from_object(config)


## DB Configs
db=SQLAlchemy(app)
migrate=Migrate(app,db)


## Flask Admin
admin = Admin(app, name='Kite India Admin DashBoard',template_mode='bootstrap4')

## Login Configs
login=LoginManager(app)
login.login_view='auth.loginUser'
login.message='Please Login To Access The Page'
login.login_message_category='info'


## Blueprint Registrations
from app.auth import auth
from app.home import home
from app.packages import packages
from app.transactions import transaction

app.register_blueprint(home,url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(packages,url_prefix='/package')
app.register_blueprint(transaction,url_prefix='/transaction')

#Adding Admin Views

from app.auth.models import User
from app.packages.models import Package
from app.transactions.models import Booking


class Kite(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.isAdmin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login'))

admin.add_view(Kite(User, db.session))
admin.add_view(Kite(Package, db.session,endpoint='package_'))
admin.add_view(Kite(Booking, db.session))
with app.app_context():
    db.create_all()