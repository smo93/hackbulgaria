import unittest
import solution


class SumOfDigitsTest(unittest.TestCase):
    """docstring for SumOfDigitsTest"""
    def test_sum_of_digits(self):
        self.assertEqual(6, solution.sum_of_digits(123))
        self.assertEqual(43, solution.sum_of_digits(1325132435356))

if __name__ == '__main__':
    unittest.main()
