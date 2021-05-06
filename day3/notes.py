def main():
    # Conditional statements
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))
    bill = 0

    if height > 120:
        print("You can ride the rollercoaster!")
        age = int(input("What is your age? "))
        if age < 12:
            bill = 5
            print("Child tickets are $5.")
        elif age <= 18:
            bill = 7
            print("Youth tickets are $7.")
        elif 45 <= age <= 55:
            print("Have a free ride on us!")
        else:
            bill = 12
            print("Adult tickets are $12.")

        wants_photo = input("Do you want a photo taken? Y or N. ")

        if wants_photo == "Y":
            bill += 3

        print(f"Your final bill is ${bill}.")

    else:
        print("Sorry you can't ride yet!")

    # Code exercise: Odd or even exercise
    number = int(input("Which number do you want to check? "))

    if number % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")

    # Code exercise: BMI 2.0
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))

    bmi = round(weight / height ** 2)

    if bmi < 18.5:
        print(f"Your bmi is {bmi}, you are underweight")
    elif bmi < 25:
        print(f"Your bmi is {bmi}, you have a normal weight")
    elif bmi < 30:
        print(f"Your bmi is {bmi}, you are overweight")
    elif bmi < 35:
        print(f"Your bmi is {bmi}, you are obese")
    else:
        print(f"Your bmi is {bmi}, you are clinically obese")

    # Code exercise: Leap Year
    year = int(input("What year do you want to check? "))

    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    if leap:
        print("Leap year")
    else:
        print("Not leap year")

    # Code exercise: Pizza Order Practice
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, L. ")
    add_pepperoni = input("Do you want pepperoni? Y or N. ")
    extra_cheese = input("Do you want extra cheese? Y or N. ")

    bill = 0

    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20
    else:
        bill += 25

    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3

    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}.")

    # Code exercise: Love Calculator
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n").lower()
    name2 = input("What is their name? \n").lower()

    combine_name = name1 + name2

    true_count = combine_name.count(
        "t") + combine_name.count("r") + combine_name.count("u") + combine_name.count("e")
    love_count = combine_name.count(
        "l") + combine_name.count("o") + combine_name.count("v") + combine_name.count("e")

    love_score = str(true_count) + str(love_count)
    love_score = int(love_score)

    if love_score < 10 or love_score > 90:
        print(
            f"Your score is {love_score}, you go together like coke and mentos.")
    elif 40 <= love_score <= 50:
        print(f"Your score is {love_score}, you are alright together.")
    else:
        print(f"Your score is {love_score}.")


if __name__ == "__main__":
    main()
