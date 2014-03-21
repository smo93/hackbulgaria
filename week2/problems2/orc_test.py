import unittest
import orc
import weapon


class OrcTest(unittest.TestCase):
    """docstring for OrcTest"""

    def setUp(self):
        self.orc = orc.Orc('Orco', 100, 1.5)

    def test_initialize_orc(self):
        self.assertEqual('Orco', self.orc.name)
        self.assertEqual(100, self.orc.health)
        self.assertEqual(1.5, self.orc.berserc_factor)

    def test_attack(self):
        w = weapon.Weapon('dagger', 20, 0.2)
        self.orc.equip_weapon(w)
        possible_demage = [30, 60]
        self.assertIn(self.orc.attack(), possible_demage)

if __name__ == '__main__':
    unittest.main()
