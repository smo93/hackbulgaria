import unittest
import solution


class CalculateCoinsTest(unittest.TestCase):
    """docstring for CalculateCoinsTest"""
    def test_with_negative_sum(self):
        self.assertEqual(False, solution.calculate_coins(-0.50))

    def test_with_zero(self):
        expected_result = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0}
        self.assertEqual(expected_result, solution.calculate_coins(0))

    def test_with_positive_sum(self):
        expected_result = {1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}
        self.assertEqual(expected_result, solution.calculate_coins(8.94))

if __name__ == '__main__':
    unittest.main()
