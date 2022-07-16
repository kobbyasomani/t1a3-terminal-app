from player import player1


class GameHost:
    """A class for displaying user feedback messages"""

    def __init__(self):
        self.feedback = ""

    def welcome(self, player1):
        if player1.games_played == 0:
            self.feedback = "\nWelcome to The Guessing Game!\nHave some fun and test your wits by guessing a secret number, word, or phrase within three guesses.\nPlease choose from one of the categories below by entering the name or number.\n"
        print(self.feedback)


gamehost = GameHost()
