# Namespaces: Local vs Global scope
enemies = 1


def increase_enemies():
    # How to modify a global variable
    global enemies  # You don't want to do this often as it is confusing
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# There is no Block (If, While, For, etc) Scope in python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)


# Global constants (all uppercase)
PI = 3.14159
URL = "https://www.google.com"
