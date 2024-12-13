"""Test Class for Lot.py.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

import pytest
from src.SecondhandAuto.data.lot.Lot import Lot


class TestLot():
    """Test class for 'Lot.py'."""
    @pytest.mark.parametrize("mileage", [98000, 150000, 250000])
    def test_get_our_price_correct(self, mileage):
        """Test get our price."""
        market_value = 12000
        if mileage <= 100000:
            value = market_value - (.1 * market_value)
        elif mileage > 100000 and mileage <= 200000:
            value = market_value - (.25 * market_value)
        else:
            value = market_value - (.45 * market_value)
        assert value == Lot().get_our_price(mileage, market_value)
