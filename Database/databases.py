from mainserver import db
class ServiceProvider(db.Model):
    __tablename__ = "serviceprovider"
    sno = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable = False)
    profession = db.Column(db.String(50),nullable = False)
    category = db.Column(db.String(50),nullable = False)
    city = db.Column(db.String(30),nullable = False)
    phone = db.Column(db.String(13),nullable = True)
    speciality = db.Column(db.String(50),nullable = True)
    qualification = db.Column(db.Text,nullable=True)
    images = db.Column(db.PickleType,nullable = True)
    address = db.Column(db.String(100),nullable = False)
    open_close_time = db.Column(db.DateTime,nullable = True)
    experience = db.Column(db.Float,nullable=True)

class Ratings(db.Model):
    __tablename__ = "rating"
    sno = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable = False)
    no_of_rating = db.Column(db.Integer,nullable = False)
    rating_list = db.Column(db.PickleType,nullable = False)


class Reviews(db.Model):
    __tablename__ = "reviews"
    sno = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable = False)
    no_of_review = db.Column(db.Integer,nullable = False)
    review_list = db.Column(db.PickleType,nullable = False)    

class User(db.Model):
    __tablename__ = "user"
    sno = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable = False)
    city = db.Column(db.String(30),nullable = False)
    phone = db.Column(db.String(13),nullable = True)
class Admin(db.Model):
    __tablename__ = "admin"
    sno = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable = False)
    password = db.Column(db.String(10),nullable = False)