import random

# List of words
words = ["python", "developer", "programme", "hangman", "computer", "car"]
word = random.choice(words)  # Pick a random word
guessed = set()  # Store guessed letters
lives = 5  # Number of attempts

while lives > 0:
    display = ''.join(letter if letter in guessed else '_' for letter in word)
    print(f"\nWord: {display}  |  Lives: {lives}  |  Guessed: {' '.join(guessed)}")

    if '_' not in display:
        print("\nCongrats! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").upper()

    if guess in guessed:
        print("You already guessed that letter!")
    elif guess in word:
        guessed.add(guess)
    else:
        guessed.add(guess)
        lives -= 1
        print("Wrong guess!")

if lives == 0:
    print("\nYou lost! The word was:", word)

