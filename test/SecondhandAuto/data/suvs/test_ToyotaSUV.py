"""Test Class for Toyota SUV.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.SecondhandAuto.data.suvs.ToyotaSUV import ToyotaSUV

class TestToyotaSUV():
    """Test class for 'ToyotaSUV.py'."""
    def test_backup_cam_false_on_init(self):
        """Test backup cam init."""
        toyota = ToyotaSUV()
        assert toyota.backup_cam == False

    def test_folded_seats_true_on_init(self):
        """Test nav init."""
        toyota = ToyotaSUV()
        assert toyota.folded_seats == True

    def test_color_on_init(self):
        """Test color init."""
        toyota = ToyotaSUV()
        assert toyota.color == "Silver"

    def test_price_on_init(self):
        """Test price init."""
        toyota = ToyotaSUV()
        assert toyota.price == 16000

    def test_year_on_init(self):
        """Test year init."""
        toyota = ToyotaSUV()
        assert toyota.year == 2012

    def test_make_on_init(self):
        """Test make init."""
        toyota = ToyotaSUV()
        assert toyota.make == "Toyota"

    def test_model_on_init(self):
        """Test model init."""
        toyota = ToyotaSUV()
        assert toyota.model == "Highlander"

    def test_mielage_on_init(self):
        """Test mielage init."""
        toyota = ToyotaSUV()
        assert toyota.mileage == 189400

    def test_Toyota_to_string(self):
        """Test to string method."""
        toyota = ToyotaSUV()
        real = "2012 Toyota Highlander"
        assert str(toyota) == real
