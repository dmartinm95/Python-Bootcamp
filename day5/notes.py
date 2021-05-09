# Loops
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

# Coding exercise: Average Height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_heights = 0
number_students = 0

for height in student_heights:
    total_heights += height
    number_students += 1

average_height = total_heights / number_students

print(f"The average height in the class is: {round(average_height)}")

# Coding exercise: High Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = -1

for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")

# Using a loop independently of a list
total_sum = 0
for number in range(1, 101):
    total_sum += number

print(f"Adding every number between 1 and 100 is {total_sum}")

# Coding exercise: Adding Even Numbers
total_even_sum = 0
# Could also specify the stepsize within the range() method, as
# for number in range(2, 101, 2):
for number in range(1, 101):
    if number % 2 == 0:
        total_even_sum += number
print(total_even_sum)

# Coding exercise: FizzBuzz Job Interview Question
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzByzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
