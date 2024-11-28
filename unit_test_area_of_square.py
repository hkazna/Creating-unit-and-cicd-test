import unittest
from unittest import*

def area_square_on_the_coordinate_system(a):
    return a * a


class SquareTestCase(unittest.TestCase):
    def test_area_of_square_with_positive_side(self):
        result = area_square_on_the_coordinate_system(10)
        self.assertEqual(result, 100)

    def test_area_of_square_with_zero_side(self):
        result = area_square_on_the_coordinate_system(0)
        self.assertEqual(result, 0)

    def test_area_of_square_with_negative_numbers(self):
        result = area_square_on_the_coordinate_system(-10)
        self.assertEqual(result, 100)

    def test_area_of_square_with_negative_numbers(self):
        result = area_square_on_the_coordinate_system(0)
        self.assertEqual(result, 100)

#command for running unittests:  python.exe -m unittest square.py


