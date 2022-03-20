# import requests
# import random
# from tkinter import *
# import html

# #Basic Needs
# THEME_COLOR="#375362"
# score=0
# i=TRUE

# response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
# response.raise_for_status()
# data = response.json()
# number=random.randint(1,9)
# quest = html.unescape([i['question'] for i in data["results"]][number])
# answer = [i['correct_answer'] for i in data["results"]][number]

# question_number=0
# score=0
# question_list=quest
# current_question=None

# def keep_quizing():
#     global i
#     global score
#     print(question)
#     x=input("(True/False)\n")
#     if x==answer:
#         print('You guessed it right')
#         score+=1
#         print(f"Your current score is {score}/5")

#         if score>=3:
#             print("You won")
#             i=False

#     else :
#         print("your guess is incorrect")
#         score+=-1
#         print(f"Your current score is {score}/5")
#         if score<=-2:
#             z=False
#             print("you lose")
#             i=False

# def true_pressed():
#     pass

# def false_pressed():
#     pass

# def feedback():
#     pass

# window = Tk()
# window.title("Quiz App")
# window.config(padx=50,pady=50,bg=THEME_COLOR)
# canvas = Canvas(width=300,height=250,bg="White")
# question=canvas.create_text(
#             150,
#             125,
#             width=280,
#             text="Some Question Text",
#             fill=THEME_COLOR,
#             font=("Arial", 20, "italic")
#         )
# canvas.itemconfig(question(text=f"{quest}"))
# canvas.grid(row=1, column=0, columnspan=2, pady=50)

# true_image = PhotoImage(file="images/true.png")
# true_button = Button(image=true_image, highlightthickness=0, command=true_pressed)
# true_button.grid(row=2,column=0)

# false_image = PhotoImage(file="images/false.png")
# false_button = Button(image=false_image, highlightthickness=0, command=false_pressed)
# false_button.grid(row=2, column=1)

# while i:
#     keep_quizing()
# window.mainloop()

# #Don't go up its scary there caused me a brain zapp!!!

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
