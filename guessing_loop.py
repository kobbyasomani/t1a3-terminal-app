from dataclasses import dataclass
from menu import menu_categories
from secret import list_secrets
from gamehost import gamehost
import random


@dataclass
class GuessingLoop():
    """A class for selecting secrets and clues, and tracking the guessing loop state"""
    round_num = 1
    current_secret = ""
    guesses_used = 0
    guesses_remaining = 3
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

    def use_guess(self):
        self.guesses_used += 1
        self.guesses_remaining -= 1
        return self.guesses_remaining

    def start(self, category=menu_categories.get_selection()):
        # Initialise user guess variable and select a random secret from category
        guess = ""
        secret = self.get_secret(category)
        guesses_remaining = self.guesses_remaining
        guesses_used = self.guesses_used
        difficulty = "hard"

        # Start guessing loop
        while guess != secret and guesses_remaining > 0:
            # present a clue to the user and take input
            clue = self.get_clue(category, secret, difficulty)
            gamehost.give_clue(clue, guesses_remaining)
            guess = input("Enter you guess: ").lower()

            # update remaining and used guesses
            guesses_remaining = self.use_guess()

            # Give feedback after each guess
            # Win
            if guess == secret:
                gamehost.congratulate(guesses_used)
            # Miss
            elif guess != secret and guesses_remaining > 0:
                if guesses_remaining == 2:
                    difficulty = "medium"
                elif guesses_remaining == 1:
                    difficulty = "easy"
                gamehost.encourage(guess, "miss", guesses_remaining)
            # Loss
            else:
                gamehost.encourage(guess, "loss", guesses_remaining)

        # end the loop if the guess matches the secret

        # update overall user stats at the end of the guessing round

        # update menu at the end of the guessing round (show stats at the top)


guessing_loop = GuessingLoop()
