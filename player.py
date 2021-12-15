from utility import input_validate
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel


console = Console()


class Player:
    def __init__(self) -> None:
        self._name = None
        self.score = 0
        self.game_level = None
        self.lifeline_qty = 0
        self.start_game_time = None
        self.game_time = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def pick_game_level(self) -> str:
        print("\nPlease choose a game level: \n")
        level_menu = {
            1: "normal",
            2: "expert",
        }
        for key, value in level_menu.items():
            print(f"{key} - {value.upper()}")

        while True:
            level = input_validate(
                "\nENTER YOUR CHOICE: ",
                is_int=True,
                range_list=[1, 2],
                min_length=1,
                max_length=1,
            )
            if level == 1:
                questions_qty = 10
                self.lifeline_qty = 2
                game_title = "IN THE EARTH!"
            else:
                questions_qty = 20
                game_title = "IN THE WHOLE GALAXY!"
                self.lifeline_qty = 4
            self.game_level = level_menu[level]

            txt0 = " lifelines to remove two wrong answers."
            txt1 = f"You will be presented with {questions_qty} questions."
            txt2 = " Enter the appropriate letter to answer the question."
            txt3 = f" In case of trouble, you can use {self.lifeline_qty}"
            +txt0
            txt4 = " To use your lifeline press 'h'."
            txt_t = f"THE GREATEST CHAMPION {game_title}"
            txt5 = " After completing the quiz, you will receive a title: "
            +txt_t
            txt6 = " GOOD LUCK!"
            txt7 = f"\nYou picked level: '{level_menu[level].upper()}'"
            print(
                Panel.fit(
                    Markdown(txt7, justify="center"),
                    width=60, style="bold dark_blue"
                )
            )
            print(
                Panel.fit(
                    Markdown(
                        txt1 + txt2 + txt3 + txt4 + txt5 + txt6,
                        justify="center"
                        ),
                    width=60,
                    style="bold dark_blue",
                )
            )
            return level_menu[level]
