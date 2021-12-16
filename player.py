from messages import PLAYER__RULES_TEXT
from utility import input_validate
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from messages import RUN__NORMAL_TITLE
from messages import RUN__EXPERT_TITLE
import time
from questions import Question


console = Console()


class Player:
    """Player class"""

    def __init__(self) -> None:
        """Player construct method"""
        self._name = None
        self.score = 0
        self.game_level = None
        self.lifeline_qty = 0
        self.start_game_time = None
        self.game_time = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        self._name = name

    def player_name(self) -> None:
        """Get name for the player"""
        name = input_validate(
            "\nPLEASE TYPE YOUR NAME: ",
            is_int=False,
            allowed_list=None,
            case_sensitive=True,
            max_length=20,
            min_length=3,
        )
        self._name = name
        w_txt = "welcome to BRAINSTORM QUIZ!"
        console.print(f"\n[info]Hello {self._name} " + w_txt)

    def final_results(self) -> None:
        """Display player final stats"""
        console.print(f"[info]{self.name} YOUR FINAL SCORE IS: {self.score}\n")
        self.game_time = time.time() - self.start_game_time
        t = time.strftime("[info]%H:%M:%S\n", time.gmtime(self.game_time))
        console.print(f"[info]{self.name} YOUR GAME TIME IS: " + t)

    def champion_type_title(self) -> None:
        """Display player title when player finished the game"""
        normal_title = Panel.fit(
            Markdown(RUN__NORMAL_TITLE, justify="center"),
            width=60,
            style="gold1",
        )
        expert_title = Panel.fit(
            Markdown(RUN__EXPERT_TITLE, justify="center"),
            width=60,
            style="gold1",
        )
        if self.game_level == "normal":
            console.print(normal_title)
        else:
            console.print(expert_title)

    def show_lifeline_qty(self) -> None:
        """Display player lifline quantity"""
        if self.lifeline_qty >= 1:
            l_suffix = "" if self.lifeline_qty == 1 else "S"
            l_txt = f"LIFELINE{l_suffix}"
            console.print(f"[yellow1]YOU HAVE {self.lifeline_qty} " + l_txt)

    def lifeline_option(self, game_question: Question) -> None:
        """Control the player lifline quantity and trigger question lifeline
        logic

        :param game_question: Game question instance
        :type game_question: Question
        """
        if self.lifeline_qty:
            self.lifeline_qty -= 1
            game_question.lifeline()
        if self.lifeline_qty == 0:
            console.print("OUCH! YOU DON'T HAVE ANY LIFELINES!", style="red")

    def pick_game_level(self) -> str:
        """Handles player game level choice

        :return: Game level name
        :rtype: str
        """

        def _display_panel() -> None:
            """Display game level info panel"""
            msg = f"\nYou picked level: '{level_menu[level].upper()}'"
            print(
                Panel.fit(
                    Markdown(msg, justify="center"),
                    width=60,
                    style="bold dark_blue",
                )
            )
            print(
                Panel.fit(
                    Markdown(
                        PLAYER__RULES_TEXT.format(
                            questions_qty, self.lifeline_qty, title
                        ),
                        justify="center",
                    ),
                    width=60,
                    style="bold dark_blue",
                )
            )

        print("\nPlease choose a game level: \n")
        level_menu = {
            1: "normal",
            2: "expert",
        }
        for key, value in level_menu.items():
            print(f"{key} - {value.upper()}")
        level = input_validate(
            "\nENTER YOUR CHOICE: ",
            is_int=True,
            allowed_list=[1, 2],
            min_length=1,
            max_length=1,
        )

        if level == 1:
            questions_qty = 10
            self.lifeline_qty = 2
            title = "IN THE EARTH!"
        else:
            questions_qty = 20
            self.lifeline_qty = 4
            title = "IN THE WHOLE GALAXY!"
        self.game_level = level_menu[level]
        _display_panel()
        return level_menu[level]
