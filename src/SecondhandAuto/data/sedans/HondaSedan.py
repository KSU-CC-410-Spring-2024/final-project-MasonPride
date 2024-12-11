"""Honda Sedan class.

This class creates a Honda Sedan.

Author: Mason Pride
Version: 0.1
"""
from src.SecondhandAuto.data.sedans.Sedan import Sedan


class HondaSedan(Sedan):
    """Represents a Honda Sedan.

    Builds a Honda Sedan.
    """
    def __init__(self) -> None:
        """Honda Sedan class constructor.

        Creates an instance of a Honda Sedan.
        """
        super().__init__()
        self.led_lights: bool = True
        self.nav_system: bool = True
        self.__color: str = "Maroon"

    @property
    def price(self) -> int:
        """Price getter method.

        Returns the price of the sedan.
        """
        return 12000

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
        return 2012

    @property
    def make(self) -> str:
        """Make getter method.

        Gets the make of the sedan.
        """
        return "Honda"

    @property
    def model(self) -> str:
        """Model getter method.

        Gets the model of the sedan
        """
        return "Civic"

    @property
    def mileage(self) -> int:
        """Mileage getter method.

        Gets the mileage of the Truck
        """
        return 280450

    def __str__(self) -> str:
        """String override method."""
        return "{} {} {}".format(str(self.year),
                                 self.make,
                                 self.model)
