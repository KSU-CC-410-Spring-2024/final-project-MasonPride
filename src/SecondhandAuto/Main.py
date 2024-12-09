"""Main class for secondhand-auto.

This class will run the SecondhandAuto package.

Author: Mason Pride
Version: 0.1
"""
from typing import List
from src.SecondhandAuto.data.trucks.Chevrolet import Chevrolet

class Main:
    """Main Class."""

    @staticmethod
    def main(args: List[str]) -> None:
        """Main method."""
        print("Hello World")
        chevy = Chevrolet()
        print(chevy)
