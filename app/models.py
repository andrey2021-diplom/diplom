from flask_login.mixins import UserMixin
from . import db
from flask_login import UserMixin
from datetime import datetime as dt

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String)
    password = db.Column(db.String)

class FindRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    r_fio = db.Column(db.String)
    r_phone = db.Column(db.String)
    f_fio = db.Column(db.String)
    f_dob = db.Column(db.String)
    f_description = db.Column(db.String)
    f_place = db.Column(db.String)
    status = db.Column(db.String)
