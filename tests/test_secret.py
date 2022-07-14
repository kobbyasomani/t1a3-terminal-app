# from secret import Secret
from dataclasses import dataclass
import unittest


@dataclass
class Secret():
    """A class for storing answers (words and phrases) and corresponding clues"""
    answer: str
    clues: dict[
        "easy": [],
        "medium": [],
        "hard": []
    ]

    def get_answer(self):
        return self.answer

    def has_clues(self):
        clues = self.clues
        for clue_difficulty, clue_list in clues.items():
            if len(clue_list) > 0:
                return True
        else:
            return False


class TestSecret(unittest.TestCase):
    # Test whether secret has no answer
    def test_secret_has_no_answer(self):
        secret = Secret("", [])
        self.assertFalse(secret.get_answer())

    # Test whether secret has a retrievable answer
    def test_secret_has_answer(self):
        secret = Secret("answer", [])
        self.assertTrue(secret.get_answer())

    # Test whether secret has no clues
    def test_secret_has_no_clues(self):
        secret = Secret("answer", {})
        self.assertFalse(secret.has_clues())

    # Test whether secret has clues
    def test_secret_has_clues(self):
        secret = Secret("answer", {
            "easy": [
                "easy clue 1"
            ]
        })
        self.assertTrue(secret.has_clues())
