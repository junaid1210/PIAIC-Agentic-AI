# Project 4

import random  # Importing random module

def play():
    user = input("Enter \n 'r' for Rock \n 'p' for Paper \n 's' for Scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])  # Computer randomly selects

    print(f"Computer chose: {computer}")

    if user == computer:
        return " \n Its a tie"

    if is_win(user, computer):
        return " \n You won"

    return " \n You lost"

def is_win(player, opponent):
    # Winning conditions: Rock beats Scissors, Scissors beats Paper, Paper beats Rock
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

# Run the game
print(play())

