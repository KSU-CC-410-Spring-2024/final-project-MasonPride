"""Test Class for Dodge Truck.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from src.SecondhandAuto.data.trucks.DodgeTruck import DodgeTruck


class TestDodgeTruck():
    """Test class for 'DodgeTruck.py'."""
    def test_backup_cam_false_on_init(self):
        """Test backup cam init."""
        dodge = DodgeTruck()
        assert not dodge.four_wd

    def test_folded_seats_true_on_init(self):
        """Test nav init."""
        dodge = DodgeTruck()
        assert dodge.cab_type == "Crew Cab"

    def test_color_on_init(self):
        """Test color init."""
        dodge = DodgeTruck()
        assert dodge.color == "Grey"

    def test_price_on_init(self):
        """Test price init."""
        dodge = DodgeTruck()
        assert dodge.price == 11000

    def test_year_on_init(self):
        """Test year init."""
        dodge = DodgeTruck()
        assert dodge.year == 2007

    def test_make_on_init(self):
        """Test make init."""
        dodge = DodgeTruck()
        assert dodge.make == "Dodge"

    def test_model_on_init(self):
        """Test model init."""
        dodge = DodgeTruck()
        assert dodge.model == "Ram 1500"

    def test_mielage_on_init(self):
        """Test mielage init."""
        dodge = DodgeTruck()
        assert dodge.mileage == 100000

    def test_dodge_to_string(self):
        """Test to string method."""
        dodge = DodgeTruck()
        real = "2007 Dodge Ram 1500"
        assert str(dodge) == real
