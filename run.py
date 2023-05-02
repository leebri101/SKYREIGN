from classes.game import person, bcolors
from classes.magic import spell
from classes.invetory import item

# Black Magic
fire = spell("Fire:", 10, 100, "black")
thunder = spell("Thunder:", 15, 150, "black")
blizzard = spell("Blizzard:", 5, 50, "black")
meteor = spell("Meteor:", 20, 200, "black")


# White Magic
cure = spell("Cure:", 5, 50, "white")
cura = spell("Cura:", 10, 100, "white")
curaga = spell("Curaga:", 15, 150, "white")

# Items
potion = item("Potion", "potion", "Heals 50 HP", 50)
hipotion = item("HI-Potion", "potion", "Heals 100 HP", 100)
superpotion = item("Super-Potion", "potion", "Heals 150 HP", 150)
elixir = item("Elixir", "elixir", "Restores HP/MP of one party member", 500)
hielixir = item("HI-Elixir", "elixir", "Fully restores HP/MP of all members", 9999)

dagger = item("Dagger", "attack", "Deals Damage of 250", 250)
dagger = item("Dagger", "attack", "Deals Damage of 250", 250)



# Python code goes here
player = person(5460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura, curaga])
enemy = person(1200, 65, 45, 25, [])

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
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(bcolors.OKBLUE + bcolors.BOLD + "You attacked", dmg, "Points of DMG.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input()) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + bcolors.BOLD + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.charm == "white":
            player.heal(magic_dmg)
            print(bcolors.OKGREEN + "\n" + spell.name + " healed", str(magic_dmg), "HP" + bcolors.ENDC)
        elif spell.charm == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "damage" + bcolors.ENDC)
        
    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(bcolors.FAIL + bcolors.BOLD + "Enemy Attacked", enemy_dmg)


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