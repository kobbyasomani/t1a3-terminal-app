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
        guess_type = "win"
        self.assertTrue(gamehost.get_prefix(guess_type))

    # Test giving encouragement message after miss (incorrect guess)
    def test_encourage_player_miss(self):
        gamehost = GameHost()
        guess = "dog"
        guess_type = "miss"
        guesses_remaining = 2
        encouragement_message = gamehost.encourage(guess, guess_type, guesses_remaining)
        self.assertEqual(encouragement_message, gamehost.feedback)

    # Test giving encouraging message after loss (incorrect final guess)
    def test_encourage_player_loss(self):
        gamehost = GameHost()
        guess = "dog"
        guess_type = "loss"
        guesses_remaining = 0
        encouragement_message = gamehost.encourage(guess, guess_type, guesses_remaining)
        self.assertEqual(encouragement_message, gamehost.feedback)
    
    # Test congratulating player after a win
    def test_congratulate_player(self):
        gamehost = GameHost()
        guesses_used = 1
        guess = "unicorn"
        congratulation_message = gamehost.congratulate(guess, guesses_used)
        self.assertEqual(congratulation_message, gamehost.feedback)