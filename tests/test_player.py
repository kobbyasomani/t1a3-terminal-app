import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    
    # Test getting a player attribute
    def test_no_games_played(self):
        player = Player()
        self.assertEqual(player.get("games_played"), 0)

    # Test incerementing a player attribute
    def test_increment_games_played(self):
        player = Player()
        self.assertGreater(player.increment("games_played"), 0)

    # Test calculating the average guesses to an answer
    def test_calculate_avg_guesses_to_answer(self):
        player = Player()
        games_played = 5
        total_guesses = 9
        self.assertEqual(player.calc_avg_guesses(total_guesses, games_played), 1.8)
