from dataclasses import dataclass
from menu import menu_categories
from secret import list_secrets
import random


@dataclass
class GuessingLoop():
    """A class for selecting secrets and clues, and tracking the guessing loop state"""
    round_num = 1
    current_secret = ""
    used_guesses = 0
    remaining_guesses = 3
    is_running = False

    def get_secret(self, category=menu_categories.get_selection()):
        keys = []
        for key, secret in list_secrets[category].items():
            keys.append(key)
        secret = random.choice(keys)
        self.current_secret = secret
        return secret

    def get_clue(self, category=menu_categories.get_selection(), secret=current_secret, difficulty="hard"):
        clue = list_secrets[category][secret].get_clue(difficulty)
        return clue

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


guessing_loop = GuessingLoop()
