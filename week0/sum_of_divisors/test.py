import unittest
import solution


class SumOfDivisorsTest(unittest.TestCase):
    """docstring for SumOfDivisorsTest"""
    def test_sum_of_divisors(self):
        self.assertEqual(2340, solution.sum_of_divisors(1000))
        self.assertEqual(15, solution.sum_of_divisors(8))

if __name__ == '__main__':
    unittest.main()
