from re import U
from flask import render_template, Blueprint, request, abort, jsonify
from flask_login import login_required
from werkzeug.utils import redirect
from . import db
from .models import FindRequests

admin = Blueprint('admin', __name__)


@admin.route('/admin')
@login_required
def admin_get():
    fr = FindRequests.query.all()
    return render_template('admin.html', r=fr)

@admin.route('/admin/card/id=<id>')
@login_required
def admin_card(id):
    u = FindRequests.query.filter_by(id=id).first()
    return render_template('card.html', user=u)

@admin.route('/admin/card/setstatus/id=<id>&status=<status>')
@login_required
def admin_setstatus(id, status):
    u = FindRequests.query.filter_by(id=id).first()
    u.status = status
    db.session.add(u)
    db.session.commit()
    return redirect('/admin')

@admin.route('/admin/card/delete/id=<id>')
@login_required
def admin_delete(id):
    u = FindRequests.query.filter_by(id=id).first()
    db.session.delete(u)
    db.session.commit()
    return redirect('/admin')
