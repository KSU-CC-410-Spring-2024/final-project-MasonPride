"""Main class for secondhand-auto.

This class will run the SecondhandAuto package.

Author: Mason Pride
Version: 0.1
"""
from typing import List
#from src.SecondhandAuto.data.lot.Lot import Lot
from src.SecondhandAuto.api.GetMarketValue import GetMarketValue
class Main:
    """Main Class."""

    @staticmethod
    def main(args: List[str]) -> None:
        """Main method."""
        print("Hello World")
        """
        lot = Lot.on_lot()
        for car in lot:
            print(car)
        """
        print(GetMarketValue.get_value("2007", "Dodge", "Charger"))
