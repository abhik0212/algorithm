import unittest
from interleaving import check_interleave


class PrimesTestCase(unittest.TestCase):
    """Tests for interleaving.py."""

    def test_1(self):
        """"XXY", "XXZ", "XXXXZY" is interleaving"""
        self.assertTrue(check_interleave("XXY", "XXZ", "XXXXZY"))

    def test_2(self):
        """"XY", "X", "XXY" is interleaving"""
        self.assertTrue(check_interleave("XY", "X", "XXY"))

    def test_3(self):
        """"YX", "X", "XXY" is not interleaving"""
        self.assertFalse(check_interleave("YX", "X", "XXY"))

if __name__ == '__main__':
    unittest.main()
