"""Test Class for Honda Sedan.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""


from src.SecondhandAuto.data.sedans.HondaSedan import HondaSedan


class TestHondaSedan():
    """Test class for 'HondaSedan.py'."""
    def test_led_lights_false_on_init(self):
        """Test LED lights init."""
        honda = HondaSedan()
        assert honda.led_lights

    def test_nav_system_true_on_init(self):
        """Test nav init."""
        honda = HondaSedan()
        assert honda.nav_system

    def test_color_on_init(self):
        """Test color init."""
        honda = HondaSedan()
        assert honda.color == "Maroon"

    def test_price_on_init(self):
        """Test price init."""
        honda = HondaSedan()
        assert honda.price == 12000

    def test_year_on_init(self):
        """Test year init."""
        honda = HondaSedan()
        assert honda.year == 2012

    def test_make_on_init(self):
        """Test make init."""
        honda = HondaSedan()
        assert honda.make == "Honda"

    def test_model_on_init(self):
        """Test model init."""
        honda = HondaSedan()
        assert honda.model == "Civic"

    def test_mielage_on_init(self):
        """Test mielage init."""
        honda = HondaSedan()
        assert honda.mileage == 280450

    def test_honda_to_string(self):
        """Test to string method."""
        honda = HondaSedan()
        real = "2012 Honda Civic"
        assert str(honda) == real
