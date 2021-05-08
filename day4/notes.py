import random

random_integer = random.randint(1, 10)
print(random_integer)

# Generate a random decimal number between 0 and 5
random_float = random.random() * 5
print(random_float)

# Coding exercise: Random exercise (Heads or Tails)
coin = random.randint(0, 1)
if coin == 1:
    print("Heads")
else:
    print("Tails")


# Python list
states_of_america = ["Delaware", "Pennsylvania", "sfsffsfs", "sfsfsdf"]

# Using a negative index will start counting at the end of the list
print(states_of_america[-1])

# Adding a single item to the end of the list using append()
states_of_america.append("Angelaland")

print(states_of_america[-1])

# Coding exercise: Banker Roulette
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_choice = random.randint(0, len(names)-1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to by the meal today.")

# Nested list
fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

# Coding exercise: Treasure Map
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

treasure_map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
col = int(position[0]) - 1
row = int(position[1]) - 1
treasure_map[row][col] = "X"
print(f"{row1}\n{row2}\n{row3}")
