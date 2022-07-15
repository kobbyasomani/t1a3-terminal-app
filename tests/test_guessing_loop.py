import unittest
from guessing_loop import GuessingLoop
from secret import list_secrets


class TestGuessingLoop(unittest.TestCase):
    def test_select_random_secret(self):
        guessing_loop = GuessingLoop()
        category = "mythical creatures"
        self.assertTrue(guessing_loop.get_secret(category))