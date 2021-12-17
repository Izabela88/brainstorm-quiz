<h1 align="center">BRAINSTORM QUIZ GAME</h1>

[View the live project here](https://brainstorm-quiz-game.herokuapp.com/)

The goal of the Brainstorm Quiz is to become the Brainstorm Champion. To achieve this, the player must answer all questions.
The player can choose between two difficulty levels: Normal and Expert. 

After completing the game on a Normal level, the player receives the title "THE GREATEST CHAMPION IN THE EARTH!".
After completing the game on an Expert-level, the player receives the title "THE GREATEST CHAMPION IN THE WHOLE GALAXY".

The player scores are recorded on the scoreboard, so the player has the opportunity to check his score. Only the top 10 scores hit the scoreboard.


<h2 align="center"><img src="https://github.com/Izabela88/brainstorm-quiz/blob/main/media/main-menu.jpg"></h2>

## **Table of content**

- [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
  - [Scope](#scope)
    - [Aplication Flow Chart](#aplication-flow-chart)
- [Features](#features)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
- [Code Organisation](#code-organisation)
- [Data Validation](#data-validation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Bugs](#bugs)
- [Credits](#credits)
  - [Code](#code)
  - [Content](#content)
  - [Acknowledgements](#acknowledgements)

## USER EXPERIENCE

- ### USER STORIES

  - #### VISITOR GOALS

    - As the Visitor:

      1. I want to easily understand the main purpose of the game.
      2. I want to be able to easily navigate throughout the game options.
      3. I want to know the rules of the game.
      4. I want to be able to see the results of my game.
      5. I want to know clearly what the steps of the game are.
      6. I want to be able to play again.
      7. I want to be able exit game.

  
- ### DESIGN

  This game is displayed in the terminal, so the design options are minimal. However, I used an external library to add colours and emojis. Thanks to this, the game is legible and more player-friendly.

  - #### COLOR SCHEME

  Colors used: yellow, blue, purple, green and red.


- ### SCOPE

  - #### APLICATION FLOW CHART

  ![Flow chart](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/structure1.jpg)
  ![Flow chart](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/structure2.jpg)

## FEATURES


- #### MAIN MENU

- I want to easily understand the main purpose of the game.
- I want to know the rules of the game.
  
  - Contains the name of the game and basic information about the game's rules.
  - Information on how to start the game is provided at the bottom.
  
  ![Main Menu](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/main-menu.jpg)


- #### GAME MENU

- I want to be able to easily navigate throughout the game options.

  - Game menu is divided into three categories: New Game, Best Scores and Exit.
  - The player can choose the option by entering the assigned number.
  
  ![Game Menu](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/game-menu.jpg)


- #### SCOREBOARD

- I want to be able to see the results of my game.

  - Scoreboard contains the top ten game scores in two levels.
  
  ![Scoreboard](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/score-board.jpg)

  - An appropriate message appears when there are no results in the game yet.

  ![Scoreboard](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/score-board-no-results-msg.jpg)

  - The message is displayed if a player qualifies or does not qualify to the scoreboard.

  ![Scoreboard Message](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/score-board-not-msg.jpg)

  ![Scoreboard Message](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/score-board-yes-msg.jpg)
  

- #### NEW GAME

-  I want to know clearly what the steps of the game are.

  - To start a new game, the player must go through several steps:
    - Enter name.
    - Choose game level.
    - Type 's' to start game.
  
  ![Enter Name](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/enter-name.jpg)

  ![Choose Game Level](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/game-level.jpg)

  ![Start Game](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/start-game.jpg)


- #### GAME LEVELS

- I want to know the rules of the game.

  - The game has two difficulty levels: Normal and Expert.

    - Level Normal:
        - Contains 10 questions.
        - Contains 2 Lifelines.
        - After answering all the questions, the player receives the title: THE GREATEST CHAMPION IN THE EARTH.

    - When a player selects a Normal difficulty level, a message will appear explaining the rules of the game for that difficulty:

    ![Normal level](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/normal-lvl-msg.jpg)
    
    
    - Level Expert:
        - Contains 20 questions.
        - Contains 4 Lifelines.
        - After answering all the questions, the player receives the title: THE GREATEST CHAMPION IN THE WHOLE GALAXY.

    - When a player selects an Expert difficulty level, a message will appear explaining the rules of the game for that difficulty:

    ![Expert level](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/expert-lvl-msg.jpg)

    - After completing the quiz, a message will appear stating that the player has earned the title based on their game level.

    - Normal level:

    ![Normal Level](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/complete-game.jpg)

    - Expert level:

    ![Expert Level](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/complete-game-exp.jpg)


- #### BEGIN GAME

  - After pressing the letter 's', the message "Let's Begin" appears.
  - A countdown of five seconds begins until the game begins.

  ![Begin Game](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/begin-game.jpg)


- #### LIFELINES

  - The player has the option to use Lifeline during the game.
  - Two wrong ones are removed from the four available answers when a player uses Lifeline.
  - The player always know How many lifelines are left.

  ![Lifeline](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/use-lifeline.jpg)

  - No lifelines

    ![No lifelines](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/use-lifeline-last-time.jpg)


- #### QUESTIONS AND ANSWERS

  - The questions are numbered so that the player knows where he is in the game.
  - The questions are highlighted in a different colour to make them legible.
  - To answer a question, the player should enter the appropriate letter.
  
  ![Questions](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/question.jpg)

  - After the player answers, a message appears depending on whether the player answered correctly or not.
  - For each correct answer, the player gets 10 points. The wrong answer ends the game.
  - At the end of the game, information about the final score and time is displayed.

  ![Good answer](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/correct-answer.jpg)

  ![Bad answer](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/incorrect-answer.jpg)

  

- #### PLAY AGAIN

- I want to be able to play again.

  - The player has the option to play again.
  - A query appears on the screen.
  - To play again, play must enter 'y'. If he does not want to play again must select 'n'.

  ![Play again](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/play-again-y-msg.jpg)


- #### FINISH GAME

- I want to be able exit game.

  - To end the game, the player can select the number  '3' from the game menu or enter the letter 'n' when is asked if he wants to play again.
  - Some goodbye messages appear when the game is over.

  ![Exit msg](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/exit-msg.jpg)
  ![Exit msg](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/no-play-again-msg.jpg)



## TECHNOLOGIES USED

### LANGUAGES USED

- [Python 3.8.2](https://en.wikipedia.org/wiki/Python_(programming_language))


### FRAMEWORKS AND LIBRARIES USED

1. [Rich:](https://rich.readthedocs.io/en/latest/introduction.html)
   - Rich is a Python library for writing rich text (with color and style) to the terminal, and for displaying advanced content such as tables, markdown, and syntax highlighted code.
1. [Black:](https://pypi.org/project/black/)
   - Used for format the code.
1. [Flake8:](https://flake8.pycqa.org/en/latest/)
   - Used for checking if code is correct.


## CODE ORGANISATION

- As the code grew, the I decided to split all Python code for parts:

  - run.py: 
  
    - Contains the main code relating to the entire logic of the game.

  - questions.py:

    - There are two classes that contain the code related to the questions.

    - Class Questions store game questions and question numbers, and it also has a method that gets the next question and shows its number and method, which draw unique questions from JSON file.

    - Class Question store single question, answers and correct answers. It also has methods which: print question, a check answers correct and lifeline method which removes two incorrect answers and
        call another method to print again question with only two answers.

  - score_board.py: 
  
    - There is a Scoreboard class that contains the code related to the scoreboard. It includes methods that save player score, check if score is qualified to the scoreboard and display best scores.

    - The class also contains three static methods which get the best scores, save scores to JSON file and sort scores.

  - player.py: 
  
    - There is a Player class that stores player name, score, game level, lifeline quantity and game time.

    - It also contains methods which: display final results, display type of champion title, display lifelines quantity and trigger question lifeline logic, handles player game level choice and display game level info panel.

  - utility.py: 
  
    - Contains a function that validates inputs and function which counts time to start the game.

  - messages.py: 
  
    - Contains long sets of strings moved into this file to make the code more readable

- The questions are taken from the local JSON file.
- The player's score is saved to a JSON file. 


## DATA VALIDATION

  - Input validation:

    - No blank fields.

    ![Blank](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/validation/blank-field.jpg)

    - Right input.

    ![Right input](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/validation/integer.jpg)

    ![Right input](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/validation/valid-answer.jpg)

    ![Right input](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/validation/start-game.jpg)

    ![Right input](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/validation/enter.jpg)

    - Too few characters.

    ![Too few](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/validation/too-low-characters.jpg)

    - Too many characters.

    ![Too many](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/validation/too-many-characters.jpg)
    
    - Play again.

    ![play again](https://github.com/Izabela88/brainstorm-quiz/blob/main/media/validation/play-again.jpg)
    
      

## TESTING

I have manually tested this project by doing the following:

  - Passed the code through a PEP8 linter and confirmed there are no issues.
  [PEP8:](http://pep8online.com/)

  - Giving invalid input.


## DEPLOYMENT

This project was deployed using Code institute's mock terminal for Heroku.

  - Steps for deployment:
    - Fork or clone this repository
    - create a new Heroku app
    - Set the buildpacks to 'Python' and 'NodeJS' in that order
    - Link the Heroku app to the respository
    - Click on 'Deploy'


### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Izabela88/brainstorm-quiz)
2. At the top of the Repository (not top of page), just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Izabela88/brainstorm-quiz)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

## BUGS

No bugs remaining.


## CREDITS

  - Code Institute for the deploytment terminal.


### CODE

While coding for some problems and inspirations with Python code, I looked for answers on websites:

- [W3School](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)


### CONTENT

- All content was written by the developer.

### ACKNOWLEDGEMENTS

- My Mentor for continuous helpful feedback.
- Tobiasz Chodarewicz for review my code and helpful sugestions.
