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

    # Test get random message prefix
    def test_get_message_prefix(self):
        gamehost = GameHost()
        self.assertTrue(gamehost.get_prefix())
    
    # Test generate congratulations message
    def test_congratulate_player(self):
        gamehost = GameHost()
        guesses_used = 1
        congratulation_message = gamehost.congratulate(guesses_used)
        self.assertEqual(congratulation_message, gamehost.feedback)