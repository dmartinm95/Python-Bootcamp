# Object Oriented Programming
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu_items = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

continue_program = True

while continue_program:
    user_input = input(f"What would you like? {menu_items.get_items()}: ")
    item = menu_items.find_drink(user_input)
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        continue_program = False
    else:
        if coffee_maker.is_resource_sufficient(item):
            cost = item.cost
            if money_machine.make_payment(cost):
                coffee_maker.make_coffee(item)
