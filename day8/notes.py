import math
# Function that allows for input
# Parameter is the name of the value getting passed into the function, eg: name
# Argument is the actual value of the data, eg: "Diego"


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")
    print("How's the weather today?")


greet_with_name("Diego")

# Function with more than 1 input


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# It is using positional arguments
greet_with("Diego", "Canada")


# Now using keyword arguments
greet_with(name="Diego", location="Canada")

# Coding exercise: Paint Area Calculator


def paint_calc(height, width, cover):
    area = height * width
    number_cans = math.ceil(area / cover)
    print(f"You'll need {number_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)

# Coding exercise: Prime Number Checker
# Prime number: can only be divided by 1 and itself


def prime_checker(number):
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
