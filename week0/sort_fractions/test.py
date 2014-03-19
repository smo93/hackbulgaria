import unittest
import solution


class SortFractionsTest(unittest.TestCase):
    """docstring for CompFractionsTest"""
    def test_sort_fractions(self):
        self.assertEqual([(1, 2), (2, 3)],\
                solution.sort_fractions([(2, 3), (1, 2)]))
        self.assertEqual([(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)],\
                solution.sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8),\
                (9, 6), (15, 32)]))

if __name__ == '__main__':
    unittest.main()
