"""
Number Guessing Game
Author: Prachi
"""

import random


def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("\nI'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        attempts += 1

        if guess < number:
            print("Too low!\n")
        elif guess > number:
            print("Too high!\n")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.\n")
            return

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Attempts left: {remaining}\n")

    print(f"Out of attempts! The number was {number}.\n")


def main():
    print("==== NUMBER GUESSING GAME ====")

    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
