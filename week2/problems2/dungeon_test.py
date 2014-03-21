"""Dungeon module unittests"""
import unittest
from dungeon import Dungeon
from os import remove
from hero import Hero
from orc import Orc
from weapon import Weapon


class DungeonTest(unittest.TestCase):
    """docstring for DungeonTest"""

    def setUp(self):
        self.test_m = ['..##......',
                    '#.##..###.',
                    '#.###.###.',
                    '#..S.S###.',
                    '###.#####.']
        test_map_file = open('test_map.txt', 'w')
        test_map_file.write('\n'.join(self.test_m))
        test_map_file.close()
        self.test_map = Dungeon('test_map.txt')

    def test_print_map(self):
        self.assertEqual('\n'.join(self.test_m), self.test_map.print_map())

    def test_spawn(self):
        hero = Hero('p1', 100, 'first')
        orc = Orc('p2', 100, 2)
        self.test_map.spawn('player1', hero)
        self.assertEqual('H', self.test_map.print_map()[36])
        self.assertEqual('S', self.test_map.print_map()[38])
        self.test_map.spawn('player2', orc)
        self.assertEqual('O', self.test_map.print_map()[38])
        self.assertEqual(False, self.test_map.spawn('player3', orc))

    def tearDown(self):
        remove('test_map.txt')

    def test_move(self):
        after_move = ['..##......',
                    '#.##..###.',
                    '#.###.###.',
                    '#...HO###.',
                    '###.#####.']
        hero = Hero('p1', 100, 'first')
        orc = Orc('p2', 100, 2)
        hero_weapon = Weapon('Axe', 25, 0.1)
        hero.equip_weapon(hero_weapon)
        orc_weapon = Weapon('Stick', 5, 0.01)
        orc.equip_weapon(orc_weapon)
        self.test_map.spawn('player1', hero)
        self.test_map.spawn('player2', orc)
        self.assertTrue(self.test_map.move('player1', 'right'))
        self.assertEqual(False, self.test_map.move('player1', 'up'))
        self.assertEqual(False, self.test_map.move('player1', 'fuckedUpDirection'))
        self.assertEqual('\n'.join(after_move), self.test_map.print_map())
        self.test_map.move('player1', 'right')

    def test_fight(self):
        pass

if __name__ == '__main__':
    unittest.main()
