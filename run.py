from classes.game import Person, bcolors




# Black Magic
magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 40}]
# White Magic




# python code goes here
player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)


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
        magic_choice = int(input("Choose Magic")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)


        current_mp = player.get_mp()


        if cost > current_mp:
            print(bcolors.FAIL + "\nNot Enough MP\n" + bcolors.ENDC)
            continue
       
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "of damage" + bcolors.ENDC)




    enemy_choice = 1


    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy Attacked", enemy_dmg)


    print("----------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")


    print("Player HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")
    print("Player MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")


    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Won!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your party has been defeated!" + bcolors.ENDC)
        running = False
   



