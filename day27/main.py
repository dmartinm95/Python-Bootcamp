# Day 27: Tkinter
from tkinter import *
from playground import add, calculate, Car

window = Tk()

window.title("Mile to Km Converter")
# window.minsize(width=300, height=50)
window.config(padx=20, pady=20)

# # Label
# my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.grid(column=0, row=0)

# my_label["text"] = "New Text"
# my_label.config(text="New Text")


# def button_clicked():
#     input_str = input.get()
#     my_label["text"] = input_str
#     print("Button got clicked")


# # Button
# my_button = Button(text="Click Me", command=button_clicked)
# my_button.grid(column=1, row=1)

# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)


# # Entry
# input = Entry(width=10)
# input.grid(column=3, row=2)


# # Examples using *args and **kwargs
# print(add(2, 3, 5, 6, 7, 8))
# print(calculate(5, add=5, multiply=10))

# my_car = Car(make="Nissan")
# print(my_car.make)


miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

text_label = Label(text="is equal to")
text_label.grid(column=0, row=1)

km_val_label = Label(text="0")
km_val_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def calculate_pressed():
    miles = float(miles_entry.get())
    km = miles * 1.6093
    km_val_label["text"] = "{: .2f}".format(km)


calculate_button = Button(text="Calculate", command=calculate_pressed)
calculate_button.grid(column=1, row=2)


# This will keep the window on screen and listen for user inputs (keep at end of program)
window.mainloop()
