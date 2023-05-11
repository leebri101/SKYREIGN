from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Player's Black Magic
fire = Spell("Fireball:", 10, 300, "black")
thunder = Spell("Thunder-bolt:", 15, 450, "black")
blizzard = Spell("Blizzard:", 5, 150, "black")
meteor = Spell("Meteor:", 40, 900, "black")
comet = Spell("Comet of Light:", 80, 1000, "black")

# Enemy's Black Magic
flame = Spell("Dark-Flame", 20, 300, "black")
shadow = Spell("Shadow-Ball", 55, 600, "black")
void = Spell("Void", 70, 850, "black")
darkness = Spell("Darkness", 60, 550, "black")
thrash = Spell("Thrash", 10, 250, "black")

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
kunai = Item("Kunai", "attack", "Deals 100 Damage", 100)
grenade = Item("Grenade", "attack", "Deals 200 Damage", 200)
holy_grenade = Item("Holy-Grenade", "attack", "Deals 500 Damage", 500)

# Characters stats and items
player_spells = [fire, thunder, blizzard, meteor, comet, cure, cura, curaga]
boss_spells = [flame, shadow, void, darkness, cure, cura]
enemy_spells = [flame, thrash, cure]
player_items = [{"item": potion, "quantity": 15},
                {"item": hi_potion, "quantity": 10},
                {"item": super_potion, "quantity": 5},
                {"item": ether, "quantity": 10},
                {"item": elixir, "quantity": 3},
                {"item": hi_elixir, "quantity": 1},
                {"item": kunai, "quantity": 15},
                {"item": grenade, "quantity": 10},
                {"item": holy_grenade, "quantity": 5}]
player1 = Person("Hero : ", 4550, 100, 200, 40, player_spells, player_items)
player2 = Person("Gusak: ", 6450, 150, 250, 70, player_spells, player_items)
player3 = Person("Elora: ", 3500, 200, 175, 35, player_spells, player_items)

# Enemy stats
enemy1 = Person("Skeleton:  ", 2750, 100, 150, 50, enemy_spells, [])
enemy2 = Person("Dark Lord: ", 12000, 500, 600, 100, boss_spells, [])
enemy3 = Person("Imp:       ", 1750, 125, 75, 30, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

# Start of game 
running = True
i = 0
print(bcolors.WHITE + bcolors.BOLD + "==================================")
print("")
print(bcolors.FAIL + bcolors.BOLD + "PREPARE FOR BATTLE!!!" + bcolors.ENDC)
print("")
while running:
    print(bcolors.WHITE + bcolors.BOLD + "==================================")
    
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
    try: 
        index = int(choice) - 1
    except ValueError:
        print("Invalid Input. Please eneter a valid number.")   

        print("")
        print(bcolors.WHITE + bcolors.BOLD + "==================================")

        index = 0
        if index == 0:
            damage = player.generate_damage()
            enemy = player.choose_target(enemies)
            
            enemies[enemy].take_damage(damage)
            print("Attacked " + enemies[enemy].name.replace(" ", ""), bcolors.FAIL, damage, "Points of DMG" + bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has been defeated.")
                del enemies[enemy]

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
                
                enemy = player.choose_target(enemies)
                
                enemies[enemy].take_damage(magic_damage)

                print(bcolors.OKBLUE + "\n" + spell.name + " Deals", str(magic_damage), "Damage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has been defeated.")
                    del enemies[enemy]

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
                player.restore_mp(item.prop)
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
                
                print("\n" + bcolors.FAIL + item.name + " Deals", str(item.prop), "Damage" + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has been defeated.")
                    del enemies[enemy]
    
    # Check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1
    
    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    # Check if player won
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You Won!" + bcolors.ENDC)
        running = False

    # Check if enemy won    
    elif defeated_players == 2:
        print(bcolors.FAIL + "Your party has been defeated!" + bcolors.ENDC)
        running = False 

    # Enemy Attack phase               
    for enemy in enemies:
        enemy_choice = random.randrange(0, 3)
        
        if enemy_choice == 0:
            # Choice of attack
            target = random.randrange(0, 3)
            enemy_damage = enemy.generate_damage()

            players[target].take_damage(enemy_damage)
            print(bcolors.FAIL + bcolors.BOLD + enemy.name.replace(" ", "") + " Attacked " + 
                str(enemy_damage) + " Of Damage" + bcolors.ENDC)

        elif enemy_choice == 1:
            spell, magic_damage = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.charm == "white":
                enemy.heal(magic_damage)
                print(bcolors.OKGREEN + "\n" + spell.name + enemy.name.replace(" ", "") + " Healed", str(magic_damage), "HP" + bcolors.ENDC)
            elif spell.charm == "black":

                target = random.randrange(0, 3)
                
                players[target].take_damage(magic_damage)

                print(bcolors.FAIL + "\n" + spell.name + " Deals", str(magic_damage), "Damage to " + players[target].name.replace(" ", "") + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has been defeated.")
                    del players[player]

            print("Enemy chose", spell, "Damaged", magic_damage)

    print(bcolors.WHITE + bcolors.BOLD + "==================================")
    print("")