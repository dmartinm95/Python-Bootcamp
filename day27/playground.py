from tkinter.constants import N


def add(*args):
    # Many positional Arguments

    sum = 0
    for number in args:
        sum += number

    return sum


def calculate(n, **kwargs):
    # Many Keyword Arguments
    # kwargs is a dictionary with key being the name of the argument and the value is the value of the argument
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # Lets us look through all the inputs and find a specific one to do something
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
