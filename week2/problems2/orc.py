from entity import Entity


class Orc(Entity):
    """docstring for Orc"""
    def __init__(self, name, health, berserc_factor):
        super().__init__(name, health)
        if berserc_factor < 1:
            self.berserc_factor = 1
        elif berserc_factor > 2:
            self.berserc_factor = 2
        else:
            self.berserc_factor = berserc_factor

    def attack(self):
        if not self.has_weapon():
            return 0
        else:
            if self.weapon.critical_hit():
                return 2 * self.berserc_factor * self.weapon.demage
            else:
                return self.berserc_factor * self.weapon.demage
