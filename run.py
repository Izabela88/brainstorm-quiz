from player import Player
from questions import Questions
from utility import input_validate
from sys import stdout
from time import sleep
import time

def handle_menu():
    menu = {
        1: "New Game",
        2: "Best Scores",
        3: "Exit",
    }
    for key, value in menu.items():
        print(f"{key} - {value}")
    
    return input_validate("\nENTER YOUR CHOICE: ",is_int=True,range_list=[1,2,3])

def start_game_menu(player):
    while True:
        input_validate("TYPE S TO START BRAINSTORM QUIZ: ",is_int=False,range_list=["S"])
        if player.game_level == 1:
            questions = Questions(10)
        else:
            questions = Questions(20)
        questions.draw_questions()
        return questions

def time_counting():
    print("\nLET'S BEGIN!")
    for i in range(5,0,-1): 
        stdout.write("\r%d" % i)
        stdout.flush()
        sleep(1)
    stdout.write("\nSTART!\n")

def new_game():
    name = input_validate("\nPLEASE TYPE YOUR NAME: ",is_int=False,range_list=None)
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
            print("\nCONGRATULATIONS! YOU HAVE JUST COMPLETED BRAINSTORM QUIZ!")
            print("THANK YOU FOR THE GAME!\n")
            print(f"{player.name} your final score is: {player.score}\n")
            player.game_time = time.time() - player.start_game_time
            print(f"{player.name} your game time is: ")
            print(time.strftime("%H:%M:%S\n", time.gmtime(player.game_time)))
            # TODO:score board implementation
            break
        print("---------------------------------------------------------------")
        print(f"\nQUESTION NO. {question_number}:")
        next_game_question.print_question()
        if player.lifeline_qty >= 1:
            print(
                f"YOU HAVE {player.lifeline_qty} LIFELINE{'' if player.lifeline_qty == 1 else 'S'}"
            )
        
        answer = input_validate("\nYOUR ANSWER IS: ",is_int=False,range_list=["a","b","c","d","H"])

        if answer == "H":
            if player.lifeline_qty:
                player.lifeline_qty -= 1
                next_game_question.lifeline()
            if player.lifeline_qty == 0:
                print("OUCH! YOU DON'T HAVE ANY LIFELINES!")
            answer = input_validate("\nYOUR ANSWER IS: ",is_int=False,range_list=["a","b","c","d"])
        if next_game_question.is_answer_correct(answer):
            question_number += 1
            print("\nGREAT! CORRECT ANSWER!\n")
            player.score += 10
            print(f"AWSOME! YOU HAVE {player.score} POINTS!")
            continue
        else:
            print("\nOH NO! INCORRECT ANSWER!\n")
            print("GAME OVER!\n")
            break


def best_scores():
    print("Option 'Best Scores'")


def manage_menu_options():
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
