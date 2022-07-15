import unittest
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