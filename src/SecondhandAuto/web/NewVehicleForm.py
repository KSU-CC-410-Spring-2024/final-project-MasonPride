"""New Vehicle Form Class."""
from flask_wtf import FlaskForm # type: ignore
from wtforms import (StringField, IntegerField, validators) # type: ignore
from wtforms.widgets import NumberInput # type: ignore


class NewVehicleForm(FlaskForm):
    """New Vehicle form."""
    year = StringField("Year", [validators.Length(min=1)])
    make = StringField("Make", [validators.Length(min=1)])
    model = StringField("Model", [validators.Length(min=1)])
