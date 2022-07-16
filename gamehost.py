from player import player1
import random


class GameHost:
    """A class for displaying user feedback messages"""

    def __init__(self):
        self.feedback = ""

    def give_feedback(self):
        print(f"\n{self.feedback}")

    def welcome(self):
        if player1.games_played == 0:
            self.feedback = "\nWelcome to The Guessing Game!\nHave some fun and test your wits by guessing a secret number, word, or phrase within three guesses.\nPlease choose from one of the categories below by entering the name or number.\n"
        self.give_feedback()

    def give_clue(self, clue, guesses_remaining):
        if guesses_remaining == 3:
            self.feedback = f"And we're off! Can you guess it in one go?\nHere's your first clue: {clue}"
            self.give_feedback()

    def get_prefix(self, guess_type):
        response_prefixes = {
            "win": [
                "Amazing!",
                "Not bad at all!",
                "Well done!",
                "Not too shabby!"
            ],
            "miss": [
                "Not quite!",
                "That's not it... have another think about it.",
                "Nope!",
                "You could be close...",
                "Hmm... maybe another clue will help.",
                "Sorry, that's a miss!",
                "I'm afraid not..."
            ],
            "loss": [
                "Sorry, you're out of guesses!",
                "I'm afraid that's your last guess.",
                "Oops, that's not it either!",
                "Three strikes and you're out!"
                "Drat, another miss. Are these clues too difficult?"
            ]
        }
        return random.choice(response_prefixes[guess_type])

    def encourage(self, guess_type, guesses_remaining):
        if guess_type == "miss":
            self.feedback = f"{self.get_prefix('miss')}\nYou have {guesses_remaining} guesses left..."
        elif guess_type == "loss":
            self.feedback = f"{self.get_prefix('loss')}\nWould you like to play another round?"
        self.give_feedback()
        return self.feedback

    def congratulate(self, guesses_used):
        responses = [
            "You figured it out in just one guess!",
            "That second clue really clinched it for you!",
            "You got there in the end!"
        ]
        self.feedback = f"{self.get_prefix('win')} {responses[guesses_used-1]}"
        self.give_feedback()
        return self.feedback


gamehost = GameHost()
