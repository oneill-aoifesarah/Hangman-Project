# Import and enable random function
import random
from words import word_list_easy, word_list_medium, word_list_hard

# Display Hangman
def display_hangman(attempts):
    hangman_stages = [
        # Initial empty state
        """
           ------
           |    |
           |
           |
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
        # Torso and head
        """
           ------
           |    |
           |    O
           |    |
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
        # Two arms, torso, and head
        """
           ------
           |    |
           |    O
           |   /|\\
           |
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
        # Final hangman state - all limbs
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """
    ]
    return hangman_stages[attempts]

# Function to get a word based on difficulty
def get_word(difficulty):
    if difficulty == 'easy':
        return random.choice(word_list_easy)
    elif difficulty == 'medium':
        return random.choice(word_list_medium)
    elif difficulty == 'hard':
        return random.choice(word_list_hard)
    else:
        return None

# Function to play Hangman
def play_hangman():
    attempts = 6
    print("Welcome to Hangman!")
    username = input("Enter your name: ")
    print(f"Hi, {username}. Let's play Hangman.")

    # Ask if the player is ready to play
    ready_to_play = input("Are you ready to play? (y/n): ").lower()

    if ready_to_play != 'y':
        print("Ok, maybe next time. Bye for now!")
        return

    # Display Hangman rules
    print("Rules: Add letters to guess the word in just six attempts")

    # Selection of difficulty level
    difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()
    word = get_word(difficulty)

    if word is None:
        print("Invalid entry. Exiting the game.")
        return

    # Set of guessed letters
    guessed_letters = set()

    # Main gameplay loop
    while attempts > 0:
        # Display the current state of the hangman and the guessed word
        print(display_hangman(attempts))
        guessed_word = "".join([letter if letter in guessed_letters else '_' for letter in word])
        print(f"Current word: {guessed_word}")

        # Get the user's guess
        guess = input("Add a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)

        # Check if the guessed letter is not in the word
        if guess not in word:
            print("Letter is not in the word")
            attempts -= 1

        # Check if the user has guessed all the letters in the word
        if set(guessed_letters) == set(word):
            print("Congratulations! You guessed the word!")
            break

        # Game over: Display the correct word
        print("Game over. The word was:", word)

        # Ask if the user wants to play again
        play_again = input("Would you like to play again? (y/n): ").lower()

        if play_again != 'y':
            print("Thanks for playing. See you soon!")
            break
