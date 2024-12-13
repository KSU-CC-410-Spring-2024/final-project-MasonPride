"""Test Class for Custom Vehicle.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

import pytest
from src.SecondhandAuto.data.CustomVehicle import CustomVehicle


class TestCustomVehicle():
    """Test class for CustomVehicle."""
    def test_year_is_none_init(self):
        """Test year init."""
        custom = CustomVehicle()
        assert custom.year is None

    def test_make_is_none_init(self):
        """Test make init."""
        custom = CustomVehicle()
        assert custom.make is None

    def test_model_is_none_init(self):
        """Test model init."""
        custom = CustomVehicle()
        assert custom.model is None

    def test_price_is_0_init(self):
        """Test price init."""
        custom = CustomVehicle()
        assert custom.price is None

    def test_mielage_is_0_init(self):
        """Test mileage init."""
        custom = CustomVehicle()
        assert custom.mileage is None

    @pytest.mark.parametrize("year", [1999, 2012, 2003, 2026])
    def test_year_setter_works(self, year):
        """Test year setter."""
        custom = CustomVehicle()
        custom.year = year
        assert year == custom.year

    @pytest.mark.parametrize("make", ["Toyota", "Dodge", "Ford", "Chevrolet"])
    def test_make_setter_works(self, make):
        """Test make setter."""
        custom = CustomVehicle()
        custom.make = make
        assert make == custom.make

    @pytest.mark.parametrize("model", ["Trailblazer", "Camry", "Fiat",
                             "Highlander"])
    def test_model_setter_works(self, model):
        """Test model setter."""
        custom = CustomVehicle()
        custom.model = model
        assert model == custom.model

    @pytest.mark.parametrize("price", [0, 45000, 24000, 123456789])
    def test_price_setter_works(self, price):
        """Test price setter."""
        custom = CustomVehicle()
        custom.price = price
        assert price == custom.price

    @pytest.mark.parametrize("mileage", [0, 250000, 670000, 123456789])
    def test_mileage_setter_works(self, mileage):
        """Test mileage setter."""
        custom = CustomVehicle()
        custom.mileage = mileage
        assert mileage == custom.mileage

    def test_custom_to_string(self):
        """Test to string method."""
        custom = CustomVehicle("2010", "Kia", "Forte")
        real = "2010 Kia Forte"
        assert str(custom) == real
