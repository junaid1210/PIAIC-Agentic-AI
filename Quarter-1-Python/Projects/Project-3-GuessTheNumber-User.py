# Project 3

import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':  # Loop until the computer guesses correctly
        if low != high:
            guess = random.randint(low, high)  # Computer makes a random guess
        else:
            guess = low  # Only one number left

        # Asking for feedback from the user
        feedback = input(f"Is {guess} \n too high (h) \n too low (l) \n or correct (c)? ").lower()

        if feedback == 'h':
            high = guess - 1  # Adjust range if too high
        elif feedback == 'l':
            low = guess + 1  # Adjust range if too low

    print(f"\n Congrats! The computer guessed your number, {guess}, correctly! \n")

# Run the game
computer_guess(100)  # The user thinks of a number between 1 and 100

