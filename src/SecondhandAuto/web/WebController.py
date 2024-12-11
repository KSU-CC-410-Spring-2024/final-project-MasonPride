"""Web Controller class.

Creates the controller for our web app.

Author: Mason Pride
Version: 0.1
"""
from flask import render_template, request
from flask_classful import FlaskView, route  # type: ignore
from src.SecondhandAuto.data.lot.Lot import Lot
from src.SecondhandAuto.api.GetMarketValue import GetMarketValue


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
        try:
            data = GetMarketValue.get_value(year, make, model)
            return render_template("market_value.html", data=data)
        except Exception as e:
            error = e
            return render_template("market_value.html", error=error)
