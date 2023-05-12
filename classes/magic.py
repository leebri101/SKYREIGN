import random
# magic class
class Spell:
    def __init__(self, name, cost, damage, charm):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.charm = charm
    # Generation of spell damage
    def generate_damage(self):
        low = self.damage - 15
        high = self.damage + 15
        return random.randrange(low, high)