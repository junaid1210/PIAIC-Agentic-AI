# Project-2-GuessTheNumber

import random  # Importing random module to generate a random number

def guess(x):
    random_number = random.randint(1, x)  # Machine  will pick a random number between 1 and x
    guess = 0  # Initialize guess variable

    while guess != random_number:  # Loop until the user guesses correctly
        guess = int(input(f"Guess a number between 1 and {x}: "))  # Take user input
        
        if guess < random_number:
            print("\n Guess Aagin, Your guess is low.\n")
        elif guess > random_number:
            print("\n Guess again. Your guess is high.\n")

    print(f"\n Congrats! You have guessed the number {random_number} correctly\n")

guess(20) # Call the function to start the game (range 1 to 20)

