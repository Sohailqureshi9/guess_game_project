import random
import time

# Store the high scores globally
high_scores = {
    'easy': {'attempts': float('inf'), 'time': float('inf')},
    'medium': {'attempts': float('inf'), 'time': float('inf')},
    'hard': {'attempts': float('inf'), 'time': float('inf')}
}

def get_valid_guess(min_value, max_value):
   
    while True:
        try:
            guess = int(input(f"Enter your guess ({min_value}-{max_value}): "))
            if min_value <= guess <= max_value:
                return guess
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def show_high_scores():
  
    print("\nHigh Scores:")
    for difficulty, score in high_scores.items():
        print(f"{difficulty.capitalize()} Difficulty: {score['attempts']} attempts, {score['time']} seconds")

def guess_the_number():
    """
    Main game loop for 'Guess the Number' game with difficulty levels, high scores, and timing.
    """
    # Select difficulty
    print("Welcome to 'Guess the Number'!")
    difficulty = input("Choose a difficulty (easy/medium/hard): ").strip().lower()
    
    # Set number range and max attempts based on difficulty
    if difficulty == "easy":
        min_value, max_value = 1, 50
        max_attempts = 10
    elif difficulty == "hard":
        min_value, max_value = 1, 200
        max_attempts = 15
    else:
        min_value, max_value = 1, 100
        max_attempts = 12

    target_number = random.randint(min_value, max_value)
    attempts = 0
    start_time = time.time()  # Track start time

    print(f"\nI've selected a number between {min_value} and {max_value}. You have {max_attempts} attempts to guess it.")
    
    # Game loop
    while attempts < max_attempts:
        user_guess = get_valid_guess(min_value, max_value)
        attempts += 1

        if user_guess > target_number:
            print("Your guess is too high. Try a lower number.")
        elif user_guess < target_number:
            print("Your guess is too low. Try a higher number.")
        else:
            end_time = time.time()  # Track end time
            time_taken = round(end_time - start_time, 2)
            print(f"\nCongratulations! You've guessed the number {target_number} correctly in {attempts} attempts and {time_taken} seconds.")
            
            # Update high scores if necessary
            if attempts < high_scores[difficulty]['attempts']:
                high_scores[difficulty]['attempts'] = attempts
                high_scores[difficulty]['time'] = time_taken
            
            break  # Exit the loop if the user guesses correctly

        # Provide a hint every 3 wrong guesses
        if attempts % 3 == 0:
            if target_number % 2 == 0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")
        
        if attempts == max_attempts:
            print(f"\nSorry, you've used all {max_attempts} attempts. The correct number was {target_number}.")
            break

    # Show stats and ask for replay
    show_high_scores()

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        guess_the_number()
    else:
        print("Thanks for playing! Goodbye.")

# Start the game
if __name__ == "__main__":
    guess_the_number()
