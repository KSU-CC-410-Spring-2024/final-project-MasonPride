"""Test Class for Ford Truck.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from src.SecondhandAuto.data.trucks.FordTruck import FordTruck


class TestFordTruck():
    """Test class for 'FordTruck.py'."""
    def test_backup_cam_false_on_init(self):
        """Test backup cam init."""
        ford = FordTruck()
        assert not ford.four_wd

    def test_folded_seats_true_on_init(self):
        """Test nav init."""
        ford = FordTruck()
        assert ford.cab_type == "Super Cab"

    def test_color_on_init(self):
        """Test color init."""
        ford = FordTruck()
        assert ford.color == "White"

    def test_price_on_init(self):
        """Test price init."""
        ford = FordTruck()
        assert ford.price == 21000

    def test_year_on_init(self):
        """Test year init."""
        ford = FordTruck()
        assert ford.year == 2019

    def test_make_on_init(self):
        """Test make init."""
        ford = FordTruck()
        assert ford.make == "Ford"

    def test_model_on_init(self):
        """Test model init."""
        ford = FordTruck()
        assert ford.model == "Ranger"

    def test_mielage_on_init(self):
        """Test mielage init."""
        ford = FordTruck()
        assert ford.mileage == 200000

    def test_ford_to_string(self):
        """Test to string method."""
        ford = FordTruck()
        real = "2019 Ford Ranger"
        assert str(ford) == real
