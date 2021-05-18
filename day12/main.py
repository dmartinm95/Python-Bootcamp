# Day 11 Project: The Number Guessing Game
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


import random
from art import logo


def check_guess(guess_number, correct_number, current_attempts):

    if guess_number < correct_number:
        print("Too low.")
    elif guess_number > correct_number:
        print("Too high.")
    else:
        print(f"You got it! The answer was {correct_number}.")
        return -1

    current_attempts -= 1

    return current_attempts


play_again = True


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    continue_game = True

    random_number = random.randint(1, 100)

    print(f"Pssst, the correct answer is {random_number}")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        number_attempts = 10
    else:
        number_attempts = 5

    while continue_game:
        print(
            f"You have {number_attempts} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        number_attempts = check_guess(
            guess_number=guess, correct_number=random_number, current_attempts=number_attempts)

        if number_attempts == 0:
            print("You've run out of guesses, you lose.")
            continue_game = False
        elif number_attempts == -1:
            continue_game = False


while play_again:
    game()
    again = input("Would you like to play again? 'Y' or 'N': ").upper()
    if again == "N":
        play_again = False
