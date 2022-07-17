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

    # Test calculating the average guesses to a correct answer
    def test_calculate_avg_guesses_to_answer(self):
        player = Player()
        player.games_played = 5
        player.guesses_total = 9
        self.assertEqual(player.calc_avg_guesses(), 1.8)

    # Test calculating average guesses when there are no games played
    def test_calculate_avg_guesses_to_answer_zero(self):
        player = Player()
        player.games_played = 0
        player.total_guesses = 0
        self.assertEqual(player.calc_avg_guesses(), 0)

    # Test displaying player stats when at least one game has been played
    def test_show_player_stats(self):
        player = Player()
        player.games_played = 1
        self.assertTrue(player.show_player_stats())

    # Test displaying player stats when at least no games have been played
    def test_show_player_stats_empty(self):
        player = Player()
        player.games_played = 0
        self.assertFalse(player.show_player_stats())
