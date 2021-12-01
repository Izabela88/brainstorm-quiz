class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
        self.game_level = None
        self.lifeline_qty = 0

    def pick_game_level(self):
        print("\nPlease choose a game level:")
        level_menu = {
            1: "NORMAL",
            2: "EXPERT",
        }
        for key, value in level_menu.items():
            print(f"{key} - {value}")

        while True:
            try:
                level = int(input("Enter your choice: "))
                if level == 1:
                    questions_qty = 10
                    self.lifeline_qty = 2
                elif level == 2:
                    questions_qty = 20
                    self.lifeline_qty = 4
                else:
                    print("Please enter a valid number from 1 to 2.")
                self.game_level = level

                print(f"\nYou picked level {level_menu[level]}")
                print(f"\nYou will be presented with {questions_qty} questions.")
                print("Enter the appropriate number to answer the question.")
                print(
                    f"In case of trouble, you can use {self.lifeline_qty} lifelines to remove two wrong answers."
                )
                print("To use your lifeline press 'h'.")
                print("GOOD LUCK!\n")
                return level
            except ValueError:
                print("Please enter a valid number from 1 to 2.")
