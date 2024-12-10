"""Ford class.

This class creates a Ford truck.

Author: Mason Pride
Version: 0.1
"""
from src.SecondhandAuto.data.trucks.Truck import Truck


class FordTruck(Truck):
    """Represents a Ford truck.

    Builds a Chevrolet truck.
    """

    def __init__(self) -> None:
        """Ford class constructor.

        Creates an instance of a Ford
        truck.
        """
        super().__init__()
        self.four_wd: bool = False
        self.cab_type: str = "Super Cab"
        self.__color: str = "White"

    @property
    def price(self) -> int:
        """Price getter method.

        Returns the price of the truck.
        """
        return 21000

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
        return 2019

    @property
    def make(self) -> str:
        """Make getter method.

        Gets the make of the truck.
        """
        return "Ford"

    @property
    def model(self) -> str:
        """Model getter method.

        Gets the model of the Truck
        """
        return "Ranger"

    def __str__(self) -> str:
        """String override method."""
        return "{} {} {}".format(str(self.year), self.make, self.model)
