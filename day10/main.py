# Day 10 Project: Calculator
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    calculate_another = True

    while calculate_another:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        function = operations[operation_symbol]

        answer = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if choice == 'n':
            calculate_another = False
            calculator()
        else:
            num1 = answer


calculator()
