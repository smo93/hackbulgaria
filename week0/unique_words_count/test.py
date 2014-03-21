import unittest
import solution


class UniqueWordsCountTest(unittest.TestCase):
    """docstring for UniqueWordsCountTest"""
    def test_unique_words_count(self):
        self.assertEqual(3, solution.unique_words_count(["apple", "banana",
            "apple", "pie"]))
        self.assertEqual(2, solution.unique_words_count(["python", "python",
            "python", "ruby"]))

if __name__ == '__main__':
    unittest.main()
