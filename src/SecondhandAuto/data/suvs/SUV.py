"""SUV base class.

This is the base abstract class
for SUV's

Author: Mason Pride
Version: 0.1
"""
from src.SecondhandAuto.data.Vehicle import Vehicle


class SUV(Vehicle):
    """SUV class.

    Creates abstract methods used by
    SUV's.
    """

    def __init__(self) -> None:
        """SUV class constructor.

        initializes common attributes of
        SUV's.
        """
        self.__backup_cam: bool = False
        self.__folded_seats: bool = False

    @property
    def backup_cam(self) -> bool:
        """Getter for backup cam attrribute.

        Gets the back up cam attribute
        """
        return self.__backup_cam

    @backup_cam.setter
    def backup_cam(self, value: bool) -> None:
        """Setter for back up cam attrribute.

        Sets the back up cam attribute
        """
        self.__backup_cam = value

    @property
    def folded_seats(self) -> str:
        """Getter for folded_seats attrribute.

        Gets the folded_seats attribute
        """
        return self.__folded_seats

    @folded_seats.setter
    def folded_seats(self, value: bool) -> None:
        """Setter for folded_seats attrribute.

        Sets the cab type attribute
        """
        self.__folded_seats = value
