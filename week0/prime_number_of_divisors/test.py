import unittest
import solution


class PrimeNumberOfDivisorsTest(unittest.TestCase):
    """docstring for PrimeNumberOfDivisorsTest"""
    def test_prime_number_of_divisors(self):
        self.assertTrue(solution.prime_number_of_divisors(7))
        self.assertFalse(solution.prime_number_of_divisors(8))
        self.assertTrue(solution.prime_number_of_divisors(9))

if __name__ == '__main__':
    unittest.main()
