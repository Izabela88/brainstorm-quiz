from player import Player


def show_menu():
    menu = {
        1: "New Game",
        2: "Best Scores",
        3: "Exit",
    }
    for key, value in menu.items():
        print(f"{key} -- {value}")


def new_game():
    name = str(input("What is your name?  "))
    player = Player(name)

    print(f"\nHello {player.name}, welcome to BRAINSTORM QUIZ!") 
    print("You will be presented with 10 questions.")
    print("Enter the appropriate number to answer the question")
    print("Good luck!")
    
    while True:
        break


def best_scores():
    print("Option 'Best Scores'")


def manage_options():
    print("MENU:")
    while True:
        show_menu()
        option = ""
        try:
            option = int(input("Enter your choice: "))
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
    manage_options()
