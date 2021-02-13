from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def get_user(user_email):
    return User.query.get(user_email)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, name,surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = generate_password_hash(password)
    
    def __repr__(self):
        return f'<User {self.username}>'

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def __repr__(self):
        return '<User %r>' % self.name