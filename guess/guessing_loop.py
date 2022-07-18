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
    """A class for selecting secrets and clues, 
    and tracking the guessing loop state.
    """
    round_num = 1
    current_secret = ""
    guesses_used = 0
    guesses_remaining = 3
    is_running = False

    def quit_game(self):
        """Print a goodbye message, show final stats, and quit the game."""
        system("clear")
        gamehost.goodbye(player1.get("games_played"))
        if player1.get("games_played") > 0:
            player1.show_player_stats()
        sys.exit(0)

    def get_secret(self, category=menu_categories.get_selection()):
        """Randomly choose a secret matching the category."""
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

    def get_clue(self, guess: str, category=menu_categories.get_selection(),
                secret=current_secret, difficulty="hard"):
        """Randomly choose a clue for the chosen secret."""
        if category == "numbers":
            if guess:
                if int(guess) > int(secret):
                    higher_or_lower = "less"
                else:
                    higher_or_lower = "greater"
                clue = f"The secret number is {higher_or_lower} than {guess}."
            else:
                if int(secret) <= 5:
                    clue = (f"The secret number is less than "
                            f"{random.randint(int(secret)+1, 10)}.")
                else:
                    clue = (f"The secret number is greater than "
                            f"{random.randint(1, int(secret)-1)}.")
            return clue
        else:
            clue = dict_secrets[category][secret].get_clue(difficulty)
        return clue

    def use_guess(self):
        """Decrement guesses remaining and increment 
        guesses used after each guess input.
        """
        self.guesses_used += 1
        self.guesses_remaining -= 1
        return self.guesses_remaining

    def start(self, category=menu_categories.get_selection()):
        """Start the main guessing loop."""
        # Set user guess variable and select a random secret from category
        guess = ""
        secret = self.get_secret(category)
        guesses_remaining = self.guesses_remaining
        guesses_used = self.guesses_used
        difficulty = "hard"

        # Start guessing loop
        while guess != secret and guesses_remaining > 0:
            # Present a clue to the user and take input
            clue = self.get_clue(guess, category, secret, difficulty)
            gamehost.give_clue(clue, guesses_remaining)
            guess = input("Enter you guess: ").lower()
            if guess == "quit":
                self.quit_game()
            # Check for correct input in word categories
            if category != "numbers" and guess != "quit":
                while (guess.replace(" ", "").isalpha() == False
                        or len(guess) < 3
                        and guess != "quit"):
                    if guess.replace(" ", "").isalpha() == False:
                        guess = (input(f"\n{category.title()} secrets "
                                        "don't include numbers or symbols!"
                                        "\nTry guessing a word: "
                                        ).lower())
                    else:
                        guess = (input("\nYour guess must be three or more "
                                        "letters!"
                                        "\nTry another guess: "
                                        ).lower())
            if guess == "quit":
                self.quit_game()
            # Check for non-numeric or out of range input in 'Numbers'
            elif category == "numbers" and guess != "quit":
                while (guess.isnumeric() == False and guess != "quit"):
                    guess = input("\nThe secret is a positive integer!"
                                "\nEnter a number from 1 to 10 as your "
                                "guess: ")
                if guess == "quit":
                    self.quit_game()
                elif int(guess) < 1 or int(guess) > 10:
                    guess = (input(f"\nThat number's not in the right range!"
                                    "\nEnter a number from 1 to 10 as your "
                                    "guess: ").lower())

            # Update remaining and used guesses and round number
            guesses_remaining = self.use_guess()
            guesses_used = self.guesses_used
            self.round_num += 1
            player1.increment("guesses_total")

            # Give feedback after each guess
            # Win (end the loop if the guess matches the secret)
            if guess == secret:
                gamehost.congratulate(guess, guesses_used)
                player1.increment("games_won")
            # Miss (give feedback, encouragement, and another clue)
            elif guess != secret and guesses_remaining > 0:
                if guesses_remaining == 2:
                    difficulty = "medium"
                elif guesses_remaining == 1:
                    difficulty = "easy"
                # Check for a close or partial match
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
                # Check if player wants to know the secret
                reveal_secret = gamehost.give_choice(
                    "Should I tell you the secret")
                if reveal_secret == True and reveal_secret != "quit":
                    print(
                        f"\nThe secret was {secret.title()}! "
                        "do the clues make sense now?")
                # Check for quit attempt at the end of round prompt.
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
