"""Toyota SUV class.

This class creates a Toyota suv.

Author: Mason Pride
Version: 0.1
"""
from src.SecondhandAuto.data.suvs.SUV import SUV


class ToyotaSUV(SUV):
    """Represents a Toyota suv.

    Builds a Toyota suv.
    """

    def __init__(self) -> None:
        """Toyota class constructor.

        Creates an instance of a Toyota
        suv.
        """
        super().__init__()
        self.backup_cam: bool = False
        self.folded_seats: bool = True
        self.__color: str = "Silver"

    @property
    def price(self) -> int:
        """Price getter method.

        Returns the price of the suv.
        """
        return 16000

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
        return 2012

    @property
    def make(self) -> str:
        """Make getter method.

        Gets the make of the suv.
        """
        return "Toyota"

    @property
    def model(self) -> str:
        """Model getter method.

        Gets the model of the suv
        """
        return "Highlander"

    def __str__(self) -> str:
        """String override method."""
        return "{} {} {}".format(str(self.year), self.make, self.model)
