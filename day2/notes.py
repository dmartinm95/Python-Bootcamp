# Primitive data types

def main():
    # Subscripting: Get the first character of a string or at any index starting from 0
    print("Hello"[0])

    # Integer
    print(123 + 245)

    # Using underscore is only to make the large number more readable.
    # The number would be stripped down to 734529.678
    print(734_529.678)

    # Float
    print(1.23)

    # Boolean
    print(True)

    # Coding exercise: Sum the digits of a 2-digit number
    two_digit_number = input("Type a two digit number: ")
    print(type(two_digit_number))
    first_digit = int(two_digit_number[0])
    second_digit = int(two_digit_number[1])
    result = first_digit + second_digit
    print(result)

    # Mathematical operations
    # 3 + 5: addition
    # 7 - 4: subtraction
    # 3 * 2: multiplication
    # 10 / 5: division
    # 2 ** 3: exponent 2*2*2

    # Order of priority: PEMDAS
    # Parenthesis
    # Exponents
    # Multiplication
    # Division
    # Addition
    # Substraction

    print((3 * 3 + 3 / 3 - 3) - 4)

    # Coding exercise: BMI Calculator
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")

    height = float(height)
    weight = float(weight)

    bmi = weight / height**2

    print(int(bmi))

    # Round numbers and specify the number of decimal spaces
    print(round(8/3, 2))

    # Floor division using '//', rounds down
    print(8 // 3)

    # f-strings, used to incorporate different data types into a string
    score = 0
    height = 1.7
    is_winning = True
    print(
        f"Your score is {score} and your height is {height} and you are winning is {is_winning}")

    # Coding exercise: Life in Weeks
    age = input("What is your current age? ")

    age = int(age)
    final_age = 90
    years_left = final_age - age
    months_left = years_left * 12   # 12 months in a year
    weeks_left = years_left * 52    # 52 weeks in a year
    days_left = years_left * 365    # 365 days in a year

    message = f"You have {days_left} days, {weeks_left} weeks and {months_left} months left"
    print(message)


if __name__ == "__main__":
    main()
