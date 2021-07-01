from flask import Flask,render_template,request,session,abort
from flask.helpers import flash
from werkzeug.utils import redirect
import random
import json
from Database.databases import ServiceProvider,Appointment,Admin,User,Ratings,Reviews,maindb as db 
app = Flask(__name__)
app.config["SECRET_KEY"] = "dfssdafasbsjcsdflhnvvbhflssdfhjsffrdees"
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:kapil@localhost/service_provider_website"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3306/service_provider_website"
db.__init__(app)


@app.route("/")
def home():
    user = None
    if "user" in session:
        user = session['user']
    return render_template("index.html",user = user)

@app.route("/user/login",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("userlogin.html")
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email = email).first()
        if user:
            if user.password == password:
                session['user'] = {"name":user.name,"email":user.email}
                return redirect("/")
        return render_template("userlogin.html")

@app.route("/dr/login",methods = ["GET","POST"])
def drlogin():
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

@app.route("/user/signup",methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("userlogin.html")
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        pass1 = request.form.get("pass1")
        pass2 = request.form.get("pass2")
        if pass1 == pass2:
            user = User(
                name = name,
                email = email,
                phone = phone,
                password = pass1
            )
            db.session.add(user)
            db.session.commit()
            print("add successfully")
        return render_template("userlogin.html")

@app.route('/dr/signup', methods=['GET','POST'])
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



@app.route("/logout")
def logout():
    try:
        session.pop("user")
    except:
        pass
    return redirect("/")

@app.route('/profile/<string:email>')
def profile(email):
    user  = ServiceProvider.query.filter_by(email = email).first()
    if not user:
        user = User.query.filter_by(email = email).first()
    curr_user = None
    if 'user' in session:
        curr_user = session['user']
    if user:
        return render_template('profile.html',user = user,curr_user = curr_user)
    return abort(404)

@app.route("/profile/edit",methods = ["GET",'POST'])
def ProfileEdit():
    if 'user' not in session:
        return abort(404)
    user = ServiceProvider.query.filter_by(email = session['user']['email']).first()
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
    jsonfile = open("./static/assets/data/categories_prof.json")
    jsondata = json.load(jsonfile)
    categories = jsondata["professions"]
    serviceproviders = ServiceProvider.query.all()
    return render_template("serviceproviderlist.html",providers = serviceproviders,categories = categories)

app.run(debug=True)