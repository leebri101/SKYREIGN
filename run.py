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
kunai = Item("Kunai", "attack", "Deals 100 DMG", 100)
grenade = Item("Grenade", "attack", "Deals 200 DMG", 200)
holy_grenade = Item("Holy-Grenade", "attack", "Deals 500 DMG", 500)

# Characters stats and items
player_spells = [fire, thunder, blizzard, meteor, comet, cure, cura, curaga]
boss_spells = [flame, shadow, void, darkness, cure, cura]
enemy_spells = [flame, thrash, cure]
player_items = [{"item": potion, "sum": 15},
                {"item": hi_potion, "sum": 10},
                {"item": super_potion, "sum": 5},
                {"item": ether, "sum": 10},
                {"item": elixir, "sum": 5},
                {"item": hi_elixir, "sum": 2},
                {"item": kunai, "sum": 15},
                {"item": grenade, "sum": 10},
                {"item": holy_grenade, "sum": 5}]
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
        print("Please enter in a number between 1-3")
        choice = int(input(f"{bcolors.CYAN}  Choose Action:"))
        # check if choice is in one of the options
        if choice != 1 and choice != 2 and choice != 3:
            print("Inavlid input please select between 1-3")
        else:
            break

        # Check if all conditions are met
        if type(choice) != int:
            break
        else:
            print("Please select and option")

        print("")
        print(f"{bcolors.WHITE}{bcolors.BOLD}================================")

        if index == 0:
            dmg = player.generate_dmg()
            enemy = player.choose_target(enemies)

            if enemy < len(enemies):
                enemies[enemy].take_dmg(dmg)

            # Display of regular attack damage
            print("")
            print(f"Attacked {enemies[enemy].name.replace('' ,'')}{bcolors.FAIL}{dmg} of DMG{bcolors.ENDC}")

            print("")
            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " died")

        # choice of spell options
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("\n" + "Choose Spell: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_dmg()

            mp_now = player.get_mp()

            if spell.cost > mp_now:
                print(f"{bcolors.FAIL}No MP left{bcolors.ENDC}")
                continue

            player.reduce_mp(spell.cost)

            # White and Black magic
            if spell.charm == "white":
                player.heal(magic_dmg)
                print(f"{bcolors.GREEN}\n{spell.name}{player.name} Heals {magic_dmg} HP{bcolors.ENDC}")

            elif spell.charm == "black":
                while True:
                    enemy = player.choose_target(enemies)

                    if enemy < len(enemies):
                        enemies[enemy].take_dmg(magic_dmg)
                        print(f"{bcolors.OKBLUE}\n{spell.name} Damages {magic_dmg} to {enemies[enemy].name.replace(' ', '')}{bcolors.ENDC}")

                        if enemies[enemy].get_hp() == 0:
                            print(enemies[enemy].name.replace(" ", "") + " died")

        # Item choices for player to use
        elif index == 2:
            player.choose_item()

            print("")
            item_choice = int(input("Choose Item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            # Display of item choices with amount and message of no items left
            if player.items[item_choice]["sum"] == 0:
                print(f"{bcolors.FAIL}\n No {item.name} left {bcolors.ENDC}")
                continue
            # Prompt of item selection
            player.items[item_choice]["sum"] -= 1
            print("Selected Item: " + item.name)

            # Recovery Items
            if isinstance(item, Item) and item.category == "potion":
                player.heal(item.prop)
                print(f"{bcolors.GREEN}\n{item.name} Healed {str(item.prop)} HP{bcolors.ENDC}")

            elif isinstance(item, Item) and item.category == "ether":
                player.restore_mp(item.prop)
                print(f"{bcolors.OKBLUE}\n{item.name} Restored {str(item.prop)} MP{bcolors.ENDC}")
            elif isinstance(item, Item) and item.category == "elixir":

                if item.name == "Hi-Elixir":
                    for i in players:
                        i.hp = player.maxhp
                        i.mp = player.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(f"{bcolors.MAGENTA}\n{item.name} fully restores HP/MP {str(item.prop)}{bcolors.ENDC}")

            # Attack Items
            elif isinstance(item, Item) and item.category == "attack":
                while True:
                    enemy = player.choose_target(enemies)
                    if enemy < len(enemies):
                        enemies[enemy].take_dmg(item.prop)

                        # Damage message to enemy
                        print(f"{player.name} Used {item.name} Deals {bcolors.FAIL}{str(item.prop)} Damage{bcolors.ENDC}")

                        if enemies[enemy].get_hp() == 0:
                            print(enemies[enemy].name.replace(" ", "") + " died")

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
        print(bcolors.GREEN + "You Won!" + bcolors.ENDC)
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
            enemy_dmg = enemy.generate_dmg()

            players[target].take_dmg(enemy_dmg)
            print(f"\n{bcolors.FAIL}{enemy.name.replace(' ', '')} Attacked {str(enemy_dmg)} Damage to {players[target].name.replace(' ', '')}{bcolors.ENDC}")

        # Choice of magic spells for enemy
        elif enemy_choice == 1:
            spell_info = enemy.choose_enemy_spell()
            if spell_info:
                spell, magic_dmg = enemy.choose_enemy_spell()
                enemy.reduce_mp(spell.cost)
                # Recovery and attack spells for enemy
                if spell.charm == "white":
                    enemy.heal(magic_dmg)
                    print(f"\n{bcolors.FAIL}{enemy.name.replace(' ', '')} Used {bcolors.ENDC}")
                    print(f"\n{bcolors.GREEN}{spell.name} Healed {str(magic_dmg)} HP{bcolors.ENDC}")
                elif spell.charm == "black":
                    target = random.randrange(0, 3)
                    players[target].take_dmg(magic_dmg)
                    print(f"{bcolors.FAIL}{enemy.name.replace(' ', '')} Used {spell.name} Deals {str(magic_dmg)} Damage to {players[target].name.replace(' ', '')}{bcolors.ENDC}")

                    if players[target].get_hp() == 0:
                        print(players[target].name.replace(" ", "") + " died")
                        del players[target]
            else:
                print(f"{bcolors.FAIL}{enemy.name.replace(' ', '')} didn't choose spell{bcolors.ENDC}")
