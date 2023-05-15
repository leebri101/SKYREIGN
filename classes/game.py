import random
import pprint


# Colors and styling
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    GREEN = '\033[92m'
    FAIL = '\033[91m'
    WHITE = '\033[37m'
    CYAN = '\033[36m'
    MAGENTA = '\033[35m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


# Coding which defines
# all characters
# and enemies within the code.
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
    """
    Random generation of atk damage
    """
    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_dmg(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    # Healing and restoration of MP
    # HP stats,
    # MP stats
    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def restore_mp(self, sum):
        self.mp += sum
        if self.mp > self.maxmp:
            self.mp = self.maxmp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp
    """
    Reduction of MP and spells which
    displays the cost of each spell for the player
    """
    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]
    """
    choice of actions for
    players
    """
    def choose_action(self):
        i = 1
        print(f"{bcolors.WHITE}{bcolors.BOLD}================================")
        print("")
        print(bcolors.BOLD + self.name + bcolors.ENDC)
        print("")
        print(f"{bcolors.GREEN}{bcolors.BOLD}Pick An Action:{bcolors.ENDC}")

        for item in self.actions:
            print("  " + str(i) + ".", item)
            i += 1
    """
    Choice of meagic spells
    for players
    """
    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + "Select Magic Spell:" + bcolors.ENDC)
        for spell in self.magic:
            print(f"  {i}. {spell.name} (cost: {spell.cost})")
            i += 1
    """
    Item choices for players
    to use against enemies
    """
    def choose_item(self):
        i = 1
        print(f"\n{bcolors.GREEN}{bcolors.BOLD}Select Item:{bcolors.ENDC}")
        for item in self.items:
            txt = f"{i}.{item['item'].name} {item['item'].info} (x{item['sum']})"
            print(txt)
            i += 1
    """
    Players having the choice
    to target any charcters
    with any actions prompted
    before hand.
    """
    def choose_target(self, enemies):
        i = 1
        print("")
        print(bcolors.FAIL + bcolors.BOLD + "TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("  " + str(i) + ".", enemy.name)
            i += 1
        print("")
        choice = int(input("Choose Target:")) - 1
        return choice
    """
    Enemy stat bars
    which show a
    simple display
    of a bars which are
    indicated by a red color
    """
    def get_enemy_stats(self):
        hp_bar = ""
        hp_ticks = (self.hp / self.maxhp) * 100 / 2

        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        hp_now = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)
            while decreased > 0:
                hp_now += " "
                decreased -= 1

            hp_now += hp_string
        else:
            hp_now = hp_string

        txt = f"\n{self.name} HP: {hp_now}|{bcolors.FAIL}{hp_bar}{bcolors.ENDC}|"
        print(txt)

    """
    Player stat bars,s
    which are shown,
    with HP and MP bar,
    green for HP and
    blue for MP.
    """
    def get_stats(self):
        hp_bar = ""
        hp_ticks = (self.hp / self.maxhp) * 100 / 4
        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        hp_now = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            while decreased > 0:
                hp_now += " "
                decreased -= 1

            hp_now += hp_string
        else:
            hp_now = hp_string
        mp_string = str(self.mp) + "/" + str(self.maxmp)
        mp_now = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                mp_now += " "
                decreased -= 1

            mp_now += mp_string
        else:
            mp_now = mp_string

        txt = f"\n{self.name} HP:{hp_now}|{bcolors.GREEN}{hp_bar}{bcolors.ENDC}|"
        print(txt)
        txt = f"\nMP: {mp_now}|{bcolors.OKBLUE}{mp_bar}{bcolors.ENDC}|"
        print(txt)
    '''
    Enemies can choose spells
    to attack players at random
    '''
    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_dmg()

        pct = self.hp / self.maxhp * 100

        if self.mp < spell.cost or spell.charm == "white" and pct > 50:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg
