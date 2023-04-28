from classes.game import person, bcolors
from classes.magic import spell

# Black Magic
fire = spell("Fire", "MP:", 10,   100)
thunder = spell("Thunder", "cost:", 15, 150)
blizzard = spell("Blizzard", "cost:", 5, 50)
meteor = spell("Fire", "cost:", 20, 200,)

# White Magic
cure = spell("cure", 5, 50, "white")
cura = spell("cura", 10, 100, "white")
curaga = spell("curaga", 15, 150, "white")


# Python code goes here
player = person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura, curaga])
enemy = person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "Enemy Attack!!!" + bcolors.ENDC)

while running:
    print("======================")
    player.choose_action()
    choice = input("Choose Action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked", dmg, "Points of DMG.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic:")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot Enough MP\n" + bcolors.ENDC)
            continue
       
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "damage" + bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy Attacked", enemy_dmg)


    print("======================")
    print("Player HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")
    
    print("Player MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")
    
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")


    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Won!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your party has been defeated!" + bcolors.ENDC)
        running = False
   



