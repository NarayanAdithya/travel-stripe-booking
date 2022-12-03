from app.transactions import transaction, client
from app.transactions.models import Booking, Passenger
from app import db
from flask_login import login_required, current_user
from app.packages.models import Package
from flask import request, render_template, redirect, url_for, abort, flash
import os
import pickle


@transaction.route('/package/book/<int:id>',methods=['GET','POST'])
@login_required
def book_package(id):
    p=Package.query.filter_by(id=id).first()
    accompanying=[]
    if Booking.query.filter_by(user_id=current_user.id,package_id=p.id,Status='paid').first():
        flash('A Successful Booking for This Package Already Exists')
        return redirect(url_for('package.show_packages'))
    if request.method=="POST":
        for name,age,sex in zip(request.form.getlist('name'),request.form.getlist('age'),request.form.getlist('sex')):
            a={'name':name,'age':age,'sex':sex}
            accompanying.append(a)
        u=Booking(user_id=current_user.id,package_id=p.id,numOfAccompanying=int(request.form['numberofpeople']),Cost=(int(request.form['numberofpeople'])+1)*p.cost,Status='tbd',checkout_id='tbd')
        u.contactno=request.form['phno']
        db.session.add(u)
        db.session.commit()
        for a in accompanying:
            p=Passenger(package_id=u.id,name=a['name'],age=a['age'],sex=a['sex'])
            db.session.add(p)
            db.session.commit()
        return redirect(url_for('transaction.make_payment',id=u.id))
    return render_template('book_package.html',package=p)

@transaction.route('/payment/<int:id>',methods=['POST','GET'])
@login_required
def make_payment(id):
    b=Booking.query.filter_by(id=id).first()
    data = { "amount": b.Cost*100, "currency": "INR", "receipt": "booking"+str(b.id)+"_"+str(b.package.id), "payment_capture":"1" }
    payment = client.order.create(data=data)
    b.checkout_id=payment['id']
    b.status=payment['status']
    db.session.add(b)
    db.session.commit()
    return render_template('make_payment.html', key=os.environ.get('RAZORPAY_ID'), amount=b.Cost,order_id=payment['id'])

@transaction.route('/success', methods=['GET','POST'])
@login_required
def transaction_success():
    if request.method=='POST':
        print(request.data)
    return render_template('transaction_success.html')

@transaction.route('/cancel')
@login_required
def transaction_failed():
    return render_template('transaction_cancel.html')

@transaction.route('/stripe_webhook',methods=['POST'])
def stripe_webhook():
    print("EVENT TRIGGERED")
    event = None
    if request.content_length>1024*1024:
        print("REQUEST TOO BIG")
        abort(400)
    payload = request.get_data()
    sig_header = request.environ.get('HTTP_STRIPE_SIGNATURE')
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, os.environ.get('ENDPOINT_SECRET')
        )
    except ValueError as e:
        # Invalid payload
        print("Invalid Payload")
        return {},400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print("Invalid Signature")
        return {},400

    if event['type']=='checkout.session.completed':
        session = event['data']['object']
        b=Booking.query.filter_by(checkout_id=session.id).first()
        b.Status=session.payment_status
        db.session.add(b)
        db.session.commit()
    return {},200