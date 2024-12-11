"""Buik SUV class.

This class creates a Buik suv.

Author: Mason Pride
Version: 0.1
"""
from src.SecondhandAuto.data.suvs.SUV import SUV


class BuikSUV(SUV):
    """Represents a Buik suv.

    Builds a Buik suv.
    """

    def __init__(self) -> None:
        """Buik class constructor.

        Creates an instance of a Buik
        suv.
        """
        super().__init__()
        self.backup_cam: bool = True
        self.folded_seats: bool = True
        self.__color: str = "Blue"

    @property
    def price(self) -> int:
        """Price getter method.

        Returns the price of the suv.
        """
        return 12000

    @property
    def color(self) -> str:
        """Color getter method.

        Returns the color of the suv.
        """
        return self.__color

    @property
    def year(self) -> int:
        """Year getter method.

        Gets the year of the suv
        """
        return 2010

    @property
    def make(self) -> str:
        """Make getter method.

        Gets the make of the suv.
        """
        return "Buik"

    @property
    def model(self) -> str:
        """Model getter method.

        Gets the model of the suv
        """
        return "Enclave"

    @property
    def mileage(self) -> int:
        """Mileage getter method.

        Gets the mileage of the Truck
        """
        return 240000

    def __str__(self) -> str:
        """String override method."""
        return "{} {} {}".format(str(self.year),
                                 self.make,
                                 self.model)
