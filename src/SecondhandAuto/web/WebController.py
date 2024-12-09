"""Web Controller class.

Creates the controller for our web app.

Author: Mason Pride
Version: 0.1
"""
from flask import render_template, request
from flask_classful import FlaskView, route  # type: ignore
#from src.gamegrub.data.menu.Menu import Menu


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