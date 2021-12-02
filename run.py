from player import Player
from questions import Questions
# from utility import input_validate(input_text, is_int=False, range_list=None)


def handle_menu():
    menu = {
        1: "New Game",
        2: "Best Scores",
        3: "Exit",
    }
    for key, value in menu.items():
        print(f"{key} - {value}")
    
    return int(input("Enter your choice: "))


def start_game_menu(player):
    while True:
        try:
            user_input = input("TYPE S TO START BRAINSTORM QUIZ: ").lower()
            if user_input != "s":
                raise ValueError
        except ValueError:
            print("Please type right letter")
            continue
        if player.game_level == 1:
            questions = Questions(10)
        else:
            questions = Questions(20)
        questions.draw_questions()
        return questions


def new_game():
    name = input("\nWhat is your name?  ")
    player = Player(name)
    print(f"\nHello {player.name}, welcome to BRAINSTORM QUIZ!")
    player.pick_game_level()
    questions = start_game_menu(player)
    question_number = 1
    while True:
        try:
            next_game_question = questions.next_question()
        except IndexError:
            print("\nCONGRATULATIONS! YOU HAVE JUST COMPLETED BRAINSTORM QUIZ!")
            print("THANK YOU FOR THE GAME!\n")
            print(f"YOUR FINAL SCORE IS: {player.score}\n")
            # TODO:score board implementation
            break
        print("----------------------------------------------")
        print(f"\nQUESTION NO {question_number}:")
        next_game_question.print_question()
        print(
            f"YOU HAVE {player.lifeline_qty} LIFELINE{'' if player.lifeline_qty == 1 else 'S'}"
        )
        answer = input("\nYOUR ANSWER IS:").lower()

        if answer == "h":
            if player.lifeline_qty:
                player.lifeline_qty -= 1
                next_game_question.lifeline()
            else:
                print("OUCH! YOU HAVE NO LIFELINES!")
            answer = input("YOUR ANSWER IS:").lower()
        if next_game_question.is_answer_correct(answer):
            question_number += 1
            print("\nGREAT! CORRECT ANSWER!\n")
            player.score += 10
            print(f"YOU HAVE {player.score} POINTS ")
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
        try:
            option = int(handle_menu())
        except ValueError:
            print("Please enter a valid number. From 1 to 3.")
            continue
        if option == 1:
            new_game()
        elif option == 2:
            best_scores()
        elif option == 3:
            break
        else:
            print("Please enter a number between 1 and 3.")

    print("Thank you for the Game!")


if __name__ == "__main__":
    manage_menu_options()
