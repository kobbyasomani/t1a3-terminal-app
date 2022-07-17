from os import system
import sys
from dataclasses import dataclass
from menu import menu_categories
from secret import dict_secrets
from gamehost import gamehost
from player import player1
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
        if category == "quit":
            gamehost.goodbye(player1.get("games_played"))
            if player1.get("games_played") > 0:
                player1.show_player_stats()
            sys.exit(0)
        elif category == "numbers":
            secret = str(random.randint(1, 10))
            return secret
        else:
            keys = []
            for key, secret in dict_secrets[category].items():
                keys.append(key)
            secret = random.choice(keys)
            self.current_secret = secret
            return secret

    def get_clue(self, guess: str, category=menu_categories.get_selection(), secret=current_secret, difficulty="hard"):
        if category == "numbers":
            if guess:
                if int(guess) > int(secret):
                    higher_or_lower = "less"
                else:
                    higher_or_lower = "greater"
                clue = f"The secret number is {higher_or_lower} than {guess}."
            else:
                if int(secret) <= 5:
                    clue = f"The secret number is less than {random.randint(int(secret)+1, 10)}."
                else:
                    clue = f"The secret number is greater than {random.randint(1, int(secret)-1)}."
            return clue
        else:
            clue = dict_secrets[category][secret].get_clue(difficulty)
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
            clue = self.get_clue(guess, category, secret, difficulty)
            gamehost.give_clue(clue, guesses_remaining)
            guess = input("Enter you guess: ").lower()

            # update remaining and used guesses and round number
            guesses_remaining = self.use_guess()
            guesses_used = self.guesses_used
            self.round_num += 1
            player1.increment("guesses_total")

            # Give feedback after each guess
            # Win (end the loop if the guess matches the secret)
            if guess == secret:
                gamehost.congratulate(guess, guesses_used)
                player1.increment("games_won")
            # Miss (give feedback and another clue)
            elif guess != secret and guesses_remaining > 0:
                if guesses_remaining == 2:
                    difficulty = "medium"
                elif guesses_remaining == 1:
                    difficulty = "easy"
                gamehost.encourage(guess, "miss", guesses_remaining)
            # Loss (game ends if no guesses remining)
            else:
                gamehost.encourage(guess, "loss", guesses_remaining)
                player1.increment("games_lost")
                if gamehost.give_choice("Should I tell you the secret"):
                    print(
                        f"\nThe secret was {secret.title()}! do the clues make sense now?")
                else:
                    print("\nI'm sure you'll get it eventually!")

        # Update overall user stats at the end of the game
        player1.increment("games_played")
        player1.calc_avg_guesses()

        # Reset attributes for the next game
        self.round_num = 1
        self.guesses_remaining = 3
        self.guesses_used = 0


guessing_loop = GuessingLoop()
