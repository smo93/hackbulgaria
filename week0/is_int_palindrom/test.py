import unittest
import solution


class IsIntPalindromTest(unittest.TestCase):
    """docstring for IsIntPalindromTest"""
    def test_is_int_palindrom(self):
        self.assertTrue(solution.is_int_palindrom(100001))
        self.assertTrue(solution.is_int_palindrom(999))
        self.assertFalse(solution.is_int_palindrom(123))

if __name__ == '__main__':
    unittest.main()
