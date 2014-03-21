# pylint: disable=R0904
"""doc"""
from random import randint
from hero import Hero
from orc import Orc


class Fight():
    """docstring for Fight"""
    def __init__(self, hero, orc):
        self.hero = None
        self.orc = None
        self.first = None
        if type(hero) is Hero and type(orc) is Orc:
            self.hero = hero
            self.orc = orc
        else:
            raise ValueError('Wrong type of arguments! Given {}'.format(type(orc)))
        if randint(0, 100) < 50:
            self.first = 1
        else:
            self.first = 2

    def simulate_fight(self):
        """docstring for simulate_fight"""
        fight_result = []
        who_hits = self.first
        while self.hero.is_alive() and self.orc.is_alive():
            if who_hits == 1:
                hero_dmg = self.hero.attack()
                self.orc.take_demage(hero_dmg)
                fight_result.append('%s hits %s for %d demage!' %\
                        (self.hero.known_as(), self.orc.name, hero_dmg))
                who_hits = 2
            else:
                orc_dmg = self.orc.attack()
                self.hero.take_demage(orc_dmg)
                fight_result.append('%s hits %s for %d demage!' %\
                        (self.orc.name, self.hero.known_as(), orc_dmg))
                who_hits = 1
        winner = ''
        if self.hero.is_alive():
            fight_result.append('%s wins the fight!' % (self.hero.known_as()))
            winner = 'H'
        else:
            fight_result.append('%s wins the fight!' % (self.orc.name))
            winner = 'O'
        return ('\n'.join(fight_result), winner)

