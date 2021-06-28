from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from Database.databases import ServiceProvider,Admin,User,Ratings,Reviews,maindb as db
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:kapil@localhost/service_provider_website"
db.__init__(app)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login_signup.html")
    if request.method == "POSt":
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
    
app.run(debug=True)