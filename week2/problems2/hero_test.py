import unittest
import hero


class HeroTest(unittest.TestCase):
    """docstring for HeroTest"""

    def setUp(self):
        self.hero = hero.Hero('Konan', 100, 'Barbarian')

    def test_initialize_hero(self):
        self.assertEqual('Konan', self.hero.name)
        self.assertEqual(100, self.hero.max_health)
        self.assertEqual('Barbarian', self.hero.nickname)

    def test_known_as(self):
        self.assertEqual('Konan the Barbarian', self.hero.known_as())

if __name__ == '__main__':
    unittest.main()
