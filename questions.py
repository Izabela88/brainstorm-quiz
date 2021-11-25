import json
import random
import pprint
pp = pprint.PrettyPrinter()


class Question:
   
    def __init__(self, question, answers, correct_answer) -> None:
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer


def load_from_file():
    with open("questions.json","r") as json_file:
        questions = json.load(json_file)
        random.choices(questions, k=10)
        print(questions)

load_from_file()

