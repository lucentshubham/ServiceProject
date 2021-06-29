from flask import Flask,render_template,request,session
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from Database.databases import ServiceProvider,Admin,User,Ratings,Reviews,maindb as db
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
                session['user'] = user.name
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


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/doctor')
def doctor():
    return render_template('dr.html')
app.run(debug=True)

