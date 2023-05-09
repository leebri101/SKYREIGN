from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Black Magic
fire = Spell("Fireball:", 10, 300, "black")
thunder = Spell("Thunder-bolt:", 15, 450, "black")
blizzard = Spell("Blizzard:", 5, 150, "black")
meteor = Spell("Meteor:", 40, 900, "black")

# White Magic
cure = Spell("Cure:", 5, 150, "white")
cura = Spell("Cura:", 10, 350, "white")
curaga = Spell("Curaga:", 30, 750, "white")

# Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 150 HP", 150)
super_potion = Item("Super-Potion", "potion", "Heals 150 HP", 200)
elixir = Item("Elixir", "elixir", "Restores HP/MP of one party member", 1000)
hi_elixir = Item("Hi-Elixir", "elixir", "Fully restores HP/MP of all members", 9999)
ether = Item("Ether", "ether", "Restores 50 MP", 50)
dagger = Item("Dagger", "attack", "Deals 50 Damage", 50)
kunai = Item("Kunai", "attack", "Deals 100 Damage", 100)
grenade = Item("Grenade", "attack", "Deals 200 Damage", 200)

# Characters stats and items
player_spells = [fire, thunder, blizzard, meteor, cure, cura, curaga]
player_items = [{"item": potion, "quantity": 15},
                {"item": hi_potion, "quantity": 10},
                {"item": super_potion, "quantity": 5},
                {"item": ether, "quantity": 10},
                {"item": elixir, "quantity": 3},
                {"item": hi_elixir, "quantity": 1},
                {"item": dagger, "quantity": 15},
                {"item": kunai, "quantity": 10},
                {"item": grenade, "quantity": 5}]
player1 = Person("Hero : ", 4550, 200, 100, 40, player_spells, player_items)
player2 = Person("Gusak: ", 6450, 250, 150, 70, player_spells, player_items)
player3 = Person("Elora: ", 3500, 175, 200, 35, player_spells, player_items)

# Enemy stats
enemy1 = Person("Skeleton:  ", 2750, 100, 150, 50, [], [])
enemy2 = Person("Dark Lord: ", 12000, 600, 300, 90, [], [])
enemy3 = Person("Imp:       ", 2500, 125, 75, 30, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

# Start of game 
running = True
i = 0
print(bcolors.WHITE + bcolors.BOLD + "==================================")
print(bcolors.FAIL + bcolors.BOLD + "Enemy Attack!!!" + bcolors.ENDC)

while running:
    print("=" * 100 + bcolors.WHITE + bcolors.BOLD + "==================================")
    
    print("\n\n")
    print("NAME")
    for player in players:
        player.get_stats()
    
    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input(bcolors.CYAN + bcolors.BOLD + "Choose Action:")
        index = int(choice) - 1

        print("")
        print(bcolors.WHITE + bcolors.BOLD + "==================================")

        if index == 0:
            damage = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(damage)
            print("\n" + bcolors.BOLD + "Attacked " + enemies[enemy].name, bcolors.FAIL, damage, "Points of DMG" + bcolors.ENDC)

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
                print(bcolors.OKGREEN + "\n" + spell.name + player.name + " Healed", str(magic_damage), "HP" + bcolors.ENDC)
            elif spell.charm == "black":
                if len(enemies) == 0:
                    print("No enemies left!")
                enemy = player.choose_target(enemies)
                if enemy >= len(enemies):
                    print("Invalid enemy target!")
                enemies[enemy].take_damage(magic_damage)

                print(bcolors.OKBLUE + "\n" + spell.name + " Deals", str(magic_damage), "Damage to " + enemies[enemy].name + bcolors.ENDC)

        elif index == 2:
            player.choose_item()

            print("")
            item_choice = int(input("Choose Item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + '\n' + "No " + item.name + " left..." + bcolors.ENDC)
                continue
            
            player.items[item_choice]["quantity"] -= 1
            print("Selected Item: " + item.name)

            if isinstance(item, Item) and item.category == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " Healed", str(item.prop), "HP" + bcolors.ENDC)
            elif isinstance(item, Item) and item.category == "ether":
                player.mp(item.prop)
                print(bcolors.OKBLUE + "\n" + item.name + " Restored", str(item.prop), "MP" + bcolors.ENDC)
            elif isinstance(item, Item) and item.category == "elixir":

                if item.name == "Hi-Elixir":
                    for i in players:
                        i.hp = player.maxhp
                        i.mp = player.maxmp  
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.MAGENTA + bcolors.BOLD + "\n" + item.name + " fully restores HP/MP", str(item.prop), bcolors.ENDC) 
            elif isinstance(item, Item) and item.category == "attack":

                enemy = player.choose_target(enemies)
                
                enemies[enemy].take_damage(item.prop)
                
                print(bcolors.FAIL + "\n" + item.name + " Deals", str(item.prop), "Damage" + bcolors.ENDC)
    enemy_choice = 1
    target = random.randrange(0, 3)
    enemy_damage = enemies[0].generate_damage()

    players[target].take_damage(enemy_damage)
    print(bcolors.FAIL + bcolors.BOLD + enemies[enemy].name + "Attacked", enemy_damage, "Of Damage" + bcolors.ENDC)

    print(bcolors.WHITE + bcolors.BOLD + "==================================")
    print("")
    
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1
    
    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You Won!" + bcolors.ENDC)
        running = False
        
    elif defeated_players == 0:
        print(bcolors.FAIL + "Your party has been defeated!" + bcolors.ENDC)
        running = False