import unittest
from unittest import mock
from guessing_loop import GuessingLoop


class TestGuessingLoop(unittest.TestCase):
    # Test selection of a random secret
    def test_select_random_secret(self):
        guessing_loop = GuessingLoop()
        category = "mythical creatures"
        self.assertEqual(guessing_loop.get_secret(
            category), guessing_loop.current_secret)

    # Test selection of a random clue for the given secret
    def test_select_random_clue(self):
        guessing_loop = GuessingLoop()
        guess = ""
        category = "mythical creatures"
        secret = "unicorn"
        difficulty = "hard"
        self.assertTrue(guessing_loop.get_clue(
            guess, category, secret, difficulty))

    # Test that the loop starts and assigns a random secret to the current_secret attribute
    @mock.patch("guessing_loop.input", create=True)
    def test_start_guessing_loop(self, mock_guess_input):
        guessing_loop = GuessingLoop()
        category = "mythical creatures"
        mock_guess_input.side_effect = [
            "dog", "unicorn", "dragon"]
        guessing_loop.guesses_remaining = 0
        (guessing_loop.start(category))
        print(guessing_loop.current_secret)
        self.assertNotEqual(guessing_loop.current_secret, "")
