"""Web Controller class.

Creates the controller for our web app.

Author: Mason Pride
Version: 0.1
"""
from flask import render_template, request
from flask_classful import FlaskView, route  # type: ignore
#from src.gamegrub.data.menu.Menu import Menu
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
        data = GetMarketValue.get_value(year, make, model)
        return render_template("market_value.html", data=data)
