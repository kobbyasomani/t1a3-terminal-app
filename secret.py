from dataclasses import dataclass


@dataclass
class Secret():
    """A class for storing answers (words and phrases) and corresponding clues"""
    answer: str
    clues: dict[
        "easy": [],
        "medium": [],
        "hard": []
    ]
    category: str

    def get_answer(self):
        return self.answer

    def has_clues(self):
        clues = self.clues
        for clue_difficulty, clue_list in clues.items():
            if len(clue_list) > 0:
                return True
        else:
            return False

    def add_to_secrets_list(self):
        if self.category in list_secrets:
            list_secrets[self.category].append(self)
        else:
            list_secrets[self.category] = self.category
            list_secrets[self.category].append(self)


unicorn = Secret(
    "unicorn",
    {
        "easy": ["I have a long spiral horn."],
        "medium": ["I have the tail of a lion and the feet of a deer."],
        "hard": ["I am immortal."]
    },
    "mythical creatures"
)

list_secrets = {
    "mythical creatures": []
}

unicorn.add_to_secrets_list()
