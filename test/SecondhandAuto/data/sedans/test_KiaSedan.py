"""Test Class for Kia Sedan.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.SecondhandAuto.data.sedans.KiaSedan import KiaSedan

class TestKiaSedan():
    """Test class for 'KiaSedan.py'."""
    def test_led_lights_false_on_init(self):
        """Test LED lights init."""
        kia = KiaSedan()
        assert kia.led_lights == False

    def test_nav_system_true_on_init(self):
        """Test nav init."""
        kia = KiaSedan()
        assert kia.nav_system == True

    def test_color_beige_on_init(self):
        """Test color init."""
        kia = KiaSedan()
        assert kia.color == "Beige"

    def test_price_on_init(self):
        """Test price init."""
        kia = KiaSedan()
        assert kia.price == 9000

    def test_year_on_init(self):
        """Test year init."""
        kia = KiaSedan()
        assert kia.year == 2010

    def test_make_on_init(self):
        """Test make init."""
        kia = KiaSedan()
        assert kia.make == "Kia"

    def test_model_on_init(self):
        """Test model init."""
        kia = KiaSedan()
        assert kia.model == "Forte"

    def test_mielage_on_init(self):
        """Test mielage init."""
        kia = KiaSedan()
        assert kia.mileage == 178000

    def test_kia_to_string(self):
        """Test to string method."""
        kia = KiaSedan()
        real = "2010 Kia Forte"
        assert str(kia) == real
