# magic class
import random

class spell:
    def __init__(self, name, cost, dmg, type_of_magic):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type_of_magic = type_of_magic


    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)