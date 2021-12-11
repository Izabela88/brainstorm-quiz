import time
from sys import stdout
from time import sleep

from player import Player
from questions import Question, Questions
from score_board import ScoreBoard
from utility import input_validate


def handle_menu() -> int:
    menu = {
        1: "new game",
        2: "best scores",
        3: "exit",
    }
    for key, value in menu.items():
        print(f"{key} - {value.upper()}")

    return input_validate(
        "\nENTER YOUR CHOICE: ", is_int=True, range_list=[1, 2, 3]
    )


def start_game_menu(player: Player) -> Question:
    while True:
        input_validate(
            "TYPE s TO START BRAINSTORM QUIZ: ", is_int=False, range_list=["s"]
        )
        if player.game_level == 1:
            questions = Questions(10)
        else:
            questions = Questions(20)
        questions.draw_questions()
        return questions


def time_counting() -> None:
    print("\nLET'S BEGIN!")
    for i in range(5, 0, -1):
        stdout.write("\r%d" % i)
        stdout.flush()
        sleep(1)
    stdout.write("\nSTART!\n")


def new_game() -> None:
    name = input_validate(
        "\nPLEASE TYPE YOUR NAME: ",
        is_int=False,
        range_list=None,
        case_sensitive=True,
    )
    player = Player(name)
    print(f"\nHello {player.name}, welcome to BRAINSTORM QUIZ!")
    player.pick_game_level()
    questions = start_game_menu(player)
    time_counting()
    player.start_game_time = time.time()
    question_number = 1
    while True:
        try:
            next_game_question = questions.next_question()
        except IndexError:
            print(
                "\nCONGRATULATIONS! YOU HAVE JUST COMPLETED BRAINSTORM QUIZ!"
            )
            print("THANK YOU FOR THE GAME!\n")
            print(f"{player.name} your final score is: {player.score}\n")
            player.game_time = time.time() - player.start_game_time
            print(f"{player.name} your game time is: ")
            print(time.strftime("%H:%M:%S\n", time.gmtime(player.game_time)))
            score_board = ScoreBoard(player)
            if score_board.is_score_qualified():
                score_board.save_score()
            break
        print(
            "---------------------------------------------------------------"
        )
        print(f"\nQUESTION NO. {question_number}:")
        next_game_question.print_question()
        if player.lifeline_qty >= 1:
            lifeline_suffix = "" if player.lifeline_qty == 1 else "S"
            print(
                "YOU HAVE" f" {player.lifeline_qty} LIFELINE{lifeline_suffix}"
            )

        answer = input_validate(
            "\nYOUR ANSWER IS: ",
            is_int=False,
            range_list=["a", "b", "c", "d", "h"],
        )

        if answer == "h":
            if player.lifeline_qty:
                player.lifeline_qty -= 1
                next_game_question.lifeline()
            if player.lifeline_qty == 0:
                print("OUCH! YOU DON'T HAVE ANY LIFELINES!")
            answer = input_validate(
                "\nYOUR ANSWER IS: ",
                is_int=False,
                range_list=["a", "b", "c", "d"],
            )
        if next_game_question.is_answer_correct(answer):
            question_number += 1
            print("\nGREAT! CORRECT ANSWER!\n")
            player.score += 10
            print(f"AWSOME! YOU HAVE {player.score} POINTS!")
            continue
        else:
            print("\nOH NO! INCORRECT ANSWER!\n")
            print("GAME OVER!\n")
            player.game_time = time.time() - player.start_game_time
            score_board = ScoreBoard(player)
            if score_board.is_score_qualified():
                score_board.save_score()
            break


def best_scores() -> None:
    best_scores = ScoreBoard()
    best_scores.show_best_scores()


def manage_menu_options() -> None:
    print("\n***THIS IS THE BRAINSTORM QUIZ***\n")
    print("MENU:")
    while True:
        option = int(handle_menu())
        if option == 1:
            new_game()
        elif option == 2:
            best_scores()
        elif option == 3:
            break

    print("Thank you for the Game!")


if __name__ == "__main__":
    manage_menu_options()
