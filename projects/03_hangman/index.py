# Concept: a classic word game where the user
# has to guess a secret word letter by letter.
# The user has a limited number of wrong guesses
# before the hangman is drawn and the game is over.
# --------------------------------------
# Pesudo code:
# --------------------------------------
# 1. Create a list of words
# 2. Pick a random word from the list
# 3. Create an empty list for the guessed letters
# 4. Create a variable for the number of wrong guesses
# 5. Create a variable for the hangman
# 6. Create a variable for the game status
# 7. Create a while loop for the game status
# 8. Create a for loop for the hangman
# 9. Create a function to check if the user has won

import random
import time


def play_hangman():
    words: list[str] = ["sea", "cloud", "ai", "iot", "blockchain"]
    word: str = random.choice(words)
    guessed_letters: list[str] = []
    wrong_guesses: int = 0
    hangman: list[str] = [
        "  +---+  ",
        "  |   |  ",
        "      |  ",
        "      |  ",
        "      |  ",
        "      |  ",
        "=========",
    ]
    game_over: bool = False

    while not game_over:
        print(
            " ".join([letter if letter in guessed_letters else "_" for letter in word])
        )
        guess = input("Guess a letter: ").lower()
        if guess not in guessed_letters:
            guessed_letters.append(guess)
        if guess not in word:
            wrong_guesses += 1
            print("\n".join(hangman[:wrong_guesses]))
        if wrong_guesses == len(hangman):
            print("You lost! The word was " + word)
            game_over = True
        elif set(word) == set(guessed_letters):
            print("You won! The word was " + word)
            game_over = True
