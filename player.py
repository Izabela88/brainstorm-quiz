from time import time
from utility import input_validate
import datetime



class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
        self.game_level = None
        self.lifeline_qty = 0
        self.start_game_time = None
        self.game_time = None


    def pick_game_level(self):
        print("\nPlease choose a game level: \n")
        level_menu = {
            1: "NORMAL",
            2: "EXPERT",
        }
        for key, value in level_menu.items():
            print(f"{key} - {value}")

        while True:
            level = input_validate("\nENTER YOUR CHOICE: ",is_int=True,range_list=[1,2])
            if level == 1:
                questions_qty = 10
                self.lifeline_qty = 2
            else:
                questions_qty = 20
                self.lifeline_qty = 4
            self.game_level = level

            print(f"\nYou picked level: '{level_menu[level]}'")
            print(f"\nYou will be presented with {questions_qty} questions.")
            print("Enter the appropriate number to answer the question.")
            print(
                f"In case of trouble, you can use {self.lifeline_qty} lifelines to remove two wrong answers."
            )
            print("To use your lifeline press 'H'.")
            print("GOOD LUCK!\n")
            return level
        
        
