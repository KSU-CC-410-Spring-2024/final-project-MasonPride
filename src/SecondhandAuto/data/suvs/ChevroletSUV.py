"""Chevrolet SUV class.

This class creates a Chevrolet suv.

Author: Mason Pride
Version: 0.1
"""
from src.SecondhandAuto.data.suvs.SUV import SUV


class ChevroletSUV(SUV):
    """Represents a Chevrolet suv.

    Builds a Chevrolet suv.
    """

    def __init__(self) -> None:
        """Chevrolet class constructor.

        Creates an instance of a Chevrolet
        suv.
        """
        super().__init__()
        self.backup_cam: bool = False
        self.folded_seats: bool = True
        self.__color: str = "Red"

    @property
    def price(self) -> int:
        """Price getter method.

        Returns the price of the suv.
        """
        return 8500

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
        return 2009

    @property
    def make(self) -> str:
        """Make getter method.

        Gets the make of the suv.
        """
        return "Chevrolet"

    @property
    def model(self) -> str:
        """Model getter method.

        Gets the model of the suv
        """
        return "Trailblazer"

    def __str__(self) -> str:
        """String override method."""
        return "{} {} {}".format(str(self.year), self.make, self.model)
