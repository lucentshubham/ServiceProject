from flask import Blueprint,request,render_template,redirect,abort,flash,session
from ..Database.databases import ServiceProvider
from flask_sqlalchemy import SQLAlchemy
import random,json
app = Blueprint("Doctor",static_folder="static",template_folder="templates")
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
    pass

@app.route("/list")
def servicelist():
    jsonfile = open("../static/assets/data/categories_prof.json")
    jsondata = json.load(jsonfile)
    categories = jsondata["categories"]
    serviceproviders = ServiceProvider.query.all()
    return render_template("serviceproviderlist.html",providers = serviceproviders,categories = categories)

@app.route("/profile/edit",methods = ["GET",'POST'])
def ProfileEdit():
    if 'user' not in session:
        return abort(404)
    user = ServiceProvider.query.filter_by(email = session['user']['email']).first()
    if user.profession != "Doctor":
        abort(404)
    if request.method == "GET":
        return render_template("editProfile.html",user = user)
    if request.method == "POST":
        user.name = request.form.get("name")
        user.phone = request.form.get("phone")
        user.address = request.form.get("address")
        user.profession = request.form.get("profession")
        user.category = request.form.get("category")
        user.state = request.form.get("state")
        user.city = request.form.get("city")
        user.speciality = request.form.get("speciality")
        user.experience = request.form.get("experience")
        user.qualification = request.form.get("qualification")
        db.session.commit()
        flash("Profile Update")
        return redirect(f"/profile/{user.email}")