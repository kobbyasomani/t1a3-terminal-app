import unittest
from player import Player


class TestPlayer(unittest.TestCase):
        
    def test_no_games_played(self):
        player = Player()
        self.assertEqual(player.get("games_played"), 0)

    def test_increment_games_played(self):
        player = Player()
        self.assertGreater(player.increment("games_played"), 0)
