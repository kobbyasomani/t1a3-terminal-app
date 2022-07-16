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

    def give_clue(self, clue, guesses_remaining: int):
        if guesses_remaining == 3:
            self.feedback = f"And we're off! Can you guess it in one go?\nHere's your first clue: {clue}"
        elif guesses_remaining == 2:
            self.feedback = f"Ok, here's your next clue: {clue}"
        else:
            self.feedback = f"Good luck! Here's your final clue: {clue}"
        self.give_feedback()

    def get_prefix(self, guess_type: str):
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
                "No. Hmm... maybe another clue will help.",
                "Sorry, that's a miss!",
                "I'm afraid not..."
            ],
            "loss": [
                "Sorry, you're out of guesses!",
                "I'm afraid that's your last guess.",
                "Oops, that's your last try!",
                "Three strikes and you're out!",
                "Drat, another miss! Are these clues too difficult?"
            ]
        }
        return random.choice(response_prefixes[guess_type])

    def encourage(self, guess: str, guess_type: str, guesses_remaining: int):
        guesses_remaining_text = ""
        if guesses_remaining > 1:
            guesses_remaining_text = f"You have {guesses_remaining} guesses remaining"
        else:
            guesses_remaining_text = f"You have {guesses_remaining} guess remaining"
        if guess_type == "miss":
            self.feedback = f"{guess.title()} you say? {self.get_prefix('miss')}\n{guesses_remaining_text}."
        elif guess_type == "loss":
            self.feedback = f"It's not {guess.title()} either. {self.get_prefix('loss')}\nWould you like to play another round?"
        self.give_feedback()
        return self.feedback

    def congratulate(self, guess: str, guesses_used: int):
        responses = [
            "You figured it out in just one guess!",
            "That second clue really clinched it for you!",
            "You got there in the end!"
        ]
        self.feedback = f"{self.get_prefix('win')} {guess.title()} is correct. {responses[guesses_used-1]}"
        self.give_feedback()
        return self.feedback


gamehost = GameHost()
