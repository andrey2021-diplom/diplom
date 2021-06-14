from flask import render_template, Blueprint, request, abort, redirect, url_for
from flask.helpers import flash
from flask_login import login_user
from flask.globals import session
from . import db
from .models import User

from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/admin/login')
def admin_login_get():
    return render_template('login.html')


@auth.route('/admin/login', methods=['POST'])
def admin_login_post():
    # try:
    login = request.form['login']
    password = request.form['password']
    if u := User.query.filter_by(login=login).first():
        if check_password_hash(u.password, password):
            session['user'] = login
            login_user(u, remember=True)
            return redirect(url_for('admin.admin_get'))
        else:
            return redirect(url_for('auth.admin_login_get'))
    else:
        return redirect(url_for('auth.admin_login_get'))
# except Exception as e:
    #     return str(e)

@auth.route('/admin/registration')
def admin_reg():
    if len(User.query.all())>0:
        return abort(404)
    else:
        return render_template('admin_reg.html')

@auth.route('/admin/registration', methods=['POST'])
def admin_reg_post():
    if len(User.query.all())>0:
        return abort(404)

    login = request.form['login']
    password = request.form['password']

    newuser = User(login=login, password=generate_password_hash(password))

    db.session.add(newuser)
    db.session.commit()
    
    return redirect(url_for('auth.admin_login_get'))
