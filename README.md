Guess the Number Game
Overview
Guess the Number is a Python-based game that challenges players to guess a randomly selected number within a specified range. The game offers three difficulty levels: Easy, Medium, and Hard, each with different ranges and maximum attempts. Players are given feedback on their guesses (whether the guess is too high or too low) and hints (whether the number is odd or even). The game also tracks high scores based on the fewest attempts and fastest time taken to guess the number.

Features
Difficulty Levels: Three levels — Easy, Medium, and Hard.

Input Validation: Ensures players input valid numbers within the specified range.

High Scores: Tracks the fewest attempts and fastest time for each difficulty.

Hints: Provides a hint about whether the number is odd or even after every 3 incorrect guesses.

Replay Option: Players can choose to play again after completing a game.

Difficulty Levels
Easy: Number range between 1-50, Maximum attempts: 10.

Medium: Number range between 1-100, Maximum attempts: 12.

Hard: Number range between 1-200, Maximum attempts: 15.

The game displays the high score for each difficulty based on the best number of attempts and time.

Game Flow
Choose a Difficulty: Select your desired difficulty level (easy/medium/hard).

Guess the Number: The system will select a random number within the range for the chosen difficulty. You have a set number of attempts to guess the correct number.

Feedback: After each guess, the game will tell you whether your guess is too high, too low, or correct.

Hints: After every three incorrect guesses, a hint will be provided — whether the target number is odd or even.

High Scores: After you guess the number correctly or run out of attempts, the game will show the high scores for each difficulty level.

Replay: You can choose to play again or exit the game.

Installation
Prerequisites
Python 3.x is required to run the game.

Steps to Install
Clone the Repository

Open your terminal or command prompt and run the following command to clone the repository:

bash
Copy
git clone https://github.com/Sohailqureshi9/guess_game_project.git
Navigate to the Project Directory

Change to the directory of the project:

bash
Copy
cd guess_game_project
Run the Game

Run the game by executing the following command:

bash
Copy
python guess_game.py
If your system uses python3 instead of python, use the following command:

bash
Copy
python3 guess_game.py
How to Play
Start the Game: Once you run the game, you will be prompted to choose a difficulty level (easy, medium, or hard).

Enter Your Guess: After selecting the difficulty, the game will ask you to enter a guess. The number you need to guess will be hidden, and you will receive feedback after each guess (too high, too low).

Hints: Every 3 wrong guesses, the game will provide a hint whether the target number is odd or even.

Guess Correctly: When you guess the correct number, the game will display the number of attempts you made and the time it took.

High Scores: After finishing the game, you will see the current high scores for each difficulty level.

Replay Option: At the end, the game will ask if you want to play again. You can choose "yes" to play again or "no" to exit.

Example Gameplay
vbnet
Copy
Welcome to 'Guess the Number'!
Choose a difficulty (easy/medium/hard): easy

I've selected a number between 1 and 50. You have 10 attempts to guess it.

Enter your guess (1-50): 25
Your guess is too high. Try a lower number.

Enter your guess (1-50): 10
Your guess is too low. Try a higher number.

Enter your guess (1-50): 20
Congratulations! You've guessed the number 20 correctly in 3 attempts and 5.67 seconds.

High Scores:
Easy Difficulty: 3 attempts, 5.67 seconds
Medium Difficulty: inf attempts, inf seconds
Hard Difficulty: inf attempts, inf seconds

Do you want to play again? (yes/no): no
Thanks for playing! Goodbye.
Code Explanation
Main Game Logic (guess_the_number())
The main game loop starts by prompting the player to choose a difficulty level. Based on the selected difficulty, the number range and maximum attempts are set. The game then generates a random number in that range and allows the player to input guesses until they either guess the correct number or run out of attempts.

Input Validation (get_valid_guess(min_value, max_value))
This function ensures that the player inputs a valid integer within the range specified by the difficulty level. If an invalid input is provided (e.g., a non-integer or out-of-range number), the function will prompt the user to try again.

High Score Tracking (show_high_scores())
After a game finishes, the high scores for each difficulty level are displayed. The high score is tracked based on the number of attempts and the time taken to guess the correct number. If the player has a new high score, it is updated in the global high_scores dictionary.

Hints (if attempts % 3 == 0)
Every three wrong guesses, the game provides a hint about whether the target number is odd or even. This helps the player narrow down the possibilities.

High Score Tracking
The high scores for each difficulty level are stored globally and updated whenever a new high score is achieved. The scores are tracked for:

Attempts: The fewest number of guesses to correctly guess the number.

Time: The shortest amount of time taken to guess the number.

Example High Score Display
yaml
Copy
High Scores:
Easy Difficulty: 3 attempts, 5.67 seconds
Medium Difficulty: 12 attempts, 20.45 seconds
Hard Difficulty: 15 attempts, 30.21 seconds
Contributing
We welcome contributions to improve the game! If you find a bug or would like to add a new feature, feel free to fork the repository and submit a pull request.

Steps to Contribute
Fork the repository.

Clone your forked repository.

Create a new branch (git checkout -b feature-name).

Make your changes.

Commit your changes (git commit -am 'Add feature').

Push your branch (git push origin feature-name).

Open a pull request.

License
This project is licensed under the MIT License.

