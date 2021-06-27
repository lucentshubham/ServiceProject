from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:kapil@localhost/service_provider_website"
db = SQLAlchemy(app)
from Database.databases import *
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/page1")
def page1():
    return render_template("inner-page.html")
@app.route("/page2")
def page2():
    return render_template("portfolio-details.html")
app.run(debug=True)