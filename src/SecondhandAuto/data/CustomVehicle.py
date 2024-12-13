"""CustomVehicle class.

Creates a CustomVehicle.

Author: Mason Pride
Version: 0.1
"""
from src.SecondhandAuto.data.Vehicle import Vehicle
from typing import Optional


class CustomVehicle(Vehicle):
    """CustomVehicle class."""

    def __init__(self, year: Optional[int] = None,
                 make: Optional[str] = None,
                 model: Optional[str] = None) -> None:
        """Constructor for the class."""
        self.__year = year
        self.__make = make
        self.__model = model
        self.__price: Optional[int] = None
        self.__mileage: Optional[int] = None

    @property
    def year(self) -> Optional[int]:
        """Getter method for year."""
        return self.__year

    @year.setter
    def year(self, value: int) -> None:
        """Setter method for year."""
        self.__year = value

    @property
    def make(self) -> Optional[str]:
        """Getter make for year."""
        return self.__make

    @make.setter
    def make(self, value: str) -> None:
        """Setter method for make."""
        self.__make = value

    @property
    def model(self) -> Optional[str]:
        """Getter make for model."""
        return self.__model

    @model.setter
    def model(self, value: str) -> None:
        """Setter method for model."""
        self.__model = value

    @property
    def price(self) -> Optional[int]:
        """Getter method for price."""
        return self.__price

    @price.setter
    def price(self, value: int) -> None:
        """Setter method for price."""
        self.__price = value

    @property
    def mileage(self) -> Optional[int]:
        """Getter method for mileage."""
        return self.__mileage

    @mileage.setter
    def mileage(self, value: int) -> None:
        """Setter method for mileage."""
        self.__mileage = value

    def __str__(self) -> str:
        """String override method."""
        return "{} {} {}".format(str(self.year),
                                 self.make,
                                 self.model)
