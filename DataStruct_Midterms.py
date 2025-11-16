# function para sa pagdisplay ng player status
def stats(player, name, health, energy):
    print(f"Player {player} ({name})")
    print(f"Health: {health}\nEnergy: {energy}")

# function para sa pagreturn ng damage cost tas heal
def moves(choice):
    match choice:
        case "A":
            return 10, 6, 0
        case "B":
            return 40, 25, 0
        case "C":
            return 0, 10, 0
        case "D":
            return 6, 13, 10
        case "E":
            return 0, 0, 0

# main tas nagkuha ng pangalan ng players
print("Welcome Vampire Spawn!")
print("Fight for the right to ascend into a Vampire Lord")
print("Attempt to knock out your opponent.")
print("Use your vampiric moves to outsmart your opponent.")
print("Players, enter your names...\n")
p1name = input("Player 1: ")
p2name = input("Player 2: ")

# magloop kapag Y paren yung continue
continue_game = "Y"
while continue_game == "Y":
    print(f"\nLet the duel between {p1name} and {p2name} begin!\n")
    p1health, p1energy, p2health, p2energy = 100, 50, 100, 50
    nights = 1
    # magloop hangga't may buhay pa yung dalawang players
    while p1health > 0 and p2health > 0:
        print("=" * 3 + f" Night {nights} " + "=" * 3)
        print("=" * 10 + "\nPlayer Status\n" + "-" * 10)
        stats(1, p1name, p1health, p1energy)
        print("-" * 10)
        stats(2, p2name, p2health, p2energy)
        print("=" * 10)
        print("\nAvailable Moves:")
        print("A. Dagger Slash (10 damage; energy: 6)")
        print("B. Vampiric Claws (40 damage; energy: 25)")
        print("C. Dodge: Bat Form (nullifies incoming attack; energy: 10)")
        print("D. Drain Life (deals 6 damage then heals self by 10; energy: 13)")
        print("E. Do nothing (energy: 0)\n")
        print("Players, what are your moves?")
        print("Please enter A, B, C, D, or E only")
        choices = ["A", "B", "C", "D", "E"]
        p1choice, p2choice = "", ""
        # pangkuha ng choice, kapag walang energy edi automatic na E
        # pero kapag meron, kukuha ng input
        if p1energy == 0:
            print(f"Player 1 ({p1name}) has no more energy. Skipping this turn...")
            p1choice = "E"
        else:
            p1choice = input(f"Player 1 ({p1name}): ")
            while p1choice not in choices:
                print("Wrong Input. A, B, C, D, or E only.")
                p1choice = input(f"Player 1 ({p1name}): ")
        if p2energy == 0:
            print(f"Player 2 ({p2name}) has no more energy. Skipping this turn...")
            p2choice = "E"
        else:
            p2choice = input(f"Player 2 ({p2name}): ")
            while p2choice not in choices:
                print("Wrong Input. A, B, C, D, or E only.")
                p2choice = input(f"Player 2 ({p2name}): ")
        print("\nMove Effects: ")
        # call out yung moves na function para sa damage, etc.
        p1damage, p1cost, p1heal = moves(p1choice) 
        p2damage, p2cost, p2heal = moves(p2choice)
        # kapag may nagdodge, magiging 0 yung damage tas heal ng kalaban
        if p1choice == "C":
            p2damage, p2heal = 0, 0
        if p2choice == "C":
            p1damage, p1heal = 0, 0
        print(f"Player 1 ({p1name}) uses {p1cost} energy.")
        if p1heal > 0:
            print(f"Player 1 ({p1name}) heals for {p1heal} health.")
        print(f"Player 2 ({p2name}) received {p1damage} damage.")
        print(f"Player 2 ({p2name}) uses {p2cost} energy.")
        if p2heal > 0:
            print(f"Player 2 ({p2name}) heals for {p2heal} health.")
        print(f"Player 1 ({p1name}) received {p2damage} damage\n")
        # computation ng result
        p1health += p1heal - p2damage
        p2health += p2heal - p1damage
        # kapag nagnegative, magiging 0
        p1energy -= p1cost
        if p1energy < 0:
            p1energy = 0
        p2energy -= p2cost
        if p2energy < 0:
            p2energy = 0
        # kada 3 nights, may rest
        if nights % 3 == 0 and p1health > 0 and p2health > 0:
            print("3 nights have passed. Both vampire spawn shall rest")
            if p1energy == 0:
                print(f"Player 1 ({p1name}) is too tired, and can only rest partially...")
                print(f"Player 1 ({p1name}) heals for 20 and replenishes 13 energy.\n")
                p1health += 20
                p1energy += 13
            else:
                print(f"Player 1 ({p1name}) is able to have a complete rest.")
                print(f"Player 1 ({p1name}) heals for 25 and replenishes 20 energy.\n")
                p1health += 25
                p1energy += 20
            if p2energy == 0:
                print(f"Player 2 ({p2name}) is too tired, and can only rest partially...")
                print(f"Player 2 ({p2name}) heals for 20 and replenishes 13 energy.\n")
                p2health += 20
                p2energy += 13
            else:
                print(f"Player 2 ({p2name}) is able to have a complete rest.")
                print(f"Player 2 ({p2name}) heals for 25 and replenishes 20 energy.\n")
                p2health += 25
                p2energy += 20
        nights += 1
    # para malaman sino panalo
    print("=" * 10 + "\nPlayer Status\n" + "-" * 10)
    stats(1, p1name, p1health, p1energy)
    print("-" * 10)
    stats(2, p2name, p2health, p2energy)
    print("=" * 10)
    if p1health <= 0 and p2health <= 0:
        print("Draw! Nobody ascend to a Vampire Lord...")
    elif p1health <= 0:
        print(f"Player 2 ({p2name}) wins! Player 2 ascends to a Vampire Lord...")
    else:
        print(f"Player 1 ({p1name}) wins! Player 1 ascend to a Vampire Lord...")
    print("\nWould you like to Play Again?")
    continue_game = input("Type (Y) to Play Again: ")