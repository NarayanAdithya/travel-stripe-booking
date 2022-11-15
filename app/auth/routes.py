from app import  app,db, login
import sqlalchemy
from flask_login import current_user,login_user,logout_user,login_required
from datetime import datetime
from flask import request,redirect,url_for,render_template,flash,get_flashed_messages,flash,jsonify
from .models import User
from werkzeug.urls import url_parse
from app.auth import auth, client
import os
import requests
import json

def get_google_provider_cfg():
    return requests.get(os.environ.get('GOOGLE_DISCOVERY_URL')).json()

@auth.route('/home')
def home():
    return render_template('home.html')

@auth.route('/logout')
def logout():
    current_user.last_seen=datetime.utcnow()
    db.session.commit()
    logout_user()
    return redirect(url_for('auth.home'))

@auth.route('/googlelogin')
def logingoogle():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    print(request.base_url)
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri= url_for('auth.callback'),
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@auth.route('/callback')
def callback():
    code = request.args.get("code")
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(os.environ.get('CLIENT_ID'), os.environ.get('CLIENT_SECRET')),
    )
    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    users_email = userinfo_response.json()["email"]
    picture = userinfo_response.json()["picture"]
    users_name = userinfo_response.json()["given_name"]
    u=User.query.filter_by(email=users_email).first() 
    if not u:
        print("User Not Registered Yet")
        u=User(name=users_name, email=users_email, isOAuth=True, profimg=picture)
        db.session.add(u)
        db.session.commit()
    login_user(u)
    return redirect(url_for('home.home'))
    
@auth.route('/login',methods=['GET','POST'])
def loginUser():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))
    if request.method=='POST':
        user=User.query.filter_by(email=request.form['email']).first()
        if user is None:
            flash('Account Does Not Exist | Create Account Here',category="danger")
            return redirect(url_for('auth.register'))
        if user.isOAuth:
            return redirect(url_for('auth.logingoogle')) 
        if user.check_password(request.form['password']):
            flash('Invalid Email or Password ',category="danger")
            return redirect(url_for('auth.loginUser'))
        login_user(user)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc!='':
            next_page=url_for('home.home')
        return redirect(next_page)
    return render_template('signin.html')


@auth.route('/register',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))
    if request.method=='POST':
        u=User.query.filter_by(email=request.form['email']).first()
        if u:
            flash('User Already Registered, Please Login',category="danger")
            return redirect(url_for('auth.loginUser'))
        user=User(name=request.form['name'],email=request.form['email'],isOAuth=False)
        user.set_password(request.form['password'])
        db.session.add(user)
        db.session.commit()
        flash('Successfully Registered',category="success")
        return redirect(url_for('auth.loginUser'))
    return render_template('signup.html')


@auth.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

# @auth.route("/reset_password", methods=['GET', 'POST'])
# def reset_request():
#     # if current_user.is_authenticated:
#     #     return redirect(url_for('index'))
#     # form = RequestResetForm()
#     # if form.validate_on_submit():
#     #     user = User.query.filter_by(email=form.email.data).first()
#     #     send_reset_email(user)
#     #     flash('An email has been sent with instructions to reset your password.', 'info')
#     #     return redirect(url_for('auth.loginUser'))
#     return render_template('reset_request.html', title='Reset Password')


