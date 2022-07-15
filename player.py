from dataclasses import dataclass


@dataclass
class Player():
    """A class for keeping track of player stats"""
    games_played = 0
    games_won = 0
    games_lost = 0
    avg_guesses_to_answer = 0.0

    def get_games_played(self):
        return self.games_played

    def increment_games_played(self):
        self.games_played += 1
        return self.games_played


player1 = Player()
