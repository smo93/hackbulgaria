import unittest
import solution


class ContainsDigitsTest(unittest.TestCase):
    """docstring for ContainsDigitsTest"""
    def test(self):
        self.assertEqual(False, solution.contains_digit(123, 4))
        self.assertEqual(True, solution.contains_digit(123, 2))
        self.assertEqual(True, solution.contains_digit(1000, 0))
        self.assertEqual(False, solution.contains_digit(12346789, 5))

if __name__ == '__main__':
    unittest.main()
