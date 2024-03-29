import os
from flask import render_template, redirect, flash, request, send_from_directory
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import func
from werkzeug.urls import url_parse
from models import User
from app import app, db, login_manager
from forms import NameForm, RSVPForm


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
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
    return render_template(
        "/login.html",
        home=True,
        view=False,
        form=form,
    )

@app.route("/edit", methods=["GET", "POST"])
@login_required
def edit():
    form = RSVPForm()
    if current_user.dish:
        form.dish.render_kw['placeholder'] = current_user.dish
    if form.validate_on_submit():
        current_user.rsvp = form.rsvp.data
        current_user.dish = form.dish.data
        current_user.color = form.color.data
        db.session.commit()
        return redirect('/view')
    return render_template(
        "/edit.html",
        home=False,
        view=False,
        form=form,
        first=current_user.first,
    )

@app.route("/view", methods=["GET", "POST"])
@login_required
def view():
    rsvp_yes = User.query.filter_by(rsvp='yes')
    rsvp_no = User.query.filter_by(rsvp='no')
    return render_template(
        "/view.html",
        home=False,
        view=True,
        yes=rsvp_yes,
        no=rsvp_no,
    )


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/')
