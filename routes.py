import os
from flask import render_template, redirect, flash, request, send_from_directory
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import func
from werkzeug.urls import url_parse
from models import User
from app import app, db
from forms import NameForm



@app.route("/")
@app.route("/index")
def index():
    form = NameForm()
    return render_template("/login.html", form=form)

