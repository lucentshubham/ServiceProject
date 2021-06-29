from flask_sqlalchemy import SQLAlchemy
maindb = SQLAlchemy()
class ServiceProvider(maindb.Model):
    __tablename__ = "serviceprovider"
    sno = maindb.Column(maindb.Integer,primary_key = True)
    name = maindb.Column(maindb.String(50),nullable=False)
    email = maindb.Column(maindb.String(50),nullable = False)
    password = maindb.Column(maindb.String(50),nullable = False)
    profession = maindb.Column(maindb.String(50),nullable = False)
    category = maindb.Column(maindb.String(50),nullable = False)
    city = maindb.Column(maindb.String(30),nullable = True)
    state = maindb.Column(maindb.String(30),nullable = True)
    phone = maindb.Column(maindb.String(13),nullable = False)
    speciality = maindb.Column(maindb.String(50),nullable = True)
    qualification = maindb.Column(maindb.PickleType,nullable=True)
    images = maindb.Column(maindb.PickleType,nullable = True)
    address = maindb.Column(maindb.String(100),nullable = True)
    open_close_time = maindb.Column(maindb.DateTime,nullable = True)
    experience = maindb.Column(maindb.Float,nullable=True)

class Ratings(maindb.Model):
    __tablename__ = "rating"
    sno = maindb.Column(maindb.Integer,primary_key = True)
    name = maindb.Column(maindb.String(50),nullable = False)
    no_of_rating = maindb.Column(maindb.Integer,nullable = False)
    rating_list = maindb.Column(maindb.PickleType,nullable = False)


class Reviews(maindb.Model):
    __tablename__ = "reviews"
    sno = maindb.Column(maindb.Integer,primary_key = True)
    name = maindb.Column(maindb.String(50),nullable = False)
    no_of_review = maindb.Column(maindb.Integer,nullable = False)
    review_list = maindb.Column(maindb.PickleType,nullable = False)    

class User(maindb.Model):
    __tablename__ = "user"
    sno = maindb.Column(maindb.Integer,primary_key = True)
    name = maindb.Column(maindb.String(50),nullable=False)
    email = maindb.Column(maindb.String(50),nullable = False)
    city = maindb.Column(maindb.String(30),nullable = False)
    state=maindb.Column(maindb.String(30),nullable = False)
    phone = maindb.Column(maindb.String(13),nullable = True) 

class Admin(maindb.Model):
    __tablename__ = "admin"
    sno = maindb.Column(maindb.Integer,primary_key = True)
    name = maindb.Column(maindb.String(50),nullable=False)
    username=maindb.Column(maindb.String(50),nullable=False)
    email = maindb.Column(maindb.String(50),nullable = False)
    password = maindb.Column(maindb.String(10),nullable = False)