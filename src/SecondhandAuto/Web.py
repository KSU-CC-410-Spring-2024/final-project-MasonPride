"""Web class for SecondhandAuto.

Author: Mason Pride
Version: 0.1
"""
from flask import Flask
from src.SecondhandAuto.web.WebController import WebController
from typing import List


class Web:
    """Web class."""

    @staticmethod
    def main(args: List[str]):
        """Main method."""
        app = Flask(__name__)
        WebController.register(app)
        app.config['WTF_CSRF_ENABLED'] = False
        return app
