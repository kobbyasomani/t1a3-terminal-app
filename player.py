from dataclasses import dataclass


@dataclass
class Player():
    """A class for keeping track of player stats"""
    games_played: int = 0
    games_won: int = 0
    games_lost: int = 0
    avg_guesses_to_answer: float = 0.0
    points: int = 0


player = Player()