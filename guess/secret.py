from dataclasses import dataclass
import random


dict_secrets = {}


@dataclass
class Secret():
    """A class for storing answers (words and phrases) 
    and corresponding clues"""
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

mermaid = Secret(
    "mermaid",
    {
        "easy": ["My siren song has been known to lure ships to wreck."],
        "medium": ["My scales shimmer with iridescence."],
        "hard": ["I don't need to hold my breath underwater."]
    },
    "mythical creatures"
)

phoenix = Secret(
    "phoenix",
    {
        "easy": ["When I'm reborn, I spread my wings anew in fire."],
        "medium": ["Glorious red is my plumage."],
        "hard": ["My weeping may heal your wounds."]
    },
    "mythical creatures"
)

eiffel_tower = Secret(
    "eiffel tower",
    {
        "easy": ["I make my home in 'the city of love'."],
        "medium": ["I have an ornate, wrought-iron lattice."],
        "hard": ["I'm 300 metres tall."]
    },
    "famous monuments"
)

great_pyramid_of_giza = Secret(
    "great pyramid of giza",
    {
        "easy": ["I'm the 'great' tomb of an ancient Pharaoh."],
        "medium": ["I have a very broad base and a very narrow top."],
        "hard": ["I'm surrounded by ever-shifting sands."]
    },
    "famous monuments"
)

great_wall_of_china = Secret(
    "great wall of china",
    {
        "easy": ["My ancient stones stretch for miles and miles."],
        "medium": ["I've seen many 'great' battles between empires."],
        "hard": ["I'm the guardian of ancient states."]
    },
    "famous monuments"
)

statue_of_liberty = Secret(
    "statue of liberty",
    {
        "easy": ["I'm a symbol of 'liberty' in the United States."],
        "medium": ["A fiery beacon is in my right hand."],
        "hard": ["A teal crown is upon my might head."]
    },
    "famous monuments"
)

taj_mahal = Secret(
    "taj mahal",
    {
        "easy": ["The final resting place of the emperor's wife, 'Mahal'."],
        "medium": ["My collosal white dome has many small friends."],
        "hard": ["My ivory marble is reflected in water."]
    },
    "famous monuments"
)
