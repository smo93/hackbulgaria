import unittest
import solution


class BiggestDifferenceTest(unittest.TestCase):
    """docstring for BiggestDifferenceTest"""
    def test_empty_array(self):
        test_array = []
        self.assertEqual(False, solution.biggest_difference(test_array))

    def test_array_of_equals(self):
        test_array = [2,2,2,2,2]
        self.assertEqual(0, solution.biggest_difference(test_array))

    def test_ordinary_array(self):
        test_array = [5, 2, 7, 9]
        self.assertEqual(-7, solution.biggest_difference(test_array))

    def test_with_negative_integers(self):
        test_array = [-10, -9, -1]
        self.assertEqual(-9, solution.biggest_difference(test_array))

if __name__ == '__main__':
    unittest.main()
