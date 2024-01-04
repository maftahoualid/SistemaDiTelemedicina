from .. import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    codice_fiscale= db.Column(db.String(16), unique=True) 
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    pressioni = db.relationship('Pressione')

class Pressione(db.Model):
    date = db.Column(db.DateTime(timezone=True), default=func.now(), primary_key=True)
    SBP = db.Column(db.Integer)
    DBP = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


