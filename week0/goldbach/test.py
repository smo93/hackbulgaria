import unittest
import solution


class GoldbachTest(unittest.TestCase):
    """docstring for GoldbachTest"""
    def test_goldbach(self):
        expected = [(2, 2)]
        self.assertEqual(expected, solution.goldbach(4))
        expected = [(3, 7), (5, 5)]
        self.assertEqual(expected, solution.goldbach(10))
        expected = [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]
        self.assertEqual(expected, solution.goldbach(100))

if __name__ == '__main__':
    unittest.main()
