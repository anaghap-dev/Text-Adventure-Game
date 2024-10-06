import time


def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)


def intro():
    print_pause(
        "You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked dragon is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty (but not very effective) dagger.\n")
    field()


def house():
    print_pause("\nYou approach the door of the house.")
    print_pause(
        "You are about to knock when the door opens and out steps a dragon.")
    print_pause("Eep! This is the dragon's house!")
    print_pause("The dragon attacks you!\n")
    choice_fight_or_flee()


def cave():
    print_pause("\nYou peer cautiously into the cave.")
    print_pause("It turns out to be a small, dark cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and take the sword with you.")
    print_pause("You walk back out to the field.\n")
    field()


def field():
    print("Enter 1 to knock on the door of the house.")
    print("Enter 2 to peer into the cave.")
    print("What would you like to do?")
    choice = input("(Please enter 1 or 2): ")
    if choice == '1':
        house()
    elif choice == '2':
        cave()
    else:
        field()


def choice_fight_or_flee():
    choice = input("Would you like to (1) fight or (2) run away? ")
    if choice == '1':
        fight()
    elif choice == '2':
        print_pause(
            "\nYou run back into the field. Luckily, you don't seem to have been followed.\n")
        field()
    else:
        choice_fight_or_flee()


def fight():
    print_pause("\nYou do your best...")
    print_pause("but your dagger is no match for the dragon.")
    print_pause("You have been defeated!")
    play_again()


def play_again():
    choice = input("Would you like to play again? (y/n) ")
    if choice == 'y':
        print_pause("\n\nRestarting the game...\n")
        start_game()
    elif choice == 'n':
        print("Thanks for playing! Goodbye!")
    else:
        play_again()


def start_game():
    print("\n-------------------------------------------------------------------------------------------------------")
    print("                                          Text Adventure Game")
    print("-------------------------------------------------------------------------------------------------------")
    intro()


start_game()
