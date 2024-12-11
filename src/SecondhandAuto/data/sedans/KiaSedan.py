"""Kia Sedan class.

This class creates a Kia Sedan.

Author: Mason Pride
Version: 0.1
"""
from src.SecondhandAuto.data.sedans.Sedan import Sedan


class KiaSedan(Sedan):
    """Represents a Kia Sedan.

    Builds a Kia Sedan.
    """
    def __init__(self) -> None:
        """Kia class constructor.

        Creates an instance of a Kia
        Sedan.
        """
        super().__init__()
        self.led_lights: bool = False
        self.nav_system: bool = True
        self.__color: str = "Beige"

    @property
    def price(self) -> int:
        """Price getter method.

        Returns the price of the sedan.
        """
        return 9000

    @property
    def color(self) -> str:
        """Color getter method.

        Returns the color of the sedan.
        """
        return self.__color

    @property
    def year(self) -> int:
        """Year getter method.

        Gets the year of the sedan
        """
        return 2010

    @property
    def make(self) -> str:
        """Make getter method.

        Gets the make of the sedan.
        """
        return "Kia"

    @property
    def model(self) -> str:
        """Model getter method.

        Gets the model of the sedan
        """
        return "Forte"

    @property
    def mileage(self) -> int:
        """Mileage getter method.

        Gets the mileage of the Truck
        """
        return 178000

    def __str__(self) -> str:
        """String override method."""
        return "{} {} {}".format(str(self.year),
                                 self.make,
                                 self.model)
