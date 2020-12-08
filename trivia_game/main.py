from question_model import QuestionModel
from question_controller import QuestionController
from trivia_integration import Question
import time

questions = Question()
questions_data = questions.question_data_list["results"]
question_list = []
for question_data in questions_data:
    question_text = question_data["question"]
    question_answer = question_data["correct_answer"]
    next_question = QuestionModel(question_text, question_answer)
    question_list.append(next_question)

question_controller = QuestionController(question_list)

while True:
    if question_controller.still_has_question():
        question_controller.next_question()
    else:
        print("End of the Game!")
        brake

