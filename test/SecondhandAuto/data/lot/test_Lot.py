"""Test Class for Lot.py.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.SecondhandAuto.data.sedans.HondaSedan import HondaSedan

class TestLot():
    """Test class for 'Lot.py'."""
    @pytest.mark.parametrize("mileage", [98000, 150000, 250000])
    def test_get_our_price_correct(self, mileage):
        market_value = 12000
        if mileage <= 100000:
            value = market_value - (.1 * market_value)
        elif mileage > 100000 and mileage <= 200000:
            val = market_value - (.25 * market_value)
        else:
            val = market_value - (.45 * market_value)
