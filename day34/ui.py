from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 16, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)

        self.score_label = Label(
            text="Score: 0", background=THEME_COLOR, fg="white", font=20)
        self.score_label.grid(row=0, column=1, padx=20, pady=(20, 0))

        self.canvas = Canvas(width=300, height=250, bg="white")

        self.quote_text = self.canvas.create_text(
            150, 125, text="Question quote", width=280, font=FONT, fill="black")

        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        false_button_image = PhotoImage(file="day34\\images\\false.png")
        true_button_image = PhotoImage(file="day34\\images\\true.png")

        self.false_button = Button(
            image=false_button_image, highlightthickness=0, command=self.false_button_press)
        self.false_button.grid(row=2, column=0, pady=(0, 20))

        self.true_button = Button(
            image=true_button_image, highlightthickness=0, command=self.true_button_press)
        self.true_button.grid(row=2, column=1, pady=(0, 20))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=question_text)
        else:
            self.canvas.itemconfig(
                self.quote_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def false_button_press(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def true_button_press(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
