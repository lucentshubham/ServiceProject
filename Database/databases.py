class Databases:
    def __init__(self,db):
        self.db = db
    class ServiceProvider(self.db.Model):
        __tablename__ = "serviceprovider"
        pass
    class User(self.db.Model):
        __tablename__ = "user"
        pass
    class Admin(self.db.model):
        __tablename__ = "admin"
        pass    
    