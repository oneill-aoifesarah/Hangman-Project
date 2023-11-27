# Import and enable random function
import random
from words import word_list_easy, word_list_medium, word_list_hard


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
    print("Rules: Suggest letters to guess the word.")