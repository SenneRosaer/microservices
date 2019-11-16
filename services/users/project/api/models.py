from sqlalchemy.sql import func

from project import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
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