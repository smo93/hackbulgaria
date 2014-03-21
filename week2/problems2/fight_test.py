# pylint: disable=R0904
"""unittests for the fight class"""
import unittest
import fight
from hero import Hero
from orc import Orc
from weapon import Weapon


class FightTest(unittest.TestCase):
    """docstring for FightTest"""
    def setUp(self):
        weapon = Weapon('Dagger', 10, 0.0)
        hero = Hero('Asd', 100, 'Hero')
        hero.equip_weapon(weapon)
        orc = Orc('Dsa', 1, 1.4)
        orc.equip_weapon(weapon)
        self.fight = fight.Fight(hero, orc)

    def test_initialize_fight(self):
        """test"""
        self.assertNotEqual(None, self.fight.hero)
        self.assertNotEqual(None, self.fight.orc)
        self.assertIn(self.fight.first, [1, 2])

    def test_simulate_fight(self):
        """docstring for test_simulate_fight"""
        when_hero_starts = 'Asd the Hero hits Dsa for 10 demage!\n' \
                            'Asd the Hero wins the fight!'
        when_orc_starts = 'Dsa hits Asd the Hero for 14 demage!\n' \
                            'Asd the Hero hits Dsa for 10 demage!\n' \
                            'Asd the Hero wins the fight!'
        if self.fight.first is 1:
            self.assertEqual(when_hero_starts, self.fight.simulate_fight()[0])
        else:
            self.assertEqual(when_orc_starts, self.fight.simulate_fight()[0])

if __name__ == '__main__':
    unittest.main()
