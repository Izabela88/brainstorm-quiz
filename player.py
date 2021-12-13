from utility import input_validate
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel


console = Console()


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0
        self.game_level = None
        self.lifeline_qty = 0
        self.start_game_time = None
        self.game_time = None

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
                "\nENTER YOUR CHOICE: ", is_int=True, range_list=[1, 2]
            )
            if level == 1:
                questions_qty = 10
                self.lifeline_qty = 2
            else:
                questions_qty = 20
                self.lifeline_qty = 4
            self.game_level = level_menu[level]

            s = " lifelines to remove two wrong answers."
            s1 = f"You will be presented with {questions_qty} questions."
            s2 = " Enter the appropriate letter to answer the question."
            s3 = f" In case of trouble, you can use {self.lifeline_qty}" + s
            s4 = " To use your lifeline press 'h'."
            s5 = " GOOD LUCK!"
            s6 = f"\nYou picked level: '{level_menu[level].upper()}'"
            print(Panel.fit(Markdown(s6), width=60))
            print(Panel.fit(Markdown(s1 + s2 + s3 + s4 + s5 ),width=60))
            return level_menu[level]
