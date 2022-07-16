from dataclasses import dataclass


@dataclass
class Player():
    """A class for keeping track of player stats"""
    games_played = 0
    games_won = 0
    games_lost = 0
    guesses_total = 0
    avg_guesses_to_answer = 0.0

    # Get a player attribute by passing the attribute name as an argument
    def get(self, attr: str):
        try:
            return getattr(self, attr)
        except AttributeError:
            print(f"{attr} is not a Player attribute.")

    def increment(self, attr: str):
        if attr != "avg_guesses_to_answer":
            try:
                attribute = getattr(self, attr)
                attribute += 1
                return attribute
            except AttributeError:
                print(f"{attr} is not a Player attribute.")
        else:
            print("avg_guesses_to_answer cannot be incremented.")

    def calc_avg_guesses(self, guesses_total=guesses_total, games_played=games_played):
        try:
            self.avg_guesses_to_answer = guesses_total / games_played
            return self.avg_guesses_to_answer
        except ZeroDivisionError:
            print(
                "Unable to calculate avg_guesses_to_answer. There are no games played yet.")
            return 0


player1 = Player()
# print(player1.calc_avg_guesses())
