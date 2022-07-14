from secret import Secret
import unittest


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
