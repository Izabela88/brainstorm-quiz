import json
import random
from typing import List
from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown

console = Console()


class Questions:
    def __init__(self, qty: int) -> None:
        self.qty = qty
        self.game_questions = []
        self.question_number = 1

    def show_question_no(self) -> None:
        show_question_number = Panel.fit(
            Markdown(
                f"\nQUESTION NO. {self.question_number}:", justify="center"
            ),
            width=60,
            style="bold dark_blue",
        )
        console.print(show_question_number)

    def draw_questions(self) -> None:
        raw_questions = load_from_file()
        for i in random.sample(raw_questions, k=self.qty):
            question = Question(
                i["question"], i["answers"], i["correct_answer"]
            )
            self.game_questions.append(question)
        return self.game_questions

    def next_question(self) -> None:
        return self.game_questions.pop()


class Question:
    def __init__(
        self, question: str, answers: List[str], correct_answer: int
    ) -> None:
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
        self.answers_mapping = {"a": 0, "b": 1, "c": 2, "d": 3}

    def print_question(self, print_only: list = None) -> None:
        show_question = Panel.fit(
            Markdown(f"\n{self.question}\n", justify="center"),
            width=60,
            style="bold dark_blue",
        )
        console.print(show_question)

        for idx, i in enumerate(self.answers):
            if print_only and idx not in print_only:
                continue
            print(f"{list(self.answers_mapping.keys())[idx]}: {i}\n")

    def is_answer_correct(self, player_answer: int) -> bool:
        if self.answers_mapping.get(player_answer) == self.correct_answer:
            return True
        return False

    def lifeline(self) -> None:
        answers_copy = list(self.answers)
        for idx, _ in enumerate(answers_copy):
            answers_copy[idx] = idx
        incorrect_answers = list(set(answers_copy) - {self.correct_answer})
        lifeline_answers = random.sample(incorrect_answers, k=1)
        lifeline_answers.append(self.correct_answer)
        self.print_question(lifeline_answers)


def load_from_file() -> list:
    with open("questions.json", "r") as json_file:
        return json.load(json_file)
