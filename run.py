import time
from messages import RUN__QUIZ_TITLE
from messages import RUN__MODULE_1
from player import Player
from questions import Questions
from score_board import ScoreBoard
from utility import input_validate
from utility import time_counting
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown
from rich.theme import Theme
from rich.prompt import Confirm


custom_theme = Theme(
    {
        "info": "bold dark_blue",
        "warning": "bold yellow1",
        "danger": "bold red",
        "general": "bold dark_violet",
        "correct": "chartreuse3",
    }
)

console = Console(theme=custom_theme)


def run_brainstorm():
    """Main function that init game"""
    while True:

        def _print_game_panel() -> None:
            """Helper function. Print out the first block when game launch"""
            panel_title = Panel.fit(
                Markdown(RUN__QUIZ_TITLE, justify="center"), width=60
            )
            panel_1 = Panel.fit(
                Markdown(RUN__MODULE_1, justify="center"),
                width=60,
                title="RULES",
                subtitle="[danger]PRESS ENTER TO BEGIN",
            )
            console.print(panel_title, style="warning")
            console.print(panel_1, style="info")

        _print_game_panel()
        enter_game = input()
        if len(enter_game) > 0:
            console.print(
                "Please press ENTER to start game!",
                style="danger",
                justify="left",
            )
            continue
        manage_menu_options()


def manage_menu_options() -> None:
    """Control game menu options.
    Player can pick one of the options that is displayed.
    """
    player = Player()
    while True:
        option = int(handle_menu())
        if option == 1:
            if not new_game(player):
                console.print("\n:heart:  THANK YOU FOR THE GAME! :heart:\n")
                break
        elif option == 2:
            best_scores()
        elif option == 3:
            console.print("\n:heart:  BYE BYE! :heart:\n")
            break


def handle_menu() -> int:
    """Display game menu options and handle user input

    :return: User input, after validation
    :rtype: int
    """
    menu = {
        1: "new game",
        2: "best scores",
        3: "exit",
    }
    console.print("\nGAME MENU:\n", style="info")
    for key, value in menu.items():
        print(f"{key} - {value.upper()}")

    return input_validate(
        "\nENTER YOUR CHOICE: ",
        is_int=True,
        allowed_list=[1, 2, 3],
        max_length=1,
    )


def best_scores() -> None:
    """Display best scores"""
    best_scores = ScoreBoard()
    best_scores.show_best_scores()


def new_game(player: Player) -> bool:
    """This is core logic of the Brainstorm game mode. Function handles
    questions and user answers

    :param player: Game player
    :type player: Player
    :return: True if player would like to continue game, else False
    :rtype: bool
    """
    continue_game = False
    player.is_new_player()
    player.pick_game_level()
    questions = init_questions(player)
    input_validate(
        "\nTYPE s TO START BRAINSTORM QUIZ: ", is_int=False, allowed_list=["s"]
    )
    time_counting()
    player.start_game_time = time.time()
    player.score = 0
    while True:
        try:
            next_game_question = questions.next_question()
        except IndexError:
            player.champion_type_title()
            player.final_results()
            save_score(player)
            continue_game = Confirm.ask("Do you want to play again? ")
            break
        questions.show_question_no()
        next_game_question.print_question()
        player.show_lifeline_qty()
        answer = input_validate(
            "\nYOUR ANSWER IS: ",
            is_int=False,
            allowed_list=["a", "b", "c", "d", "h"],
            max_length=1,
            min_length=1,
        )
        if answer == "h":
            player.lifeline_option(next_game_question)
            answer = input_validate(
                "\nYOUR ANSWER IS: ",
                is_int=False,
                allowed_list=["a", "b", "c", "d"],
                max_length=1,
                min_length=1,
            )

        if next_game_question.is_answer_correct(answer):
            correct_answer(player)
            questions.question_number += 1
            continue
        else:
            incorrect_answer()
            player.final_results()
            save_score(player)
            continue_game = Confirm.ask("Do you want to play again?")
            if continue_game:
                continue_msg = (
                    f"[info]\nWOW! YOU DON'T GIVE UP {player._name}! COOL!"
                )
                console.print(continue_msg)
            break
    return continue_game


def init_questions(player: Player) -> Questions:
    """Initate game questions. Function will handle quantity and

    :param player: Game player
    :type player: Player
    :return: Questions instance after init with questions qty
    :rtype: Questions
    """

    if player.game_level == "normal":
        questions = Questions(10)
    else:
        questions = Questions(20)
    questions.draw_questions()
    return questions


def correct_answer(player: Player) -> None:
    """Display message and top up player score when aswer is correct

    :param player: Game player
    :type player: Player
    """
    console.print("\n:thumbs_up: [correct]GREAT! CORRECT ANSWER!\n")
    player.score += 10
    console.print(f"[general]AWSOME! YOU HAVE {player.score} POINTS!")


def incorrect_answer() -> None:
    """Display messages when answer is incorrect"""
    console.print("\n:thumbsdown: [danger]OH NO! INCORRECT ANSWER!\n")
    console.print(":x: [danger]GAME OVER!:x:\n")


def save_score(player: Player) -> None:
    """Save player score if qualified

    :param player: Game player instance
    :type player: Player
    """
    score_board = ScoreBoard(player)
    if score_board.is_score_qualified():
        score_board.save_score()


if __name__ == "__main__":
    run_brainstorm()
