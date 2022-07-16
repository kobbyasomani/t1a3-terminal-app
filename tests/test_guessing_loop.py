import unittest
from unittest import mock
from guessing_loop import GuessingLoop


class TestGuessingLoop(unittest.TestCase):
    def test_select_random_secret(self):
        guessing_loop = GuessingLoop()
        category = "mythical creatures"
        self.assertTrue(guessing_loop.get_secret(category))

    def test_select_random_clue(self):
        guessing_loop = GuessingLoop()
        category = "mythical creatures"
        secret = "unicorn"
        difficulty = "hard"
        self.assertTrue(guessing_loop.get_clue(category, secret, difficulty))

    # Test that the loop starts and assigns a random secret to the current_secret attribute
    @mock.patch("guessing_loop.input", create=True)
    def test_start_guessing_loop(self, mock_guess_input):
        guessing_loop = GuessingLoop()
        category = "mythical creatures"
        mock_guess_input.side_effect = ["dog", "unicorn", "dragon"]
        guessing_loop.start(category)
        self.assertNotEqual(guessing_loop.current_secret, "")


    # Test that there are no guesses remaining
"""     def test_no_guesses_remaining(self):
        guessing_loop = GuessingLoop()
        self.assertEqual(guessing_loop.remaining_guesses, 0) """
