# Guess the Number
# ------------------
# concept: Use Control Structures,random library, exception handling, functions, loops, and conditional statements
# ------------------
# pesudo code
# 1. import random library
# 2. define a function to generate a random number
# 4. define a function to check if the number is too high or too low
# 5. define a function to check if the number is out of range
# 6. Loop through the program until the user gets the correct number
# 7. Ask the user if they want to play again
# 8. If yes, loop through the program again
# ------------------

import random
import time


def generate_random_number() -> int:
    """
    This function generates a random number between 1 and 10
    """
    return random.randint(1, 10)


def check_number(num: int, randNum: int) -> str:
    """
    This function checks if the number is correct, out of range, too high or too low
    """
    if num > 10 or num < 1:
        return "out of range"
    elif num > randNum:
        return "too high"
    elif num < randNum:
        return "too low"
    else:
        return "correct"


def take_input() -> int:
    """
    This function takes the input from the user
    """
    while True:
        try:
            num = int(input("Please enter a number between 1 and 10\n"))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")


def guess_the_number():
    play_again = "y"
    print("===Welcome to Guess the Number===\n")
    while play_again == "y":
        time.sleep(0.5)
        randNum = generate_random_number()

        while True:
            num = take_input()

            print("Checking the number...\n")
            result = check_number(num, randNum)
            time.sleep(1)

            if result == "correct":
                print("You guessed the number correctly\n")
                time.sleep(0.5)
                play_again_input = ""
                while play_again_input not in ["y", "n"]:
                    play_again_input = input("Do you want to play again? (y/n)").lower()
                play_again = play_again_input
                break
            else:
                print(f"The number is {result}, try again\n")


guess_the_number()
