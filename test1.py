import unittest
from your_module_name import max_water_area

class TestMaxWaterArea(unittest.TestCase):
    def test_max_water_area(self):
        # Test case where the maximum area is in the middle of the array
        self.assertEqual(max_water_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

        # Test case where the maximum area is at the beginning of the array
        self.assertEqual(max_water_area([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 25)

        # Test case where the maximum area is at the end of the array
        self.assertEqual(max_water_area([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 25)

        # Test case where all heights are equal
        self.assertEqual(max_water_area([5, 5, 5, 5, 5, 5]), 25)

        # Test case where heights are in descending order
        self.assertEqual(max_water_area([10, 8, 6, 4, 2, 1]), 10)

        # Test case where heights are in ascending order
        self.assertEqual(max_water_area([1, 2, 4, 6, 8, 10]), 10)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
