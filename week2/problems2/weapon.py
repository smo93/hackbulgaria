from random import randint


class Weapon():
    """docstring for Weapon"""
    def __init__(self, type, demage, critical_strike_percent):
        self.type = type
        self.demage = demage
        if critical_strike_percent < 0:
            self.critical_strike_percent = 0
        elif critical_strike_percent > 1:
            self.critical_strike_percent = 1
        else:
            self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        if randint(0, 1000) < self.critical_strike_percent * 1000:
            return True
        return False
