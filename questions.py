import json
import random


class Questions:
    def __init__(self, qty):
        self.qty = qty
        self.game_questions = []

    def draw_questions(self):
        raw_questions = load_from_file()
        for i in random.choices(raw_questions, k=self.qty):
            question = Question(i["question"], i["answers"], i["correct_answer"])
            self.game_questions.append(question)
        return self.game_questions


class Question:
    def __init__(self, question, answers, correct_answer) -> None:
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer


def load_from_file():
    with open("questions.json", "r") as json_file:
        return json.load(json_file)
