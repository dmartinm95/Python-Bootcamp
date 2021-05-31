# Day 15 Project: Coffee Machine Program
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}


# 1. Print report
# 2. Check resources sufficient
# 3. Process coins
# 4. Check transaction successful
# 5. Make Coffee

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

    return total_amount


def process_order(user_input, pay_amount):
    cost = MENU[user_input]['cost']
    if pay_amount < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change_back = pay_amount - cost
        resources['money'] += round(cost, 2)
        if change_back > 0:
            print(f"Here is ${round(change_back, 2)} in change.")

        return True


def check_enough_materials(user_input):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']

    ingredients_required_dict = MENU[user_input]['ingredients']

    for key in ingredients_required_dict:
        amount_needed = ingredients_required_dict[key]
        if key == 'water':
            water_remaining = water - amount_needed
            if water_remaining < 0:
                print(f"Sorry there is not enough water.")
                return False
        elif key == 'milk':
            milk_remaining = milk - amount_needed
            if milk_remaining < 0:
                print(f"Sorry there is not enough milk.")
                return False
        else:
            coffee_remaining = coffee - amount_needed
            if coffee_remaining < 0:
                print(f"Sorry there is not enough coffee.")
                return False

    return True


def consume_resources(user_input):
    ingredients_required_dict = MENU[user_input]['ingredients']

    for key in ingredients_required_dict:
        if key == "water":
            resources['water'] -= ingredients_required_dict[key]
        elif key == "milk":
            resources['milk'] -= ingredients_required_dict[key]
        else:
            resources['coffee'] -= ingredients_required_dict[key]


continue_program = True

while continue_program:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        continue_program = False
    elif user_input == "report":
        print_report()
    else:
        if check_enough_materials(user_input):
            payment = process_coins()
            if(process_order(user_input, payment)):
                consume_resources(user_input)
                print(f"Here is your {user_input} ☕ Enjoy!")
