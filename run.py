import time
from sys import stdout
from time import sleep
from player import Player
from questions import Questions
from score_board import ScoreBoard
from utility import input_validate
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

q_title = """
# *** THIS IS THE BRAINSTORM QUIZ ***
"""

md1 = """
# Your goal is to collect as many points as possible.
# To become a Brainstorm King, you have to answer all the questions.
# But be careful! 
# The total playing time is also counts! HAVE FUN!
"""


def run_brainstorm():
    while True:
        panel_title = Panel.fit(Markdown(q_title, justify="center"), width=60)
        panel_1 = Panel.fit(
            Markdown(md1, justify="center"),
            width=60,
            title="RULES",
            subtitle="[danger]PRESS ENTER TO BEGIN",
        )
        console.print(panel_title, style="warning")
        console.print(panel_1, style="info")

        enter_game = input()
        if len(enter_game) > 0:
            console.print(
                "Please press ENTER to start game!", style="danger", 
                justify="left"
            )
            continue
        manage_menu_options()


def handle_menu() -> int:
    menu = {
        1: "new game",
        2: "best scores",
        3: "exit",
    }
    console.print("\nMENU:\n", style="info")
    for key, value in menu.items():
        print(f"{key} - {value.upper()}\n")

    return input_validate(
        "\nENTER YOUR CHOICE: ", is_int=True, range_list=[1, 2, 3], 
        max_length=1
    )


def start_game_menu(player: Player) -> Questions:
    while True:
        input_validate(
            "\nTYPE s TO START BRAINSTORM QUIZ: ", is_int=False, 
            range_list=["s"]
        )
        if player.game_level == "normal":
            questions = Questions(3)
        else:
            questions = Questions(20)
        questions.draw_questions()
        return questions


def time_counting() -> None:
    start_msg = Panel.fit(
        Markdown("\nLET'S BEGIN!", justify="center"), width=60, style="warning"
    )
    console.print(start_msg)
    for i in range(5, 0, -1):
        stdout.write("\r%d" % i)
        stdout.flush()
        sleep(1)
    stdout.write("\n\n")


def new_game() -> bool:
    continue_game = False
    name = input_validate(
        "\nPLEASE TYPE YOUR NAME: ",
        is_int=False,
        range_list=None,
        case_sensitive=True,
        max_length=20,
        min_length=3,
    )
    player = Player(name)
    console.print(f"\n[info]Hello {player.name}, welcome to BRAINSTORM QUIZ!")
    player.pick_game_level()
    questions = start_game_menu(player)
    time_counting()
    player.start_game_time = time.time()
    question_number = 1
    while True:
        c_msg = "CONGRATULATIONS! YOU BECOME A KING OF BRAINSTORM QUIZ!\n"
        emo = "\n:smiling_face_with_sunglasses: "
        try:
            next_game_question = questions.next_question()
        except IndexError:
            console.print(emo + c_msg, style="gold1")
            final_results(player)
            save_score(player)
            q = Confirm.ask("Do you want to play again? ")
            if q is True:
                continue_game = True
            break
        console.print(f"\n[info]QUESTION NO. {question_number}:")
        next_game_question.print_question()

        if player.lifeline_qty >= 1:
            l_suffix = "" if player.lifeline_qty == 1 else "S"
            l_txt = f"LIFELINE{l_suffix}"
            console.print(f"[warning]YOU HAVE {player.lifeline_qty} " + l_txt)

        answer = input_validate(
            "\nYOUR ANSWER IS: ",
            is_int=False,
            range_list=["a", "b", "c", "d", "h"],
            max_length=1,
            min_length=1,
        )
        if answer == "h":
            if player.lifeline_qty:
                player.lifeline_qty -= 1
                next_game_question.lifeline()
            if player.lifeline_qty == 0:
                console.print("OUCH! YOU DON'T HAVE ANY LIFELINES!", 
                style="danger")
            answer = input_validate(
                "\nYOUR ANSWER IS: ",
                is_int=False,
                range_list=["a", "b", "c", "d"],
                max_length=1,
                min_length=1,
            )
        if next_game_question.is_answer_correct(answer):
            question_number += 1
            console.print("\n:thumbs_up: [correct]GREAT! CORRECT ANSWER!\n")
            player.score += 10
            console.print(f"[general]AWSOME! YOU HAVE {player.score} POINTS!")
            continue
        else:
            console.print("\n:thumbsdown: [danger]OH NO! INCORRECT ANSWER!\n")
            console.print(":x: [danger]GAME OVER!:x:\n")
            q = Confirm.ask("Do you want to play again? ")
            if q is True:
                continue_game = True
            final_results(player)
            save_score(player)
            break
    return continue_game


def save_score(player):
    score_board = ScoreBoard(player)
    if score_board.is_score_qualified():
        score_board.save_score()


def final_results(player) -> None:
    console.print(f"[info]{player.name} YOUR FINAL SCORE: {player.score}\n")
    player.game_time = time.time() - player.start_game_time
    t = time.strftime("[info]%H:%M:%S\n", time.gmtime(player.game_time))
    console.print(f"[info]{player.name} YOUR GAME TIME: " + t)


def best_scores() -> None:
    best_scores = ScoreBoard()
    best_scores.show_best_scores()


def manage_menu_options() -> None:
    while True:
        option = int(handle_menu())
        if option == 1:
            if not new_game():
                console.print("\n:heart:  THANK YOU FOR THE GAME! :heart:\n")
                break
        elif option == 2:
            best_scores()
        elif option == 3:
            break


if __name__ == "__main__":
    run_brainstorm()
