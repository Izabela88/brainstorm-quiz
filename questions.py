import json
import random

class Questions:

    def __init__(self, qty):
        self.qty = qty

    def draw_questions(self):
        questions = load_from_file()
        game_questions = random.choices(questions, k=10)
        return game_questions


class Question:
   
    def __init__(self, question, answers, correct_answer) -> None:
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer


def load_from_file():
    with open("questions.json","r") as json_file:
        return json.load(json_file)


