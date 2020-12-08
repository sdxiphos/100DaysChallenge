import requests


class Question:
    def __init__(self):
        self.data = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
        self.data.raise_for_status()
        self.question_data_list = self.data.json()