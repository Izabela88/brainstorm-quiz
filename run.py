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
# To become a Brainstorm Champion, you have to answer all the questions.
# But be careful!
# The total playing time also counts! HAVE FUN!
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
    console.print("\nGAME MENU:\n", style="info")
    for key, value in menu.items():
        print(f"{key} - {value.upper()}")

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
            questions = Questions(1)
        else:
            questions = Questions(1)
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


def champion_type(player) -> None:
    ch_txt1 = "WELL DONE! YOU BECOME A GREATEST CHAMPION OF BRAINSTORM "
    ch_txt2 = "QUIZ IN THE EARTH!\n"
    ch_txt3 = "WOW! YOUR KNOWLEDGE IS IMPRESSIVE!"
    ch_txt4 = "YOU BECOME A GREATEST CHAMPION OF BRAINSTORM QUIZ "
    ch_txt5 = "IN THE WHOLE GALAXY!!!\n"
    ch_type1 = Panel.fit(Markdown(
        ch_txt1 + ch_txt2, justify="center"
        ), width=60, style="gold1")
    ch_type2 = Panel.fit(Markdown(
        ch_txt3 + ch_txt4 + ch_txt5, justify="center"
        ), width=60, style="gold1")
    if player.game_level == "normal":
        console.print(ch_type1)
    else:
        console.print(ch_type2)


def show_question_no(question_number) -> None:
    show_question_no = Panel.fit(
        Markdown(f"\nQUESTION NO. {question_number}:", justify="center"),
        width=60,
        style="bold dark_blue",
    )
    console.print(show_question_no)


def show_lifeline_qty(player):
    if player.lifeline_qty >= 1:
        l_suffix = "" if player.lifeline_qty == 1 else "S"
        l_txt = f"LIFELINE{l_suffix}"
        console.print(f"[warning]YOU HAVE {player.lifeline_qty} " + l_txt)


def new_game(player) -> bool:
    continue_game = False
    if not player.name:
        name = input_validate(
            "\nPLEASE TYPE YOUR NAME: ",
            is_int=False,
            range_list=None,
            case_sensitive=True,
            max_length=20,
            min_length=3,
        )
        player.name = name
        w_txt = "welcome to BRAINSTORM QUIZ!"
        console.print(f"\n[info]Hello {player._name} " + w_txt)

    player.pick_game_level()
    questions = start_game_menu(player)
    time_counting()
    player.start_game_time = time.time()
    player.score = 0
    question_number = 1
    while True:
        try:
            next_game_question = questions.next_question()
        except IndexError:
            champion_type(player)
            final_results(player)
            save_score(player)
            q = Confirm.ask("Do you want to play again? ")
            if q is True:
                continue_game = True
            break
        show_question_no(question_number)
        next_game_question.print_question()

        show_lifeline_qty(player)

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
                console.print(
                    "OUCH! YOU DON'T HAVE ANY LIFELINES!",
                    style="danger"
                    )
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
            final_results(player)
            save_score(player)
            q = Confirm.ask("Do you want to play again?")
            if q is True:
                continue_game = True
                c1 = f"[info]\nWOW! YOU DON'T GIVE UP {player._name}! "
                c2 = "COOL!"
                console.print(c1 + c2)
            break
    return continue_game


def save_score(player):
    score_board = ScoreBoard(player)
    if score_board.is_score_qualified():
        score_board.save_score()


def final_results(player) -> None:
    console.print(f"[info]{player.name} YOUR FINAL SCORE IS: {player.score}\n")
    player.game_time = time.time() - player.start_game_time
    t = time.strftime("[info]%H:%M:%S\n", time.gmtime(player.game_time))
    console.print(f"[info]{player.name} YOUR GAME TIME IS: " + t)


def best_scores() -> None:
    best_scores = ScoreBoard()
    best_scores.show_best_scores()


def manage_menu_options() -> None:
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


if __name__ == "__main__":
    run_brainstorm()
