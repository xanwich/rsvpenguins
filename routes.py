import os
from flask import render_template, redirect, flash, request, send_from_directory
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import func
from werkzeug.urls import url_parse
from models import User
from app import app, db
from forms import NameForm, RSVPForm


@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    return render_template("/login.html", form=form)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RSVPForm()
    return render_template("/edit.html", form=form)

@app.route("/view", methods=["GET", "POST"])
def view():
    return render_template("/view.html")