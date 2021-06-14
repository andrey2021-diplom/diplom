from flask import render_template, Blueprint, request, abort, jsonify
from flask.helpers import flash, get_flashed_messages
from . import db
from .models import FindRequests

main = Blueprint('main', __name__)

@main.route('/')
def root_path():
    return render_template('index.html')

@main.route('/policy')
def policy():
    return render_template('policy.html')

@main.route('/sendrequest', methods=['POST'])
def main_request():
    try:
        r_fio = request.form['r_fio']
        r_phone = request.form['r_phone']
        f_fio= request.form['f_fio']
        f_dob= request.form['f_dob']
        f_desc= request.form['f_desc']
        f_place = request.form['f_place']

        new_r = FindRequests(r_fio=f_fio, r_phone=r_phone, f_fio=f_fio,
                             f_dob=f_dob, f_description=f_desc, f_place=f_place, status='0')
        db.session.add(new_r)
        db.session.commit()
        flash("Ваша заявка отправлена.")
        return render_template('index.html')
    except:
        return abort(400)
