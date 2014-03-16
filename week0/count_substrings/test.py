import unittest
import solution


class CountSubstringsTest(unittest.TestCase):
    """docstring for CountSubstringsTest"""
    def test_count_substrings(self):
        self.assertEqual(2,\
                solution.count_substrings("This is a test string", "is"))
        self.assertEqual(2,\
                solution.count_substrings("This is this and that is this",\
                "this"))

if __name__ == '__main__':
    unittest.main()
