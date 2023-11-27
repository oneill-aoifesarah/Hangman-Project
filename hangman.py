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
