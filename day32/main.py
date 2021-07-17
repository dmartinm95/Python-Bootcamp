# Day 32: Send Email (SMTP - Simple Mail Transfer Protocol) and Manage Dates
import pandas
import datetime as dt
import random
import smtplib

# Make sure email used has less privacy settings set up
# my_email = "someemail@gmail.com"
# password = "password"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="someotheremail@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")

# Get current date and time
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1995, month=6, day=16)

with open("day32\\quotes.txt") as file:
    content = file.readlines()

content = [x.strip() for x in content]
chosen_quote = random.choice(content)
print(chosen_quote)

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

data = pandas.read_csv("day32\\birthdays.csv")
print(data)

todays_date = dt.datetime.now()
birthday_name = ""
letters = []

with open("day32\\letter_templates\\letter_1.txt") as file:
    content = file.readlines()
    letters.append(content)
with open("day32\\letter_templates\\letter_2.txt") as file:
    content = file.readlines()
    letters.append(content)
with open("day32\\letter_templates\\letter_3.txt") as file:
    content = file.readlines()
    letters.append(content)

letter_chosen = random.choice(letters)

for index, row in data.iterrows():
    if todays_date.month == row["month"] and todays_date.day == row["day"]:
        birthday_name = row["name"]
        letter_chosen[0] = letter_chosen[0].replace("[NAME]", birthday_name)
        print(f"Today is {birthday_name}'s birthday!")

print(letter_chosen)

# Need to create a new gmail to test out with less security level
# my_email = "someoneemail@gmail.com"
# password = "password"


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="someotheremail@gmail.com",
#                         msg=f"Subject:Happy Birthday!!\n\n{letter_chosen}")
