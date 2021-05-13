# Python dictionaries
programming_dictionary = {
    "Bug": "An error in a program that prevents the prgoram from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrive an item from a dictionary
# print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Creating an empty dictionary or wiping an existing dictionary
empty_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary
# for student in programming_dictionary:
#     print(student)
#     print(programming_dictionary[student])

# Coding exercise: Grading Program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[student] = "Acceptable"
    elif score <= 70:
        student_grades[student] = "Fail"

# print(student_grades)

# Nesting Lists and Dictionaries
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 22},
}

# Nesting a Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 22
    },
]

# Coding exercise: Dictionary in List


def add_new_country(country, times_visited, cities_visited):
    new_log_entry = {}
    new_log_entry["country"] = country
    new_log_entry["cities_visited"] = cities_visited
    new_log_entry["total_visits"] = times_visited

    travel_log.append(new_log_entry)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
