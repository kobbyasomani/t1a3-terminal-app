from dataclasses import dataclass
from menu import menu_categories
from secret import list_secrets
import random


@dataclass
class GuessingLoop():
    """A class for selecting secrets and clues, and tracking the guessing loop state"""
    round_num = 1
    secret = ""
    used_guesses = 0
    remaining_guesses = 3
    is_running = False

    def get_secret(self, category=menu_categories.selected_category):
        secret = random.choice(list_secrets[category]).get_answer()
        return secret

    # def start():
        # Select a 'secret' at random from the chosen category
        # secret = random.choice(list_secrets[menu_categories.selected_category])
        # print(secret.answer.title())

        # present a clue to the user and take input

        # update remaining and used guesses

        # decrement remaining guesses if the guess does not match the secret

        # give feedback after each guess

        # end the loop if the guess matches the secret

        # update overall user stats at the end of the guessing round

        # update menu at the end of the guessing round (show stats at the top)

# menu_categories.selected_category = "mythical creatures"
# guessing_loop()
