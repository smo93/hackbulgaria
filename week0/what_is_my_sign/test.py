import unittest
import solution


class WhatIsMySignTest(unittest.TestCase):
    """docstring for WhatIsMySignTest"""

    def test_what_is_my_sign(self):
        self.assertEqual('Capricorn', solution.what_is_my_sign(14, 1))
        self.assertEqual('Leo', solution.what_is_my_sign(14, 8))

if __name__ == '__main__':
    unittest.main()
