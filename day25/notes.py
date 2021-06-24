# Day 25: Working with CSV Data and the Pandas Library

# import csv

# with open("day25\weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
from pandas.core.frame import DataFrame

data = pandas.read_csv("day25\weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].max())
print(data["temp"].mean())


# Get data in Columns
print(data["condition"])
print(data.condition)

# Get data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(f"Monday's temp in Fahrenheit = {int(monday.temp) * 9 / 5 + 32}")


# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

data_frame = pandas.DataFrame(data_dict)

print(data_frame)

# Challenge: Figure out how many Gray, Black and Red squirrels there are, according to the csv file
squirrel_data = pandas.read_csv(
    "day25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color_column = squirrel_data["Primary Fur Color"]


grey_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_count = len(
    squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
red_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

output_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_count, red_count, black_count],
}

output_data_frame = pandas.DataFrame(output_dict)

output_data_frame.to_csv("day25\squirrel_count.csv")
