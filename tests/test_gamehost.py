import unittest
from gamehost import GameHost

class TestGameHost(unittest.TestCase):
    # Test give first clue
    def test_give_first_clue(self):
        gamehost = GameHost()
        self.assertTrue(gamehost.give_clue())