

from math import isclose
import random
from game_data import data
from art import vs, logo


def get_random_choice():
    dictionary_item = {}
    random_index = random.randint(0, len(data) - 1)
    dictionary_item = data[random_index]
    return dictionary_item


def check_guess(a, b):
    followers_a = a['follower_count']
    followers_b = b['follower_count']

    return followers_a > followers_b


def play_game():
    is_correct = True
    score = 0
    choice_a = get_random_choice()
    choice_b = get_random_choice()

    while is_correct:

        print(logo)

        while choice_a == choice_b:
            choice_b = get_random_choice()

        print(
            f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")

        print(vs)

        print(
            f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

        print(
            f"Psssst, hint: A has {choice_a['follower_count']} M followers, B has {choice_b['follower_count']} M followers.")

        user_guess = input(
            "Who has more followers? Type 'A' or 'B': ").capitalize()

        if user_guess == "A":
            is_correct = check_guess(choice_a, choice_b)
        else:
            is_correct = check_guess(choice_b, choice_a)
            if is_correct:
                choice_a = choice_b

        if is_correct:
            score += 1
            choice_b = get_random_choice()
            print("\n\n")
            print(f"You are right! Current score: {score}.")

        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")


continue_playing = True

while continue_playing:
    play_game()

    ans = input("Do you want to play again? Type 'Y' or 'N'. ").capitalize()

    if ans == "N":
        continue_playing = False
