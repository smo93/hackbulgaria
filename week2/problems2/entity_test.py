import unittest
import entity
import weapon


class EntityTest(unittest.TestCase):
    """docstring for EntityTest"""

    def setUp(self):
        self.test_entity = entity.Entity('Entity', 100)

    def test_initialize_entity(self):
        self.assertEqual('Entity', self.test_entity.name)
        self.assertEqual(100, self.test_entity.health)

    def test_get_health(self):
        self.assertEqual(100, self.test_entity.get_health())

    def test_is_alive(self):
        self.assertTrue(self.test_entity.is_alive())

    def test_is_dead(self):
        self.test_entity.take_demage(120)
        self.assertEqual(False, self.test_entity.is_alive())

    def test_take_demage(self):
        self.test_entity.take_demage(50)
        self.assertEqual(50, self.test_entity.get_health())

    def test_take_killing_blow(self):
        self.test_entity.take_demage(120)
        self.assertEqual(0, self.test_entity.get_health())

    def test_take_healing(self):
        self.test_entity.take_demage(50)
        self.test_entity.take_healing(25)
        self.assertEqual(75, self.test_entity.get_health())

    def test_heal_dead(self):
        self.test_entity.take_demage(120)
        self.assertEqual(False, self.test_entity.take_healing(20))

    def test_heal_after_max(self):
        self.test_entity.take_healing(100)
        self.assertEqual(100, self.test_entity.get_health())

    def test_has_no_weapon(self):
        self.assertEqual(False, self.test_entity.has_weapon())

    def test_equip_weapon(self):
        w = weapon.Weapon('dagger', 20, 0.2)
        self.test_entity.equip_weapon(w)
        self.assertTrue(self.test_entity.has_weapon())

    def test_attack(self):
        w = weapon.Weapon('dagger', 20, 0.2)
        self.test_entity.equip_weapon(w)
        possible_demage = [20, 40]
        self.assertIn(self.test_entity.attack(), possible_demage)

if __name__ == '__main__':
    unittest.main()
