import random

# Day 4 Project: Rock Paper Scissors

choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

computer_choice = random.randint(0, 2)

print(f"Computer chose {computer_choice}")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if choice == 0:
    if computer_choice == 0:
        print("It's a draw")
    elif computer_choice == 1:
        print("You Lose")
    else:
        print("You Win!")
elif choice == 1:
    if computer_choice == 0:
        print("You Win!")
    elif computer_choice == 1:
        print("It's a draw")
    else:
        print("You Lose")
else:
    if computer_choice == 0:
        print("You Lose")
    elif computer_choice == 1:
        print("You Win!")
    else:
        print("It's a draw")
