from app.packages import packages
from app.packages.models import Package
from flask_login import login_required
from flask import render_template, request


@packages.route('/packages')
def show_packages():
    p=Package.query.all()
    return render_template('packages.html',packages=p)

