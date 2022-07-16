import unittest
from gamehost import GameHost

class TestGameHost(unittest.TestCase):
    # Test give first clue
    def test_give_first_clue(self):
        gamehost = GameHost()
        clue = "Your first clue"
        guesses_remaining = 3
        gamehost.give_clue(clue, guesses_remaining)
        self.assertTrue(clue in gamehost.feedback)