from blogger.app import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    intro = db.Column(db.String(200), nullable=False, default='')
    profile_image = db.Column(db.String(), nullable=False, default='user.jpg')
    password = db.Column(db.String(60), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now())

    posts = db.relationship('Post', backref='user')