from app import app,db
from app.auth.models import User
from app.packages.models import Activities, Package
from app.transactions.models import Booking

# Flask Shell Command Gives Access to DataBase Manipulation Facilated Through Flask SQLAlchemy
@app.shell_context_processor
def make_shell_context():
    return {'db':db,'user':User,'package':Package,'activity':Activities,'booking':Booking}


if __name__ == '__main__':
    app.run()
