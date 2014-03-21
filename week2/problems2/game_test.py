import unittest
import game


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = game.Game('map.txt')


if __name__ == '__main__':
    unittest.main()
