import unittest
import solution


class CountConsonantsTest(unittest.TestCase):
    """docstring for CountConsonantsTest"""
    def test(self):
        self.assertEqual(4, solution.count_consonants('Python'))
        self.assertEqual(11, solution.count_consonants('Theistareykjarbunga'))
        self.assertEqual(6, solution.count_consonants('A nice day to code!'))

if __name__ == '__main__':
    unittest.main()
