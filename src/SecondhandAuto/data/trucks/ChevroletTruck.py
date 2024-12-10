"""Chevrolet class.

This class creates a Chevrolet truck.

Author: Mason Pride
Version: 0.1
"""
from src.SecondhandAuto.data.trucks.Truck import Truck


class ChevroletTruck(Truck):
    """Represents a Chevrolet truck.

    Builds a Chevrolet truck.
    """

    def __init__(self) -> None:
        """Chevrolet class constructor.

        Creates an instance of a Chevrolet
        truck.
        """
        super().__init__()
        self.four_wd: bool = True
        self.cab_type: str = "Extended Cab"
        self.__color: str = "Red"

    @property
    def price(self) -> int:
        """Price getter method.

        Returns the price of the truck.
        """
        return 8500

    @property
    def color(self) -> str:
        """Color getter method.

        Returns the color of the truck.
        """
        return self.__color

    @property
    def year(self) -> int:
        """Year getter method.

        Gets the year of the truck
        """
        return 1997

    @property
    def make(self) -> str:
        """Make getter method.

        Gets the make of the truck.
        """
        return "Chevrolet"

    @property
    def model(self) -> str:
        """Model getter method.

        Gets the model of the Truck
        """
        return "Silverado 1500"

    def __str__(self) -> str:
        """String override method."""
        return "{} {} {}".format(str(self.year), self.make, self.model)
