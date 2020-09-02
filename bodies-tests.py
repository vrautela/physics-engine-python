import unittest
from bodies import *

class TestBodyConstructors(unittest.TestCase):
    def test_negative_mass(self):
        with self.assertRaises(ValueError):
            Body(-2, 3, 4)

    def test_zero_mass(self):
        with self.assertRaises(ValueError):
            Body(0, 3, 4)

class TestRoundBodyConstructor(TestBodyConstructors):
    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            RoundBody(2, 4, 6, -3)

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            RoundBody(2, 4, 6, 0)

class TestSquareBodyConstructor(TestBodyConstructors):
    def test_negative_side_length(self):
        with self.assertRaises(ValueError):
            SquareBody(2, 4, 6, -3)

    def test_zero_side_length(self):
        with self.assertRaises(ValueError):
            SquareBody(2, 4, 6, 0)

if __name__ == '__main__':
    unittest.main()
