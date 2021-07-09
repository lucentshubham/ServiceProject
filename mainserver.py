from flask import Flask,render_template,request,session,abort
from flask.helpers import flash
from werkzeug.utils import redirect
import random
import json
from Database.databases import ServiceProvider,User,maindb as db 
from Doctor.main import db as doctor_db,app as doctor_app
app = Flask(__name__)
app.config["SECRET_KEY"] = "dfssdafasbsjcsdflhnvvbhflssdfhjsffrdees"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:kapil@localhost/service_provider_website"
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3306/service_provider_website"
db.__init__(app)
app.register_blueprint(doctor_app,url_prefix="/doctor")
doctor_db.__init__(app)
@app.route("/")
def home():
    user = None
    if "user" in session:
        user = session['user']
    return render_template("index.html",user = user)

@app.route("/login",methods = ["GET","POST"])
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


@app.route("/signup",methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("userlogin.html")
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        state=request.form.get("state")
        city=request.form.get("city")
        pass1 = request.form.get("pass1")
        pass2 = request.form.get("pass2")
        if pass1 == pass2:
            user = User(
                name = name,
                email = email,
                phone = phone,
                state = state,
                city = city,
                password = pass1
            )
            db.session.add(user)
            db.session.commit()
            print("add successfully")
        return render_template("userlogin.html")

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
        if request.form.get("experience") !="":
            user.experience = request.form.get("experience")
        else:
            user.experience = 0
        user.qualification = request.form.get("qualification")
        db.session.commit()
        print(user.city)
        flash("Profile Update")
        return redirect(f"/profile/{user.email}")

app.run(debug=True)