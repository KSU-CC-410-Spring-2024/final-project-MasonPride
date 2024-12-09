"""Vehicle interface class.

This is the interface class used as the parent
for all types of vehicles.

Author: Mason Pride
Version: 0.1
"""
from abc import ABC, abstractmethod
from typing import List


class Vehicle(ABC):
    """Vehicle class.

    This class creates the abstract methods to
    be used by vehicles.
    """
    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        """Subclass hook.

        Makes sure the item is able to inherit.
        """
        if cls is Vehicle:
            callables: List[str] = ['make', 'model', 'year']
            ret = True
            for call in callables:
                ret = ret and (hasattr(subclass, call) and
                               callable(getattr(subclass, call)))
            return ret
        else:
            return NotImplemented

    @property
    @abstractmethod
    def make(self) -> float:
        """Make getter.

        Raises NotImplementedError.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def model(self) -> float:
        """Model getter.

        Raises NotImplementedError.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def year(self) -> float:
        """Year getter.

        Raises NotImplementedError.
        """
        raise NotImplementedError
