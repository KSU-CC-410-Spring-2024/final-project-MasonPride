"""Lot class.

Represents all the cars on the lot

Author: Mason Pride
Version: 0.1
"""
from typing import List
from src.SecondhandAuto.data.Vehicle import Vehicle
from src.SecondhandAuto.data.trucks.Truck import Truck
from src.SecondhandAuto.data.suvs.SUV import SUV
from src.SecondhandAuto.data.trucks.ChevroletTruck import ChevroletTruck
from src.SecondhandAuto.data.trucks.DodgeTruck import DodgeTruck
from src.SecondhandAuto.data.trucks.FordTruck import FordTruck
from src.SecondhandAuto.data.suvs.ChevroletSUV import ChevroletSUV
from src.SecondhandAuto.data.suvs.BuikSUV import BuikSUV
from src.SecondhandAuto.data.suvs.ToyotaSUV import ToyotaSUV



class Lot():
    """Lot class.

    Static class of cars on the lot
    """
    @staticmethod
    def trucks() -> List[Truck]:
        trucks: List[Truck] = []
        chevy = ChevroletTruck()
        trucks.append(chevy)
        ford = FordTruck()
        trucks.append(ford)
        dodge = DodgeTruck()
        trucks.append(dodge)
        return trucks

    @staticmethod
    def suvs() -> List[SUV]:
        suvs: List[SUV] = []
        chevy = ChevroletSUV()
        suvs.append(chevy)
        toyota = ToyotaSUV()
        suvs.append(toyota)
        buik = BuikSUV()
        suvs.append(buik)
        return suvs

    @staticmethod
    def on_lot() -> List[Vehicle]:
        """On lot method.

        Returns all vehicles on the lot
        """
        vehicles: List[Vehicle] = []
        chevy = ChevroletTruck()
        vehicles.append(chevy)
        ford = FordTruck()
        vehicles.append(ford)
        dodge = DodgeTruck()
        vehicles.append(dodge)
        return vehicles
