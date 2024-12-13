"""New Vehicle Form Class."""
from flask_wtf import FlaskForm  # type: ignore
from wtforms import (StringField, IntegerField, validators)  # type: ignore
from wtforms.widgets import NumberInput  # type: ignore


class NewVehicleForm(FlaskForm):
    """New Vehicle form."""
    year = IntegerField("Year",
                        [validators.NumberRange(min=1900, max=2026)],
                        widget=NumberInput(step=1))
    make = StringField("Make", [validators.Length(min=1)])
    model = StringField("Model", [validators.Length(min=1)])
    mileage = IntegerField("Mileage",
                           [validators.NumberRange(min=0, max=500000)],
                           widget=NumberInput(step=1))
    price = IntegerField("Price",
                         [validators.NumberRange(min=0, max=500000)],
                         widget=NumberInput(step=1))
