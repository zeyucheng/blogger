from datetime import datetime
from blogger.app import db


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_photo = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    designer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.now())