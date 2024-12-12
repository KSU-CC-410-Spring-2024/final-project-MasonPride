"""Web Controller class.

Creates the controller for our web app.

Author: Mason Pride
Version: 0.1
"""
from flask import render_template, request
from flask_classful import FlaskView, route  # type: ignore
from src.SecondhandAuto.data.lot.Lot import Lot
from src.SecondhandAuto.api.GetMarketValue import GetMarketValue
from src.SecondhandAuto.data.CustomVehicle import CustomVehicle
from src.SecondhandAuto.web.NewVehicleForm import NewVehicleForm


class WebController(FlaskView):
    """WebController class."""
    route_base = "/"

    @route('/')
    def index(self):
        """Index route method.

        Defines the route for index.

        Returns:
            render template of index
        """
        return render_template("index.html")

    @route('/browse/')
    def browse(self):
        """Browse route method.

        Defines the route for browse

        Returns:
            render template of our lot
        """
        lot = Lot()
        return render_template("lot.html", lot=lot)

    @route('/sell/', methods=['GET'])
    def sell_form(self):
        """Sell form."""
        vehicle = CustomVehicle()
        form = NewVehicleForm(obj=vehicle)
        return render_template("sell_form.html", form=form)

    @route('/sell/', methods=['POST'])
    def sell_form_return(self):
        """Sell form."""
        form = NewVehicleForm()
        if not form.validate_on_submit():
            return render_template("sell_form.html", form=form)
        market_value = GetMarketValue.get_value(form.year.data, form.make.data, form.model.data)
        market_value = market_value[5]
        avg = ((market_value + form.price.data) /2)
        our_price = Lot().get_our_price(int(form.mileage.data), avg)
        return render_template("sell_success_form.html", our_price=our_price)

    @route('/market-value/', methods=['GET'])
    def market_value(self):
        """Market value.

        Loads the market value page
        """
        return render_template("market_value.html")

    @route('/market-value/', methods=['POST'])
    def market_value_result(self):
        """Market value.

        Loads the market value page
        """
        year: str = request.form.get('year', None)
        make: str = request.form.get('make', None)
        model: str = request.form.get('model', None)
        mileage: str = request.form.get('mileage', None)
        try:
            data = GetMarketValue.get_value(year, make, model)
            our_price = Lot().get_our_price(int(mileage), int(data[5]))
            return render_template("market_value.html", data=data, our_price=our_price)
        except Exception as e:
            error = e
            return render_template("market_value.html", error=error)
