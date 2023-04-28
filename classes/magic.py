# magic class
import random

class spell:
    def __init__(self, name, mp, cost, dmg):
        self.name = name
        self.mp = mp
        self.cost = cost
        self.dmg = dmg


    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)