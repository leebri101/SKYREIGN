# magic class
import random

class Spell:
    def __init__(self, name, cost, dmg, charm):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.charm = charm

    def generate_damage(self):
        low = self.damage - 15
        high = self.damage + 15
        return random.randrange(low, high)