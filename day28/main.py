# Day 28: Pomodoro App
import time
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
timer_running = False
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0
    global timer_running
    timer_running = False


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global timer_running

    if not timer_running:
        global reps
        reps += 1

        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        timer_running = True

        if reps % 8 == 0:
            title_label.config(text="Break", fg=RED)
            count_down(long_break_sec)
        elif reps % 2 == 0:
            title_label.config(text="Break", fg=PINK)
            count_down(short_break_sec)
        else:
            title_label.config(text="Work", fg=GREEN)
            count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""

        for _ in range(math.floor(reps/2)):
            marks += "✔"
            check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(
    FONT_NAME, 55, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day28\\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", font=(
    FONT_NAME, 10, "normal"), padx=2, pady=2, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(
    FONT_NAME, 10, "normal"), padx=2, pady=2, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


check_label = Label(font=(
    FONT_NAME, 25, "normal"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()
