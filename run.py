from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Black Magic
fire = Spell("Fireball:", 10, 100, "black")
thunder = Spell("Thunder-bolt:", 15, 150, "black")
blizzard = Spell("Blizzard:", 5, 50, "black")
meteor = Spell("Meteor:", 20, 200, "black")

# White Magic
cure = Spell("Cure:", 5, 50, "white")
cura = Spell("Cura:", 10, 100, "white")
curaga = Spell("Curaga:", 15, 150, "white")

# Items
potion = Item("Potion", "potion", "Heals 25 HP", 25)
hi_potion = Item("HI-Potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super-Potion", "potion", "Heals 150 HP", 150)
elixir = Item("Elixir", "elixir", "Restores HP/MP of one party member", 500)
hi_elixir = Item("HI-Elixir", "elixir", "Fully restores HP/MP of all members", 9999)

dagger = Item("Dagger", "attack", "Deals 150 Damage", 150)
kunai = Item("Kunai", "attack", "Deals 250 Damage", 250)
grenade = Item("Grenade", "attack", "Deals 500 Damage", 500)

# Characters stats
player_spells = [fire, thunder, blizzard, meteor, cure, cura, curaga]
player_items = [{"item": potion, "quantity": 15},
                {"item": hi_potion, "quantity": 10},
                {"item": super_potion, "quantity": 5},
                {"item": elixir, "quantity": 3},
                {"item": hi_elixir, "quantity": 1},
                {"item": dagger, "quantity": 15},
                {"item": kunai, "quantity": 10},
                {"item": grenade, "quantity": 5}]
player = Person(5460, 150, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0
print(bcolors.WHITE + bcolors.BOLD + "==================================")
print(bcolors.FAIL + bcolors.BOLD + "Enemy Attack!!!" + bcolors.ENDC)

while running:
    print(bcolors.WHITE + bcolors.BOLD + "==================================")

    player.choose_action()
    choice = input(bcolors.CYAN + bcolors.BOLD + "Choose Action:")
    index = int(choice) - 1

    print(bcolors.WHITE + bcolors.BOLD + "==================================")

    if index == 0:
        damage = player.generate_damage()
        enemy.take_damage(damage)
        print(bcolors.OKBLUE + bcolors.BOLD + "You attacked", damage, "Points of DMG.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Spell: ")) - 1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_damage = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + bcolors.BOLD + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.charm == "white":
            player.heal(magic_damage)
            print(bcolors.OKGREEN + "\n" + spell.name + " Player Healed", str(magic_damage), "HP" + bcolors.ENDC)
        elif spell.charm == "black":
            enemy.take_damage(magic_damage)
            print(bcolors.OKBLUE + "\n" + spell.name + " Deals", str(magic_damage), "Damage" + bcolors.ENDC)

    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose Item: ")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]["item"]
        print("Selected Item:", item.name, "-", item.category)

        if isinstance(item, Item) and item.category == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " Healed", str(item.prop), "HP" + bcolors.ENDC)
        elif isinstance(item, Item) and item.category == "elixir":
            player.heal(item.prop)
            player.hp = player.maxhp
            plaeyr.mp = player.maxmp
            print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP", str(item.prop), bcolors.ENDC) 
        elif isinstance(item, Item) and item.category == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " Deals", str(item.prop), "Damage" + bcolors.ENDC)
    
        

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print(bcolors.FAIL + bcolors.BOLD + "Enemy Attacked", enemy_damage, "Of Damage" + bcolors.ENDC)

    print(bcolors.WHITE + bcolors.BOLD + "==================================")
    print("")
    print("Player HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")
    
    print(bcolors.WHITE + bcolors.BOLD + "Player MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")
    
    print(bcolors.WHITE + bcolors.BOLD + "Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Won!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your party has been defeated!" + bcolors.ENDC)
        running = False