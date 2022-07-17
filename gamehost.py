import random


class GameHost:
    """A class for displaying user feedback messages"""

    def __init__(self):
        self.feedback = ""

    def give_feedback(self):
        print(f"\n{self.feedback}")
        self.feedback = ""

    def welcome(self, games_played: int):
        if games_played == 0:
            self.feedback = "Welcome to The Guessing Game!\nHave some fun and test your wits by guessing a secret number, word, or phrase within three guesses.\nPlease choose from one of the categories below by entering the name or number.\n"
        elif games_played == 1:
            self.feedback = "You decided to play another round!\nWhich category will you choose this time?"
        elif games_played <= 9:
            self.feedback = "Glad to see you're enjoying yourself!\nWhich category will you play next?"
        else:
            self.feedback = "Wow, you're a guessing machine! Shouldn't you take a break at some point?"
        self.give_feedback()

    def intro_category(self, category: str):
        if category:
            match category:
                case "numbers":
                    self.feedback = "In this game you'll need to guess a secret number between 1 and 10 (inclusive) in three guesses!\nI'll give you some clues about whether the number is higher or lower as you play."
                case "mythical creatures":
                    self.feedback = "In this game you'll have three guesses to guess the mythical creature I'm thinking of!\nI'll give you clues about the creature to help."
                case "famous monuments":
                    self.feedback = "In this game you'll have to guess the famous monument I'm thinking of from the clues.\nYou'll have three guesses to get it right!"
            intro_message = self.feedback
            print(self.feedback)
            return intro_message

    def give_clue(self, clue, guesses_remaining: int):
        if guesses_remaining == 3:
            self.feedback = f"And we're off! Can you guess it in one go?\nHere's your first clue: {clue}"
        elif guesses_remaining == 2:
            self.feedback = f"Ok, here's your next clue: {clue}"
        else:
            self.feedback = f"Good luck! Here's your final clue: {clue}"
        clue_message = self.feedback
        self.give_feedback()
        return clue_message

    def get_prefix(self, guess_type: str):
        response_prefixes = {
            "win": [
                "Amazing!",
                "Not bad at all!",
                "Well done!",
                "Not too shabby!"
            ],
            "miss": [
                "Not quite!",
                "That's not it... have another think about it.",
                "Nope!",
                "You could be close...",
                "No. Hmm... maybe another clue will help.",
                "Sorry, that's a miss!",
                "I'm afraid not..."
            ],
            "loss": [
                "Sorry, you're out of guesses!",
                "I'm afraid that's your last guess.",
                "Oops, that's your last try!",
                "Three strikes and you're out!",
                "Drat, another miss! Are these clues too difficult?"
            ]
        }
        return random.choice(response_prefixes[guess_type])

    def encourage(self, guess: str, guess_type: str, guesses_remaining: int):
        guesses_remaining_text = ""
        if guesses_remaining > 1:
            guesses_remaining_text = f"You have {guesses_remaining} guesses remaining"
        else:
            guesses_remaining_text = f"You have {guesses_remaining} guess remaining"
        if guess_type == "miss":
            self.feedback = f"{guess.title()} you say? {self.get_prefix('miss')}\n{guesses_remaining_text}."
        elif guess_type == "loss":
            self.feedback = f"It's not {guess.title()} either. {self.get_prefix('loss')}"
        self.give_feedback()
        return self.feedback

    def congratulate(self, guess: str, guesses_used: int):
        responses = [
            "You figured it out in just one guess!",
            "That second clue really clinched it for you!",
            "You got there in the end!"
        ]
        self.feedback = f"{self.get_prefix('win')} {guess.title()} is correct. {responses[guesses_used-1]}"
        self.give_feedback()
        return self.feedback

    def give_choice(self, prompt: str):
        options_yes = ["y", "yes", 1]
        options_no = ["n", "no", 0]
        user_input = ""
        while user_input not in options_yes and user_input not in options_no:
            user_input = input(f"{prompt} (y/n)? ")
        if user_input in options_yes:
            return True
        if user_input in options_no:
            return False

    def goodbye(self):
        goodbye_prefix = [
            "Thanks for playing!",
            "Sorry to see you go!",
            "Play again soon!",
            "Adiós, amgio!",
            "It's been real!",
            "I hope you had fun!"
        ]
        self.feedback = f"{random.choice(goodbye_prefix)} Here's how you did:"
        self.give_feedback()


gamehost = GameHost()
