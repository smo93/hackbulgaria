import unittest
import solution


class IsPrimeTest(unittest.TestCase):
    """docstring for IsPrimeTest"""
    def test_is_prime(self):
        self.assertTrue(solution.is_prime(2))
        self.assertTrue(solution.is_prime(11))
        self.assertFalse(solution.is_prime(1))
        self.assertFalse(solution.is_prime(-10))

if __name__ == '__main__':
    unittest.main()
