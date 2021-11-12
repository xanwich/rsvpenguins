import os
from flask import render_template, redirect, flash, request, send_from_directory
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import func
from werkzeug.urls import url_parse
from models import User
from app import app, db, login_manager
from forms import NameForm, RSVPForm


@app.route("/", methods=['GET', 'POST'])
def index():
    logout_user()
    form = NameForm()
    if form.validate_on_submit():
        # look for existing user
        user = User.query.filter_by(first=form.first.data, last=form.last.data).first()
        # if user does not exist, sign them up
        if user is None:
            user = User(first=form.first.data, last=form.last.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect('/edit')
        # if user does exist, log in
        else:
            login_user(user)
            return redirect('/view')
    return render_template("/login.html", form=form)

@login_required
@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RSVPForm()
    return render_template("/edit.html", form=form, first=current_user.first)

@login_required
@app.route("/view", methods=["GET", "POST"])
def view():
    return render_template("/view.html")