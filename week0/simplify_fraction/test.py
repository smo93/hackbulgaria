import unittest
import solution


class SimplifyFractionTest(unittest.TestCase):
    """docstring for SimplifyFractionTest"""
    def test_simplify_fractoin(self):
        self.assertEqual((1, 3), solution.simplify_fraction((3, 9)))
        self.assertEqual((3, 22), solution.simplify_fraction((63, 462)))

if __name__ == '__main__':
    unittest.main()
