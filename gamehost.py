from player import player1


class GameHost:
    """A class for displaying user feedback messages"""

    def __init__(self):
        self.feedback = ""

    def give_feedback(self):
        print(self.feedback)

    def welcome(self):
        if player1.games_played == 0:
            self.feedback = "\nWelcome to The Guessing Game!\nHave some fun and test your wits by guessing a secret number, word, or phrase within three guesses.\nPlease choose from one of the categories below by entering the name or number.\n"
        self.give_feedback()

    def give_clue(self, clue, guesses_remaining):
        if guesses_remaining == 3:
            self.feedback = f"And we're off! Can you guess it in one go?\nHere's your first clue:\n{clue}"
            self.give_feedback()


gamehost = GameHost()
