
import os
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    TextAreaField,
    BooleanField,
    PasswordField,
    SubmitField,
    SelectField,
    RadioField,
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


penguin_colors = [f for f in os.listdir('static/penguins/') if f[0] != '.']


class NameForm(FlaskForm):
    first = StringField(
        "First",
        validators=[DataRequired()],
        filters=[lower, strip],
        render_kw={"placeholder": "f1rst", "onkeyup": "return forceLower(this);"},
    )
    last = StringField(
        "Last",
        validators=[DataRequired()],
        filters=[lower, strip],
        render_kw={"placeholder": "la5t", "onkeyup": "return forceLower(this);"},
    )
    submit = SubmitField("next")


class RSVPForm(FlaskForm):
    rsvp = RadioField(
        "RSVP",
        validators=[DataRequired()],
        choices=[('yes', 'yes!!!1 :}'), ('no', "no :'-(")],
    )
    dish = StringField(
        "Dish",
        filters=[lower, strip],
        render_kw={"placeholder": "dessert pizza :0", "onkeyup": "return forceLower(this);"},
    )
    color = RadioField(
        "Color",
        validators=[DataRequired()],
        choices=penguin_colors,
    )
    submit = SubmitField("awesome!!!")
