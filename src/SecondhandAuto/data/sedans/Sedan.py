"""Sedan base class.

This is the base abstract class
for Sedan's

Author: Mason Pride
Version: 0.1
"""
from src.SecondhandAuto.data.Vehicle import Vehicle


class Sedan(Vehicle):
    """Sedan class.

    Creates abstract methods used by
    Sedan's.
    """
    def __init__(self) -> None:
        """Sedan class constructor.

        initializes common attributes of
        Sedan's.
        """
        self.__led_lights: bool = False
        self.__nav_system: bool = False

    @property
    def led_lights(self) -> bool:
        """Getter for backup cam attrribute.

        Gets the back up cam attribute
        """
        return self.__led_lights

    @led_lights.setter
    def led_lights(self, value: bool) -> None:
        """Setter for back up cam attrribute.

        Sets the back up cam attribute
        """
        self.__led_lights = value

    @property
    def nav_system(self) -> bool:
        """Getter for nav_system attrribute.

        Gets the nav_system attribute
        """
        return self.__nav_system

    @nav_system.setter
    def nav_system(self, value: bool) -> None:
        """Setter for nav_system attrribute.

        Sets the cab type attribute
        """
        self.__nav_system = value
