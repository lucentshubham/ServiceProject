import re
from flask import Flask,render_template,request,session,abort
from flask.helpers import flash
from sqlalchemy.orm import selectin_polymorphic
from werkzeug.utils import redirect
from Database.databases import ServiceProvider,Admin,User,Ratings,Reviews,maindb as db 
app = Flask(__name__)
app.config["SECRET_KEY"] = "dfssdafasbsjcsdflhnvvbhflssdfhjsffrdees"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:kapil@localhost/service_provider_website"
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3306/service_provider_website"
db.__init__(app)
@app.route("/")
def home():
    user = None
    if "user" in session:
        user = session['user']
        print(user)
    return render_template("index.html",user = user)

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

@app.route("/signup",methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("login_signup.html")
    if request.method == "POST":
        name = request.form.get("name")
        category = request.form.get("category")
        profession = request.form.get("profession")
        phone = request.form.get("phone")
        email = request.form.get("email")
        pass1 = request.form.get("pass1")
        pass2 = request.form.get("pass2")
        if pass1 == pass2:
            servprov = ServiceProvider(
                name = name,
                email = email,
                profession =profession,
                category = category,
                phone = phone,
                password = pass1
            )
            db.session.add(servprov)
            db.session.commit()
            print("add successfully")
        return render_template("login_signup.html")

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
    if user:
        return render_template('profile.html',user = user)
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

@app.route("/dr")
def dr():
    return render_template("dr.html")

app.run(debug=True)