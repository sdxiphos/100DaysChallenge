import html


class QuestionController:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_model = None
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list)-1:
            return True
        else:
            return False

    def next_question(self):
        self.question_model = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:"
                            f"{html.unescape(self.question_model.question)}"
                            f" True or False:\n")
        self.check_answer(user_answer)

    def check_answer(self, answer):
        if answer == self.question_model.answer:
            self.score += 1
            print(f"You are correct!\nYour score is : {self.score}")
        else:
            print("You are wrong")
