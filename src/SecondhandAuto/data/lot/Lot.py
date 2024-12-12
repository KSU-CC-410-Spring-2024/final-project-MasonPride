"""Lot class.

Represents all the cars on the lot

Author: Mason Pride
Version: 0.1
"""
from typing import List
from src.SecondhandAuto.data.Vehicle import Vehicle
from src.SecondhandAuto.data.trucks.Truck import Truck
from src.SecondhandAuto.data.suvs.SUV import SUV
from src.SecondhandAuto.data.sedans.Sedan import Sedan
from src.SecondhandAuto.data.trucks.ChevroletTruck import ChevroletTruck
from src.SecondhandAuto.data.trucks.DodgeTruck import DodgeTruck
from src.SecondhandAuto.data.trucks.FordTruck import FordTruck
from src.SecondhandAuto.data.suvs.ChevroletSUV import ChevroletSUV
from src.SecondhandAuto.data.suvs.BuikSUV import BuikSUV
from src.SecondhandAuto.data.suvs.ToyotaSUV import ToyotaSUV
from src.SecondhandAuto.data.sedans.KiaSedan import KiaSedan
from src.SecondhandAuto.data.sedans.HondaSedan import HondaSedan
from src.SecondhandAuto.data.sedans.ToyotaSedan import ToyotaSedan


class Lot():
    """Lot class.

    Static class of cars on the lot
    """
    @staticmethod
    def trucks() -> List[Truck]:
        """Trucks getter method.

        Reutrns:
            List[Truck] representing trucks on lot
        """
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
        """SUV getter method.

        Reutrns:
            List[SUV] representing suvs on lot
        """
        suvs: List[SUV] = []
        chevy = ChevroletSUV()
        suvs.append(chevy)
        toyota = ToyotaSUV()
        suvs.append(toyota)
        buik = BuikSUV()
        suvs.append(buik)
        return suvs

    @staticmethod
    def sedans() -> List[Sedan]:
        """Sedans getter method.

        Reutrns:
            List[Sedan] representing sedans on lot
        """
        sedan: List[Sedan] = []
        kia = KiaSedan()
        sedan.append(kia)
        toyota = ToyotaSedan()
        sedan.append(toyota)
        honda = HondaSedan()
        sedan.append(honda)
        return sedan

    @staticmethod
    def on_lot() -> List[Vehicle]:
        """On lot method.

        Returns all vehicles on the lot
        """
        trucks = Lot.trucks()
        suvs = Lot.suvs()
        sedans = Lot.sedans()
        full_lot = trucks + suvs + sedans
        return full_lot

    @staticmethod
    def get_our_price(mileage: int, market_value: int) -> int:
        """Our price method.

        Calculates the price we are willing to pay 
        based on the mielage and market value

        Args:
            market_value: int representing market price

        Returns:
            int representing our price
        """
        if mileage <= 100000:
            return int(market_value - (.1 * market_value))
        elif mileage > 100000 and mileage <= 200000:
            return int(market_value - (.25 * market_value))
        else:
            return int(market_value - (.45 * market_value))
