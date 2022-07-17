from dataclasses import dataclass
import random


dict_secrets = {}


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

    def __post_init__(self):
        if self.category in dict_secrets:
            dict_secrets[self.category][self.answer] = self
        else:
            dict_secrets[self.category] = dict()
            dict_secrets[self.category][self.answer] = self

    def get_answer(self):
        return self.answer

    def has_clues(self):
        clues = self.clues
        for clue_difficulty, clue_list in clues.items():
            if len(clue_list) > 0:
                return True
        else:
            return False

    def get_clue(self, difficulty="hard"):
        return random.choice(self.clues[difficulty])


unicorn = Secret(
    "unicorn",
    {
        "easy": ["I have a long spiral horn."],
        "medium": ["I have the tail of a lion and the feet of a deer."],
        "hard": ["I am immortal."]
    },
    "mythical creatures"
)

dragon = Secret(
    "dragon",
    {
        "easy": ["I breathe scorching fire."],
        "medium": ["I have scales like a serpent, hard as rock."],
        "hard": ["I am very long-lived."]
    },
    "mythical creatures"
)

fairy = Secret(
    "fairy",
    {
        "easy": ["Tinkerbell is one of my sisters."],
        "medium": ["I like playing in gardens among the flowers."],
        "hard": ["I have gossamer wings."]
    },
    "mythical creatures"
)

eiffel_tower = Secret(
    "eiffel tower",
    {
        "easy": ["I make my home in 'the city of love'."],
        "medium": ["I have an ornate, wrought-iron lattice"],
        "hard": ["I'm 300 metres tall."]
    },
    "famous monuments"
)

pyramid_of_giza = Secret(
    "pryamid of giza",
    {
        "easy": ["I'm the tomb of an ancient Pharaoh."],
        "medium": ["I have a very broad base and a very narrow top."],
        "hard": ["I'm surrounded by ever-shifting sands."]
    },
    "famous monuments"
)

great_wall_of_china = Secret(
    "great wall of china",
    {
        "easy": ["My ancient stones stretch for miles and miles."],
        "medium": ["I've seen many battles between empires."],
        "hard": ["I'm the guardian of ancient states"]
    },
    "famous monuments"
)
