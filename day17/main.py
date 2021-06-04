from question_model import Question
from data import question_data, new_question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(0, len(new_question_data)):
    text = new_question_data[i]['question']
    ans = new_question_data[i]['correct_answer']
    question_bank.append(Question(text, ans))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
