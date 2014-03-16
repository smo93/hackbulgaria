import unittest
import solution


class ContainsDigitsTest(unittest.TestCase):
    """docstring for ContainsDigitsTest"""
    def test(self):
        self.assertEqual(True, solution.contains_digits(402123, [0, 3, 4]))
        self.assertEqual(False, solution.contains_digits(666, [6,4]))
        self.assertEqual(False, solution.contains_digits(123456789, [1,2,3,0]))

if __name__ == '__main__':
    unittest.main()
