from flask import Blueprint,request,render_template,redirect,abort,flash,session
from Database.databases import Appointment, ServiceProvider
from flask_sqlalchemy import SQLAlchemy
import random,json
from datetime import datetime
app = Blueprint(__file__,"doctor_app",static_folder="static",template_folder="Doctor/templates")
db = SQLAlchemy()

@app.route('/signup', methods=['GET','POST'])
def drsignup():
    if request.method=="GET":
        return render_template('login_signup.html')
    if request.method =="POST":
        name=request.form.get("name")
        category=request.form.get("category")
        profession=request.form.get("profession")
        phone=request.form.get("phone")
        email=request.form.get("email")
        pass1=request.form.get("pass1")
        pass2=request.form.get("pass2")
        if pass1==pass2:
            servpr=ServiceProvider(
                name=name,
                category=category,
                profession=profession,
                phone=phone,
                email=email,
                password=pass1
            )
            db.session.add(servpr)
            db.session.commit()
            flash('signup successfully')
        return render_template('login_signup.html')


@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login_signup.html")
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = ServiceProvider.query.filter_by(email = email).first()
        if user:
            if user.password == password:
                session['user'] = {"name":user.name,"email":user.email}
                return redirect("/")
        return render_template("login_signup.html")




@app.route("/dashboard/<string:id>",methods=["GET",'POST'])
def dashboard(id):
    doctor = ServiceProvider.query.filter_by(sno = id).first()
    if doctor and doctor.profession.casefold() == "doctor":
        return render_template('dashboard.html',doctor = doctor)
    return abort(404)

@app.route("/appointment",methods = ["POST"])
def appointment():
    samples = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
               'w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
               'S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9'
              ]
    appointment_id = ''.join(random.sample(samples,5))
    appoint = Appointment(
        name = request.form.get("name"),
        phone = request.form.get("phone"),
        time = request.form.get("date"),
        dr_id = request.form.get("dr_id"),
        appoitmnt_id = appointment_id
    )
    db.session.add(appoint)
    db.session.commit()
    return f"Appointment success. Your appointent id is {appointment_id}"

@app.route("/list")
def servicelist():
    doctors = ServiceProvider.query.all()
    return render_template("serviceproviderlist.html",doctors = doctors)

