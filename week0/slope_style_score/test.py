import unittest
import solution


class SlopeStyleScoreTest(unittest.TestCase):
    """docstring for SlopeStyleScoreTest"""
    def test_slope_style_score(self):
        self.assertEqual(94.66,\
                solution.slope_style_score([94, 95, 95, 95, 90]))
        self.assertEqual(80.0,\
                solution.slope_style_score([60, 70, 80, 90, 100]))

if __name__ == '__main__':
    unittest.main()
