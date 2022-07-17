from difflib import SequenceMatcher
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

    def quit_game(self):
        system("clear")
        gamehost.goodbye(player1.get("games_played"))
        if player1.get("games_played") > 0:
            player1.show_player_stats()
        sys.exit(0)

    def get_secret(self, category=menu_categories.get_selection()):
        if category == "quit":
            self.quit_game()
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
            if guess == "quit":
                self.quit_game()
            while category != "numbers" and len(guess) < 3:
                while guess.isnumeric():
                    guess = input(
                        f"\nThe game category is {category.title()} not Numbers!\nEnter another guess: ").lower()
                while len(guess) < 3 and not guess.isnumeric():
                    guess = input(
                        f"\nYou'll need to enter at least 3 letters...\nEnter a proper guess:  ").lower()
            while category == "numbers" and not guess.isnumeric():
                guess = input(
                    f"\nYou're trying to guess a positive integer, remember?\nEnter a number between 1 and 10 as your guess: ").lower()
            while category == "numbers" and int(guess) not in range(1, 11):
                guess = input(
                    f"\nThat number's not in the right range!\nEnter a number between 1 and 10 as your guess: ").lower()
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
                match = SequenceMatcher(
                    lambda x: x == " ", guess, secret).ratio()
                if match > 0.6 or guess in secret:
                    gamehost.encourage(guess, "partial", guesses_remaining)
                else:
                    gamehost.encourage(guess, "miss", guesses_remaining)
            # Loss (game ends if no guesses remining)
            else:
                gamehost.encourage(guess, "loss", guesses_remaining)
                player1.increment("games_lost")
                reveal_secret = gamehost.give_choice(
                    "Should I tell you the secret")
                if reveal_secret == True and reveal_secret != "quit":
                    print(
                        f"\nThe secret was {secret.title()}! do the clues make sense now?")
                else:
                    if reveal_secret != "quit":
                        print("\nI'm sure you'll get it eventually!")
                    else:
                        self.quit_game()

        # Update overall user stats at the end of the game
        player1.increment("games_played")
        player1.calc_avg_guesses()

        # Reset attributes for the next game
        self.round_num = 1
        self.guesses_remaining = 3
        self.guesses_used = 0


guessing_loop = GuessingLoop()