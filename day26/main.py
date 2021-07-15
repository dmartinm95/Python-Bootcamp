# List comprehension and NATO alphabet

# Coding exercise: Squaring numbers
import pandas
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num*num for num in numbers]
print(squared_numbers)

# Coding exercise: Filtering even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Coding exercise: Data overlap
with open("day26\\file1.txt") as file1:
    file1_content = file1.readlines()
    file1_content = [int(entry.strip("\n")) for entry in file1_content]

with open("day26\\file2.txt") as file2:
    file2_content = file2.readlines()
    file2_content = [int(entry.strip("\n")) for entry in file2_content]

common_numbers = [entry for entry in file1_content if entry in file2_content]

# Coding exercise: Dictionary comprehension # 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_dict = {word: len(word) for word in sentence.split()}
print(words_dict)

# Coding exercise: Dictionary comprehension # 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: temperature_c * 9 / 5 +
             32 for (day, temperature_c) in weather_c.items()}
print(weather_f)

# Iterating over a Pandas DataFrame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

# NATO alphabet
nato_alphabet = pandas.read_csv("day26\\nato_phonetic_alphabet.csv")

nato_alphabet_dict = {row.letter: row.code for (
    _, row) in nato_alphabet.iterrows()}

print(nato_alphabet_dict)


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_code_words = [nato_alphabet_dict[letter]
                               for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_code_words)


generate_phonetic()
