"""Test Class for Toyota Sedan.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.SecondhandAuto.data.sedans.ToyotaSedan import ToyotaSedan

class TestToyotaSedan():
    """Test class for 'ToyotaSedan.py'."""
    def test_led_lights_false_on_init(self):
        """Test LED lights init."""
        toyota = ToyotaSedan()
        assert toyota.led_lights == False

    def test_nav_system_true_on_init(self):
        """Test nav init."""
        toyota = ToyotaSedan()
        assert toyota.nav_system == False

    def test_color_beige_on_init(self):
        """Test color init."""
        toyota = ToyotaSedan()
        assert toyota.color == "Silver"

    def test_price_on_init(self):
        """Test price init."""
        toyota = ToyotaSedan()
        assert toyota.price == 4000

    def test_year_on_init(self):
        """Test year init."""
        Toyota = ToyotaSedan()
        assert Toyota.year == 2002

    def test_make_on_init(self):
        """Test make init."""
        toyota = ToyotaSedan()
        assert toyota.make == "Toyota"

    def test_model_on_init(self):
        """Test model init."""
        toyota = ToyotaSedan()
        assert toyota.model == "Camry"

    def test_mielage_on_init(self):
        """Test mielage init."""
        toyota = ToyotaSedan()
        assert toyota.mileage == 134700

    def test_Toyota_to_string(self):
        """Test to string method."""
        toyota = ToyotaSedan()
        real = "2002 Toyota Camry"
        assert str(toyota) == real
