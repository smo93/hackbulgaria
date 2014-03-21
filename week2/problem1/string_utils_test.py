import string_utils
import unittest


class string_utils_Test(unittest.TestCase):

    def test_lines(self):
        self.assertEqual(['asd', 'asd'], string_utils.lines('asd\nasd'))

    def test_lines2(self):
        self.assertEqual(['asd', 'asd'], string_utils.lines('asd\nasd\n'))

    def test_unlines(self):
        self.assertEqual('asd\nasd', string_utils.unlines(['asd', 'asd']))

    def test_words(self):
        self.assertEqual(['asd', 'asd'], string_utils.words('asd asd'))

    def test_words2(self):
        self.assertEqual(['asd', 'asd'], string_utils.words('asd\nasd'))

    def test_unwords(self):
        self.assertEqual('asd asd', string_utils.unwords(['asd', 'asd']))

    def test_tabs_to_spaces(self):
        self.assertEqual('    asd', string_utils.tabs_to_spaces('\tasd', 4))

    def test_tabs_to_spaces2(self):
        self.assertEqual('    a\na', string_utils.tabs_to_spaces('\ta\na', 4))

if __name__ == '__main__':
    unittest.main()
