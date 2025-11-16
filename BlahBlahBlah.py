# import ng os para sa clear terminal tas time para sa sleep
import os
import time

# pang animation o kung ano
def dagger_slash():
    print(" " * 10 + "          /¯¯¯/")
    time.sleep(0.2)
    print(" " * 10 + "         /   /")
    time.sleep(0.2)
    print(" " * 10 + "     /¯¯¯¯¯¯¯¯¯/")
    time.sleep(0.2)
    print(" " * 10 + "    /_________/")
    time.sleep(0.2)
    print(" " * 10 + "     /     /")
    time.sleep(0.2)
    print(" " * 10 + "    /     /")
    time.sleep(0.2)
    print(" " * 10 + "   /    /")
    time.sleep(0.2)
    print(" " * 10 + "  /   /")
    time.sleep(0.2)
    print(" " * 10 + " /  /")
    time.sleep(0.2)
    print(" " * 10 + "/_/")
    time.sleep(2)

def vampiric_claws():
    print(" " * 10 + "        /|   /|    /|")
    time.sleep(0.2)
    print(" " * 10 + "       / /  / /   / /")
    time.sleep(0.2)
    print(" " * 10 + "      / /  / /   / /")
    time.sleep(0.2)
    print(" " * 10 + "     //¯  //¯   //¯")
    time.sleep(0.2)
    print(" " * 10 + "    / /  / /   / /")
    time.sleep(0.2)
    print(" " * 10 + "   / /  /  /  / /")
    time.sleep(0.2)
    print(" " * 10 + "  //¯  //¯¯  //¯")
    time.sleep(0.2)
    print(" " * 10 + " / /  / /   / /")
    time.sleep(0.2)
    print(" " * 10 + "/ /  / /   / /")
    time.sleep(0.2)
    print(" " * 10 + "|/   |/    |/")
    time.sleep(2)

def bat_form():
    print(" " * 10 + "            /\\___/\\ ")
    time.sleep(0.2)
    print(" " * 10 + "___________(       )___________")
    time.sleep(0.2)
    print(" " * 10 + "\\                             /")
    time.sleep(0.2)
    print(" " * 10 + " \\__                       __/  ")
    time.sleep(0.2)
    print(" " * 10 + "    \\                     /")
    time.sleep(0.2)
    print(" " * 10 + "     \\__               __/")
    time.sleep(0.2)
    print(" " * 10 + "        \\             /")
    time.sleep(0.2)
    print(" " * 10 + "         \\____/¯\\____/")
    time.sleep(0.2)
    print(" " * 10 + "           ||     ||")
    time.sleep(0.2)
    print(" " * 10 + "           VV     VV")
    time.sleep(2)

def drain_life():
    print(" " * 10 + "             |¯|")
    time.sleep(0.2)
    print(" " * 10 + "     /\\   ___| |___")
    time.sleep(0.2)
    print(" " * 10 + "    /  \\ |___   ___|")
    time.sleep(0.2)
    print(" " * 10 + "   /    \\    | |")
    time.sleep(0.2)
    print(" " * 10 + "  /      \\   | |")
    time.sleep(0.2)
    print(" " * 10 + " /        \\  |_|")
    time.sleep(0.2)
    print(" " * 10 + "(          )")
    time.sleep(0.2)
    print(" " * 10 + "|          |")
    time.sleep(0.2)
    print(" " * 10 + " \\        /")
    time.sleep(0.2)
    print(" " * 10 + "  \\______/")
    time.sleep(2)

def do_nothing():
    print(" " * 10 + "    /¯¯¯¯\\ ")
    time.sleep(0.2)
    print(" " * 10 + "    \\    /")
    time.sleep(0.2)
    print(" " * 10 + " ___/`--`\\___")
    time.sleep(0.2)
    print(" " * 10 + "|            |")
    time.sleep(0.2)
    print(" " * 10 + "| |\\      /| |")
    time.sleep(0.2)
    print(" " * 10 + "|_| |    | |_|")
    time.sleep(0.2)
    print(" " * 10 + " O  |    |  O")
    time.sleep(0.2)
    print(" " * 10 + "    | /\\ |")
    time.sleep(0.2)
    print(" " * 10 + "   _| || |_")
    time.sleep(0.2)
    print(" " * 10 + "  (___||___)")
    time.sleep(2)

def restwell():
    print(" " * 10 + "              |¯¯¯¯¯¯/  ")
    time.sleep(0.2)
    print(" " * 10 + "               ¯¯/  /")
    time.sleep(0.2)
    print(" " * 10 + "                /  /__")
    time.sleep(0.2)
    print(" " * 10 + "               /______|")
    time.sleep(0.2)
    print(" " * 10 + "       |¯¯¯¯/")
    time.sleep(0.2)
    print(" " * 10 + "        ¯/ /_")
    time.sleep(0.2)
    print(" " * 10 + "        /____|")
    time.sleep(0.2)
    print(" " * 10 + "|¯¯¯¯/")
    time.sleep(0.2)
    print(" " * 10 + " ¯/ /_")
    time.sleep(0.2)
    print(" " * 10 + " /____|")
    time.sleep(2)

# function para makita player status
def stats(p1name, p1health, p1energy, p2name, p2health, p2energy):
    print("=" * 10 + "\nPlayer Status\n" + "-" * 10)
    print(f"Player 1 ({p1name})")
    print(f"Health: {p1health}\nEnergy: {p1energy}")
    print("-" * 10)
    print(f"Player 2 ({p2name})")
    print(f"Health: {p2health}\nEnergy: {p2energy}")
    print("=" * 10)

# function para makuha moves ng players
def moves(player, name, energy):
    print("\nAvailable Moves:")
    print("A. Dagger Slash (10 damage; energy: 6)")
    print("B. Vampiric Claws (40 damage; energy: 25)")
    print("C. Dodge: Bat Form (nullifies incoming attack; energy: 10)")
    print("D. Drain Life (deals 6 damage then heals self by 10; energy: 13)")
    print("E. Do nothing (energy: 0)\n")
    print("Players, what are your moves?")
    print("Please enter A, B, C, D, or E only")
    choices = ["A", "B", "C", "D", "E"]
    if energy == 0:
        print(f"Player {player} ({name}) has no more energy. Skipping this turn...")
        choice = "E"
        time.sleep(3)
    else:
        choice = input(f"Player {player} ({name}): ")
        while choice not in choices:
            print("Wrong Input. A, B, C, D, or E only.")
            choice = input(f"Player {player} ({name}): ")
    return choice

# function para sa battle phase, nagcacall out ng stats tas moves
def choosing_phase(p1name, p1health, p1energy, p2name, p2health, p2energy, turn):
    print("=" * 3 + f" Night {nights} " + "=" * 3)
    stats(p1name, p1health, p1energy, p2name, p2health, p2energy)
    if turn == 1:
        choice = moves(1, p1name, p1energy)
    else:
        choice = moves(2, p2name, p2energy)
    return choice

# function para makuha damage, cost, tas heal based sa choices
def moves_result(choice):
    match choice:
        case "A":
            dagger_slash()
            return 10, 6, 0
        case "B":
            vampiric_claws()
            return 40, 25, 0
        case "C":
            bat_form()
            return 0, 10, 0
        case "D":
            drain_life()
            return 6, 13, 10
        case "E":
            do_nothing()
            return 0, 0, 0
        
# function para makuha yung resulta ng battle phase, nagcall out ng moves_result
def move_effects(p1health, p1energy, p2health, p2energy, p1choice, p2choice):
    p1damage, p1cost, p1heal = moves_result(p1choice)
    os.system('cls')
    p2damage, p2cost, p2heal = moves_result(p2choice)
    os.system('cls')
    print("Move Effects: ")
    if p1choice == "C":
        p2damage, p2heal = 0, 0
    if p2choice == "C":
        p1damage, p1heal = 0, 0
    time.sleep(0.5)
    print(f"Player 1 ({p1name}) uses {p1cost} energy.")
    if p1heal > 0:
        time.sleep(0.5)
        print(f"Player 1 ({p1name}) heals for {p1heal} health.")
    time.sleep(0.5)
    print(f"Player 2 ({p2name}) received {p1damage} damage.")
    time.sleep(0.5)
    print(f"Player 2 ({p2name}) uses {p2cost} energy.")
    if p2heal > 0:
        time.sleep(0.5)
        print(f"Player 2 ({p2name}) heals for {p2heal} health.")
    time.sleep(0.5)
    print(f"Player 1 ({p1name}) received {p2damage} damage\n")
    time.sleep(5)
    p1health += p1heal - p2damage
    p2health += p2heal - p1damage
    p1energy -= p1cost
    if p1energy < 0:
        p1energy = 0
    p2energy -= p2cost
    if p2energy < 0:
        p2energy = 0
    return p1health, p1energy, p2health, p2energy

# function na kada 3 nights, magrerest
def rest(p1name, p1health, p1energy, p2name, p2health, p2energy):
    restwell()
    os.system('cls')
    print("3 nights have passed. Both vampire spawn shall rest")
    if p1energy == 0:
        print(f"Player 1 ({p1name}) is too tired, and can only rest partially...")
        time.sleep(0.5)
        print(f"Player 1 ({p1name}) heals for 20 and replenishes 13 energy.\n")
        time.sleep(0.5)
        p1health += 20
        p1energy += 13
    else:
        print(f"Player 1 ({p1name}) is able to have a complete rest.")
        time.sleep(0.5)
        print(f"Player 1 ({p1name}) heals for 25 and replenishes 20 energy.\n")
        time.sleep(0.5)
        p1health += 25
        p1energy += 20
    if p2energy == 0:
        print(f"Player 2 ({p2name}) is too tired, and can only rest partially...")
        time.sleep(0.5)
        print(f"Player 2 ({p2name}) heals for 20 and replenishes 13 energy.\n")
        time.sleep(0.5)
        p2health += 20
        p2energy += 13
    else:
        print(f"Player 2 ({p2name}) is able to have a complete rest.")
        time.sleep(0.5)
        print(f"Player 2 ({p2name}) heals for 25 and replenishes 20 energy.\n")
        time.sleep(0.5)
        p2health += 25
        p2energy += 20
    time.sleep(5)
    return p1health, p1energy, p2health, p2energy

# pinakamain program, tanong muna pangalan
print("Welcome Vampire Spawn!")
print("Fight for the right to ascend into a Vampire Lord")
print("Attempt to knock out your opponent.")
print("Use your vampiric moves to outsmart your opponent.")
print("Players, enter your names...\n")
p1name = input("Player 1: ")
p2name = input("Player 2: ")

# hangga't Y yung continue, edi ulet ulet
continue_game = "Y"
while continue_game == "Y":
    print(f"\nLet the duel between {p1name} and {p2name} begin!\n")
    time.sleep(2)
    os.system('cls')
    # initialize ng mga variables
    p1health, p1energy, p2health, p2energy = 100, 50, 100, 50
    nights = 1
    # ulet ulet hangga't wala pang deds
    while p1health > 0 and p2health > 0:
        p1choice = choosing_phase(p1name, p1health, p1energy, p2name, p2health, p2energy, 1)
        os.system('cls')
        p2choice = choosing_phase(p1name, p1health, p1energy, p2name, p2health, p2energy, 2)
        os.system('cls')
        p1health, p1energy, p2health, p2energy = move_effects(p1health, p1energy, p2health, p2energy, p1choice, p2choice)
        os.system('cls')
        # eto yung 3 nights
        if nights % 3 == 0 and p1health > 0 and p2health > 0:
            p1health, p1energy, p2health, p2energy = rest(p1name, p1health, p1energy, p2name, p2health, p2energy)
            os.system('cls')
        nights += 1
    # tignan sino deds tas sino ang mageevolve, o kung parehas ba deds
    stats(p1name, p1health, p1energy, p2name, p2health, p2energy)
    if p1health <= 0 and p2health <= 0:
        print("Draw! Nobody ascend to a Vampire Lord...")
    elif p1health <= 0:
        print(f"Player 2 ({p2name}) wins! Player 2 ascends to a Vampire Lord...")
    else:
        print(f"Player 1 ({p1name}) wins! Player 1 ascend to a Vampire Lord...")
    # extend lima sa pc 2
    print("\nWould you like to Play Again?")
    continue_game = input("Type (Y) to Play Again: ")





