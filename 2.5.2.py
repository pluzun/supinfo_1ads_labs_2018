from random import randint


def show_matches(matches_number):
    print("{} matches left!".format(matches_number))
    print("| " * matches_number)

def player_turn(matches_number):
    print("Player turn !")

    pick_number = int(input("Select a matches number to pick : "))
    while pick_number > 3:
        pick_number = int(input("Select a matches number to pick : "))

    print("You have picked {} matches!".format(pick_number))

    return matches_number - pick_number

def computer_turn(matches_number):
    print("Computer turn !")
    pick_number = randint(1, 3)
    print("Computer has picked {} matches!".format(pick_number))

    return matches_number - pick_number

def init():
    """
    Define the number of matches and which player starts.
    """
    matches_number = int(input("Select a matches number : "))
    while matches_number % 2 == 0:
        matches_number = int(input("You must choose a odd number of matches : "))

    turn = int(input("Which player starts ? (1: Human | 2: Robot) : "))
    while turn != 1 and turn != 2:
        turn = int(input("Which player starts ? (1: Human | 2: Robot) : "))

    return matches_number, turn

matches_number, turn = init()

playing = True
while playing:
    show_matches(matches_number)
    if turn == 1:
        matches_number = player_turn(matches_number)
        turn = 2
    else:
        matches_number = computer_turn(matches_number)
        turn = 1

    playing = True if matches_number >= 1 else False

print("Player {} win!".format(turn))
