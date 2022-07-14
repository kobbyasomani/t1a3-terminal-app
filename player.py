from dataclasses import dataclass


@dataclass
class Player():
    """A class for keeping track of player stats"""
    games_played = 0
    games_won = 0
    games_lost = 0
    avg_guesses_to_answer = 0.0


player1 = Player()
