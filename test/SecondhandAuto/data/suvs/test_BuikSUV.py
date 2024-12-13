"""Test Class for buik SUV.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from src.SecondhandAuto.data.suvs.BuikSUV import BuikSUV


class TestBuikSUV():
    """Test class for 'buikSUV.py'."""
    def test_backup_cam_false_on_init(self):
        """Test backup cam init."""
        buik = BuikSUV()
        assert buik.backup_cam

    def test_folded_seats_true_on_init(self):
        """Test nav init."""
        buik = BuikSUV()
        assert buik.folded_seats

    def test_color_beige_on_init(self):
        """Test color init."""
        buik = BuikSUV()
        assert buik.color == "Blue"

    def test_price_on_init(self):
        """Test price init."""
        buik = BuikSUV()
        assert buik.price == 12000

    def test_year_on_init(self):
        """Test year init."""
        buik = BuikSUV()
        assert buik.year == 2010

    def test_make_on_init(self):
        """Test make init."""
        buik = BuikSUV()
        assert buik.make == "Buik"

    def test_model_on_init(self):
        """Test model init."""
        buik = BuikSUV()
        assert buik.model == "Enclave"

    def test_mielage_on_init(self):
        """Test mielage init."""
        buik = BuikSUV()
        assert buik.mileage == 240000

    def test_buik_to_string(self):
        """Test to string method."""
        buik = BuikSUV()
        real = "2010 Buik Enclave"
        assert str(buik) == real
