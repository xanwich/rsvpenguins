# from flask import request
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    TextAreaField,
    BooleanField,
    PasswordField,
    SubmitField,
)
from wtforms.validators import (
    ValidationError,
    DataRequired,
    InputRequired,
    Email,
    NumberRange,
    Regexp,
    Length,
    EqualTo,
    Optional,
)
from models import User


def lower(s):
    if s is not None:
        return s.lower()
    else:
        return s


def strip(s):
    if s is not None:
        return s.strip()
    else:
        return s


class NameForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[DataRequired()],
        filters=[lower, strip],
        render_kw={"placeholder": "xXx_Dark_Wolf_96_xXx", "onkeyup": "return forceLower(this);"},
    )
    submit = SubmitField("next")
