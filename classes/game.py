import random
import pprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    WHITE = '\033[37m'
    CYAN = '\033[36m'
    MAGENTA = '\033[35m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Spells", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def heal(self, damage):
        self.hp += damage
        if self.hp > self.maxhp:
            self.hp = self.maxhp 

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKGREEN + bcolors.BOLD + "Pick An Action:" + bcolors.ENDC)
        for item in self.actions:
            print("  " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + "Select Magic Spell:" + bcolors.ENDC)
        for spell in self.magic:
            print("  " +str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
    
    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "Select Item:" + bcolors.ENDC)
        for item in self.items:
            print("  " + str(i) + ".", item["item"].name, (item["item"].description), "(x" + str(item["quantity"]) + ")")
            i += 1

    def get_stats(self):
        hp_bar = ""
        hp_ticks = (self.hp / self.maxhp) * 100 / 4
        
        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 5

        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1
        while len(mp_bar) < 15:
            mp_bar += " "
        
        print("                 _________________________")
        print(bcolors.BOLD + self.name + str(self.hp) + "/" + str(self.maxhp) + "|" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|")
        print("                 _______________")
        print("     " + bcolors.BOLD + "MP: " + str(self.mp) + "/" + str(self.maxmp) + "|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + bcolors.BOLD + "|")