"""Truck base class.

This is the base abstract class
for trucks

Author: Mason Pride
Version: 0.1
"""
from src.SecondhandAuto.data.Vehicle import Vehicle


class Truck(Vehicle):
    """Truck class.

    Creates abstract methods used by
    trucks.
    """

    def __init__(self) -> None:
        """Truck class constructor.

        initializes common attributes of
        trucks.
        """
        self.__four_wd: bool = False
        self.__cab_type: str = ""

    @property
    def four_wd(self) -> bool:
        """Getter for four_wd attrribute.

        Gets the four wheel drive attribute
        """
        return self.__four_wd

    @four_wd.setter
    def four_wd(self, value: bool) -> None:
        """Setter for four_wd attrribute.

        Sets the four wheel drive attribute
        """
        self.__four_wd = value

    @property
    def cab_type(self) -> str:
        """Getter for cab_type attrribute.

        Gets the cab_type attribute
        """
        return self.__cab_type

    @cab_type.setter
    def cab_type(self, value: str) -> None:
        """Setter for cab_type attrribute.

        Sets the cab type attribute
        """
        self.__cab_type = value
