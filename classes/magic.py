import random
# magic class


class Spell:
    def __init__(self, name, cost, dmg, charm):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.charm = charm

    """
    Generation of spell damage
    """
    def generate_dmg(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)
