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

    def next_question(self):
        return self.game_questions.pop()


class Question:
    def __init__(self, question, answers, correct_answer) -> None:
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
        self.answers_mapping = {"a": 0, "b": 1, "c": 2, "d": 3}

    def print_question(self, print_only=None):
        print(f"\n{self.question}\n")

        for idx, i in enumerate(self.answers):
            if print_only and idx not in print_only:
                continue
            print(f"{list(self.answers_mapping.keys())[idx]}: {i}\n")

    def is_answer_correct(self, player_answer):
        if self.answers_mapping.get(player_answer) == self.correct_answer:
            return True
        return False

    def lifeline(self):
        answers_copy = list(self.answers)
        for idx, _ in enumerate(answers_copy):
            answers_copy[idx] = idx
        incorrect_answers = list(set(answers_copy) - {self.correct_answer})
        lifeline_answers = random.choices(incorrect_answers, k=1)
        lifeline_answers.append(self.correct_answer)
        self.print_question(lifeline_answers)


def load_from_file():
    with open("questions.json", "r") as json_file:
        return json.load(json_file)
