from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128),unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email, password):
        self.email = email
        self.username = username
        self.password = password

    def to_json(self):
        return {
            'username' : self.username,
            'email' : self.email,
            'password': self.password
        }


class Rating(db.Model):
    __tablename__ = 'rating'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    type = db.Column(db.String(128), nullable=False)
    user = db.Column(db.String(128),nullable=False)
    added_by_user = db.Column(db.Boolean,nullable=False)
    rating = db.Column(db.Integer,nullable=True)

    def __init__(self,id,type,user,added_by_user,rating = None):
        self.id = id
        self.type = type
        self.user = user
        self.added_by_user = added_by_user
        self.rating = rating

    def to_json(self):
        return {
            'id' : self.id,
            'type' : self.type,
            'user' : self.user,
            'added by user' : self.added_by_user,
            'rating' : self.rating
        }