# Day 31: Flash Card App Capstone Project
from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

current_card = {}
to_learn = {}
try:
    data = pandas.read_csv(
        "day31\\data\\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("day31\\data\\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("day31\\data\\words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)
window["background"] = BACKGROUND_COLOR

card_back_image = PhotoImage(file="day31\\images\\card_back.png")
card_front_image = PhotoImage(file="day31\\images\\card_front.png")
right_image = PhotoImage(file="day31\\images\\right.png")
wrong_image = PhotoImage(file="day31\\images\\wrong.png")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526,
                highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=LANG_FONT)
card_word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)


wrong_btn = Button(image=wrong_image, highlightthickness=0,
                   command=next_card)
wrong_btn.grid(row=1, column=0)

right_btn = Button(image=right_image, highlightthickness=0,
                   command=is_known)
right_btn.grid(row=1, column=1)

next_card()

window.mainloop()
