import unittest
import solution


class PrimeFactorizationTest(unittest.TestCase):
    """docstring for PrimeFactorializationTest"""
    def test_prime_factorization(self):
        self.assertEqual([(2,1), (5,1)], solution.prime_factorization(10))
        self.assertEqual([(2, 2), (89, 1)], solution.prime_factorization(356))

if __name__ == '__main__':
    unittest.main()
