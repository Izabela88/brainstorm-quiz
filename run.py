from player import Player
from questions import Questions, load_from_file


def handle_menu():
    menu = {
        1: "New Game",
        2: "Best Scores",
        3: "Exit",
    }
    for key, value in menu.items():
        print(f"{key} - {value}")
    return int(input("Enter your choice: "))


def start_game_menu():

    user_input = str(input("TYPE S TO START BRAINSTORM QUIZ: ")).lower()

    if user_input == "s":
        questions = Questions(10)
        questions.draw_questions()
        return questions


def new_game():
    name = str(input("What is your name?  "))
    player = Player(name)
    print(f"\nHello {player.name}, welcome to BRAINSTORM QUIZ!")
    player.pick_game_level()
    questions = start_game_menu()
    question_number = 1
    while True:
        next_game_question = questions.next_question()
        print(f"\nQUESTION NO {question_number}:")
        next_game_question.print_question()
        print(f"\nYou have {player.lifeline_qty} lifeline{'' if player.lifeline_qty == 1 else 's'}.")
        answer = input("Please type your answer:")
        if answer == "h":
            if player.lifeline_qty:
                player.lifeline_qty -= 1
                next_game_question.lifeline()
            else:
                print("You have no lifelines")   
            answer = input("Please type your answer:")
        if next_game_question.is_answer_correct(answer):
            question_number += 1

            print("\nGreat! Correct answer!\n")
            continue
        else:
            print("\nOh no! Incorrect answer!\n")
            print("GAME OVER!\n")
            break


def best_scores():
    print("Option 'Best Scores'")


def manage_menu_options():
    print("\nMENU:")
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
