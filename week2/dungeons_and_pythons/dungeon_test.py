import unittest
from dungeon import Dungeon


class DungeonTest(unittest.TestCase):
    def setUp(self):
        self.dungeon = Dungeon()

    def test_load_first_level(self):
        first_lvl_map = 'S..P..........PPI###############\n'\
                        '.#########.#####################\n'\
                        '.....P.........................A\n'\
                        '.####.##.###.###################\n'\
                        'P####.##.###.#####.....#########\n'\
                        '.####.##.###.#####.###.##IIIIII#\n'\
                        'P####.I..###.#####.###.##P....I#\n'\
                        '.####P##P###.......###.##P######\n'\
                        'P####.##.############.........A.\n'\
                        'I####A...######################G'
        dungeon_map = '\n'.join([''.join(row) for row in self.dungeon.map])
        self.assertEqual(first_lvl_map, dungeon_map)

if __name__ == '__main__':
    unittest.main()
