"""Test Class for Chevrolet SUV.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.SecondhandAuto.data.suvs.ChevroletSUV import ChevroletSUV

class TestChevroletSUV():
    """Test class for 'ChevroletSUV.py'."""
    def test_backup_cam_false_on_init(self):
        """Test backup cam init."""
        chevrolet = ChevroletSUV()
        assert chevrolet.backup_cam == False

    def test_folded_seats_true_on_init(self):
        """Test nav init."""
        chevrolet = ChevroletSUV()
        assert chevrolet.folded_seats == True

    def test_color_on_init(self):
        """Test color init."""
        chevrolet = ChevroletSUV()
        assert chevrolet.color == "Red"

    def test_price_on_init(self):
        """Test price init."""
        chevrolet = ChevroletSUV()
        assert chevrolet.price == 8500

    def test_year_on_init(self):
        """Test year init."""
        chevrolet = ChevroletSUV()
        assert chevrolet.year == 2009

    def test_make_on_init(self):
        """Test make init."""
        chevrolet = ChevroletSUV()
        assert chevrolet.make == "Chevrolet"

    def test_model_on_init(self):
        """Test model init."""
        chevrolet = ChevroletSUV()
        assert chevrolet.model == "Trailblazer"

    def test_mielage_on_init(self):
        """Test mielage init."""
        chevrolet = ChevroletSUV()
        assert chevrolet.mileage == 120500

    def test_chevrolet_to_string(self):
        """Test to string method."""
        chevrolet = ChevroletSUV()
        real = "2009 Chevrolet Trailblazer"
        assert str(chevrolet) == real
