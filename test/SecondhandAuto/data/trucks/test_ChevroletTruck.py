"""Test Class for Chevrolet Truck.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.SecondhandAuto.data.trucks.ChevroletTruck import ChevroletTruck

class TestChevroletTruck():
    """Test class for 'ChevroletTruck.py'."""
    def test_backup_cam_false_on_init(self):
        """Test backup cam init."""
        chevrolet = ChevroletTruck()
        assert chevrolet.four_wd == True

    def test_folded_seats_true_on_init(self):
        """Test nav init."""
        chevrolet = ChevroletTruck()
        assert chevrolet.cab_type == "Extended Cab"

    def test_color_on_init(self):
        """Test color init."""
        chevrolet = ChevroletTruck()
        assert chevrolet.color == "Red"

    def test_price_on_init(self):
        """Test price init."""
        chevrolet = ChevroletTruck()
        assert chevrolet.price == 8500

    def test_year_on_init(self):
        """Test year init."""
        chevrolet = ChevroletTruck()
        assert chevrolet.year == 1997

    def test_make_on_init(self):
        """Test make init."""
        chevrolet = ChevroletTruck()
        assert chevrolet.make == "Chevrolet"

    def test_model_on_init(self):
        """Test model init."""
        chevrolet = ChevroletTruck()
        assert chevrolet.model == "Silverado 1500"

    def test_mielage_on_init(self):
        """Test mielage init."""
        chevrolet = ChevroletTruck()
        assert chevrolet.mileage == 140000

    def test_chevrolet_to_string(self):
        """Test to string method."""
        chevrolet = ChevroletTruck()
        real = "1997 Chevrolet Silverado 1500"
        assert str(chevrolet) == real
