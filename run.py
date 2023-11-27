# Import words and randomize
import random
from words import word_list_easy, word_list_medium, word_list_hard


# Function to display the Hangman based on the number of attempts
def display_hangman(attempts):
    # Hangman stages for each incorrect guess
    hangman_stages = [
        # Final hangman state - all limbs
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        # One leg, two arms, torso, and head
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        # Two arms, torso, and head
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        """,
        # One arm, torso, and head
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        # Torso and head
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        # Head
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        # Initial empty state
        """
           ------
           |    |
           |
           |
           |
           |
        """,
    ]
    return hangman_stages[attempts]


# Function to get a word based on difficulty
def get_word(difficulty):
    if difficulty == "easy":
        return random.choice(word_list_easy)
    elif difficulty == "medium":
        return random.choice(word_list_medium)
    elif difficulty == "hard":
        return random.choice(word_list_hard)
    else:
        return None


# Main function to play Hangman
def play():
    # User selection of difficulty
    difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()
    word = get_word(difficulty)
    # Check validity of entry
    if word is None:
        print("Invalid entry. Exiting the game.")
        return
    # Initialize variables
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = set()
    attempts = 6
    # Display inital hangman and status of the word
    print("Let's play Hangman!")
    print(display_hangman(attempts))
    print(word_completion + "\n")
    # Main game loop
    while not guessed and attempts > 0:
        # Get user input and guess
        guess = input("Guess a letter: ").upper()
        # Validate user input
        if len(guess) == 1 and guess.isalpha():
            # Check if letter has already been guessed
            if guess in guessed_letters:
                print("Letter has alrady been guessed", guess)
                # Incorrrect letter selection, add to set
            elif guess not in word:
                print(guess, "is not in the word")
                attempts -= 1
                guessed_letters.add(guess)
            else:
                # Correct guess, update word and add to set
                print("Great,", guess, "is correct!")
                guessed_letters.add(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                # Check if complete word has been guessed
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Not a valid entry. Please enter a single letter.")
        # Display Hangman and word status
        print(display_hangman(attempts))
        print(word_completion + "\n")
        # Display word result - succesfull and unsuccesful
    if guessed:
        print("Well done! You guessed correctly:", word)
    else:
        print("Sorry, you've run out of attempts. The correct word was:", word)


# Entry point of the game
if __name__ == "__main__":
    ready_to_play = input("Are you ready to play Hangman? (y/n): ").lower()

    if ready_to_play == "y":
        play()
    else:
        print("Ok, maybe next time. Bye for now!")
