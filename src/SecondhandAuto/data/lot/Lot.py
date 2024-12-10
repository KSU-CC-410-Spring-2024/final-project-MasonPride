"""Lot class.

Represents all the cars on the lot

Author: Mason Pride
Version: 0.1
"""
from typing import List
from src.SecondhandAuto.data.Vehicle import Vehicle
from src.SecondhandAuto.data.trucks.Truck import Truck
from src.SecondhandAuto.data.trucks.Chevrolet import Chevrolet
from src.SecondhandAuto.data.trucks.Dodge import Dodge
from src.SecondhandAuto.data.trucks.Ford import Ford


class Lot():
    """Lot class.

    Static class of cars on the lot
    """
    @staticmethod
    def trucks() -> List[Truck]:
        trucks: List[Truck] = []
        chevy = Chevrolet()
        trucks.append(chevy)
        ford = Ford()
        trucks.append(ford)
        dodge = Dodge()
        trucks.append(dodge)
        return trucks

    @staticmethod
    def on_lot() -> List[Vehicle]:
        """On lot method.

        Returns all vehicles on the lot
        """
        vehicles: List[Vehicle] = []
        chevy = Chevrolet()
        vehicles.append(chevy)
        ford = Ford()
        vehicles.append(ford)
        dodge = Dodge()
        vehicles.append(dodge)
        return vehicles
