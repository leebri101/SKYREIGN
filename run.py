from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Player's Black Magic
fire = Spell("Fireball", 10, 300, "black")
thunder = Spell("Thunder-bolt", 15, 450, "black")
blizzard = Spell("Blizzard", 5, 150, "black")
meteor = Spell("Meteor", 40, 900, "black")
comet = Spell("Comet of Light", 80, 1000, "black")

# Enemy's Black Magic
flame = Spell("Dark-Flame", 20, 300, "black")
shadow = Spell("Shadow-Ball", 55, 600, "black")
void = Spell("Void", 70, 850, "black")
darkness = Spell("Darkness", 60, 550, "black")
thrash = Spell("Thrash", 10, 250, "black")

# White Magic
cure = Spell("Cure", 10, 200, "white")
cura = Spell("Cura", 15, 600, "white")
curaga = Spell("Curaga", 30, 1000, "white")

# Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 150 HP", 150)
super_potion = Item("Super-Potion", "potion", "Heals 150 HP", 200)
elixir = Item("Elixir", "elixir", "Restores HP/MP of one party member", 1000)
hi_elixir = Item("Hi-Elixir", "elixir", "Restores HP/MP of all members", 9999)
ether = Item("Ether", "ether", "Restores 50 MP", 50)
kunai = Item("Kunai", "attack", "Deals 100 Damage", 100)
grenade = Item("Grenade", "attack", "Deals 200 Damage", 200)
holy_grenade = Item("Holy-Grenade", "attack", "Deals 500 Damage", 500)

# Characters stats and items
player_spells = [fire, thunder, blizzard, meteor, comet, cure, cura, curaga]
boss_spells = [flame, shadow, void, darkness, cure, cura]
enemy_spells = [flame, thrash, cure]
player_items = [{"item": potion, "amount": 15},
                {"item": hi_potion, "amount": 10},
                {"item": super_potion, "amount": 5},
                {"item": ether, "amount": 10},
                {"item": elixir, "amount": 5},
                {"item": hi_elixir, "amount": 2},
                {"item": kunai, "amount": 15},
                {"item": grenade, "amount": 10},
                {"item": holy_grenade, "amount": 5}]
player1 = Person("Hero  ", 4550, 100, 200, 40, player_spells, player_items)
player2 = Person("Gusak ", 6450, 150, 250, 70, player_spells, player_items)
player3 = Person("Elora ", 3500, 200, 175, 35, player_spells, player_items)

# Enemy stats
enemy1 = Person("Skeleton  ", 2750, 100, 150, 50, enemy_spells, [])
enemy2 = Person("Dark-Lord ", 12000, 500, 600, 100, boss_spells, [])
enemy3 = Person("Imp       ", 1750, 125, 75, 30, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

# Start of game
running = True
i = 0

print(f"{bcolors.WHITE}{bcolors.BOLD}================================")
print("")
print(f"{bcolors.FAIL}{bcolors.BOLD}>>-PREPARE FOR BATTLE!!-<<{bcolors.ENDC}")

print("")
while running:
    print(f"{bcolors.WHITE}{bcolors.BOLD}==================================")
    print("")
    print("NAME")
    for player in players:
        player.get_stats()
    print("")

    for enemy in enemies:
        enemy.get_enemy_stats()

    # Player attack phase
    for player in players:
        # Player choice of attack
        player.choose_action()
        print("")
        choice = input(bcolors.CYAN + "Choose Action:")
        index = int(choice) - 1

        print("")
        print(f"{bcolors.WHITE}{bcolors.BOLD}================================")

        if index == 0:
            damage = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(damage)

            # Display of regular attack damage
            print("")
            print(f"Attacked {enemies[enemy].name.replace('' ,'')}{bcolors.FAIL}{damage} of DMG{bcolors.ENDC}")

            print("")
            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has been slain")
                del enemies[enemy]

        # choice of spell options
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("\n" + "Choose Spell: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_damage = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(f"{bcolors.FAIL}{bcolors.BOLD}Not enough MP{bcolors.ENDC}")
                continue

            player.reduce_mp(spell.cost)

            # White and Black magic
            if spell.charm == "white":
                player.heal(magic_damage)
                print(f"{bcolors.OKGREEN}\n{spell.name} {player.name} Healed {magic_damage} HP{bcolors.ENDC}")

            elif spell.charm == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_damage)

                print(f"{bcolors.OKBLUE}\n{spell.name} Deals {magic_damage} Damage to {enemies[enemy].name.replace(' ', '')}{bcolors.ENDC}")

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has been slain")
                    del enemies[enemy]

        # Item choices for player to use
        elif index == 2:
            player.choose_item()

            print("")
            item_choice = int(input("Choose Item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            # Display of item choices with amount and message of no items left
            if player.items[item_choice]["amount"] == 0:
                print(bcolors.FAIL + '\n' + "No " + item.name + " left..." + bcolors.ENDC)
                continue
            # Prompt of item selection
            player.items[item_choice]["amount"] -= 1
            print("Selected Item: " + item.name)

            # Recovery Items
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
            # Attack Items
            elif isinstance(item, Item) and item.category == "attack":

                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                # Damage message to enemy
                print(player.name + "Used " + item.name + " Deals", bcolors.FAIL + str(item.prop), "Damage" + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has been slain.")
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
        enemy_choice = random.randrange(0, 2)

        # Choice of attack
        if enemy_choice == 0:
            target = random.randrange(0, 3)
            enemy_damage = enemy.generate_damage()

            players[target].take_damage(enemy_damage)
            print(f"\n{bcolors.FAIL}{enemy.name.replace(' ', '')} Attacked {str(enemy_damage)} Of Damage to {players[target].name.replace(' ', '')}{bcolors.ENDC}")

        # Choice of magic spells for enemy
        elif enemy_choice == 1:
            spell, magic_damage = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            # Recovery and attack spells for enemy
            if spell.charm == "white":
                enemy.heal(magic_damage)
                print("\n" + bcolors.FAIL + enemy.name.replace(" ", "") + " Used " + bcolors.OKGREEN + spell.name + " Healed", str(magic_damage), "HP" + bcolors.ENDC)
            elif spell.charm == "black":

                target = random.randrange(0, 3)
                players[target].take_damage(magic_damage)

                print(bcolors.FAIL + enemy.name.replace(" ", "") + " Used " + bcolors.OKBLUE + spell.name + bcolors.ENDC + " Deals", bcolors.FAIL + str(magic_damage), "Damage to " + players[target].name.replace(" ", "") + bcolors.ENDC)

print(f"{bcolors.FAIL}{enemy.name.replace(' ', '')} Used {bcolors.OKBLUE}{spell.name}{bcolors.ENDC} Deals "
      f"{bcolors.FAIL}{str(magic_damage)} Damage to {players[target].name.replace(' ', '')}{bcolors.ENDC}")


                if players[target].get_hp() == 0:
                    print(f"{players[target].name.replace(' ', '')} has been slain.")
                    del players[player]