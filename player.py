class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
        self.game_level = None

    def pick_game_level(self):
        level_menu = {
            1: "Normal",
            2: "Expert",
            3: "Exit",
        }
        for key, value in level_menu.items():
            print(f"{key} - {value}")
        while True:
            try:
                level = int(input("Enter your choice: "))
                if level > 3 or level < 1:
                    raise ValueError
                if level == 3:
                    break
                self.game_level = level
                print(f"\nYou picked level {level_menu[level]}")
                return level
            except ValueError:
                print("Please enter a valid number from 1 to 2.")
