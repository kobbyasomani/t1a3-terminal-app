import random


class GameHost:
    """A class for displaying user feedback messages"""

    def __init__(self):
        self.feedback = ""

    def give_feedback(self):
        """Print a message and clear the feedback attribute."""
        print(f"\n{self.feedback}")
        self.feedback = ""

    def welcome(self, games_played: int):
        """Print a welcome message at the menu screen"""
        if games_played == 0:
            self.feedback = ("Welcome to The Guessing Game!"
                            "\nHave some fun and test your wits by guessing"
                            "a secret number, word, or\nphrase in three "
                            "guesses. Please choose from one of the "
                            "categories below\nby typing the name or number "
                            "and pressing 'enter' or 'return'.\n")
        elif games_played == 1:
            self.feedback = ("You decided to play another round!"
                            "\nWhich category will you choose this time?\n")
        elif games_played <= 9:
            welcome_prefix = [
                "Glad to see you're still enjoying yourself!",
                "May as well play another round, eh?",
                "Good stuff! Let's keep guessing...",
                "Another day, another guessing game.",
                "Right, lets dive into another category!"
            ]
            self.feedback = (f"{random.choice(welcome_prefix)}"
                            "\nWhich category will you play next?\n")
        else:
            self.feedback = ("Wow, you're a guessing machine!"
                            "\nShouldn't you take a break at some point?\n")
        self.give_feedback()

    def intro_category(self, category: str):
        """Introduce a game category at the start of the round"""
        if category:
            match category:
                case "numbers":
                    self.feedback = ("Guess a secret number between 1 and 10 "
                                    "(inclusive)\nin three guesses! I'll "
                                    "give you some clues about whether the"
                                    "\nnumber is higher or lower as you "
                                    "play. The number is an integer.")
                case "mythical creatures":
                    self.feedback = ("In this game you'll get three attempts "
                                    "to guess the mythical creature \nI'm "
                                    "thinking of! I'll give you clues about "
                                    "the creature to help. \nThe answer will "
                                    "be a single word.")
                case "famous monuments":
                    self.feedback = ("In this game you'll have to guess the "
                                    "famous monument I'm \nthinking of from "
                                    "the clues. You'll have three guesses to "
                                    "get \nit right! The answer could be "
                                    "more than one word.")
            intro_message = self.feedback
            print(self.feedback)
            return intro_message

    def give_clue(self, clue, guesses_remaining: int):
        """Print a clue passed from the guessing loop."""
        if guesses_remaining == 3:
            self.feedback = (f"And we're off! Can you guess it in one go? "
                            f"\nHere's your first clue: {clue}")
        elif guesses_remaining == 2:
            self.feedback = f"Ok, here's your next clue: {clue}"
        else:
            self.feedback = f"Good luck! Here's your final clue: {clue}"
        clue_message = self.feedback
        self.give_feedback()
        return clue_message

    def get_prefix(self, guess_type: str):
        """Get a prefix to use with an encouragement message."""
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
            ],
            "partial": [
                "You're SO CLOSE to the answer!",
                "Wow, it's right on the tip of your tongue!",
                "You're on the right track, keep going!",
                "So close, you can almost TASTE the secret!",
                "Yeah, yeah, you're almost there!",
                "One more nudge should do it!"
            ]
        }
        return random.choice(response_prefixes[guess_type])

    def encourage(self, guess: str, guess_type: str, guesses_remaining: int):
        """Print an encouraging message after a miss or loss."""
        guesses_remaining_text = ""
        if guesses_remaining > 1:
            guesses_remaining_text = (f"You have {guesses_remaining} "
                                    "guesses remaining")
        else:
            guesses_remaining_text = (f"You have {guesses_remaining} "
                                    "guess remaining")
        if guess_type == "partial":
            self.feedback = (f"{guess.title()}? {self.get_prefix('partial')}"
                            f"\n{guesses_remaining_text}")
        if guess_type == "miss":
            self.feedback = (f"{guess.title()} you say? "
                            f"{self.get_prefix('miss')}"
                            f"\n{guesses_remaining_text}.")
        elif guess_type == "loss":
            self.feedback = (f"It's not {guess.title()} either. "
                            f"{self.get_prefix('loss')}")
        self.give_feedback()
        return self.feedback

    def congratulate(self, guess: str, guesses_used: int):
        """Print a congratulatory message after a win."""
        responses = [
            "You figured it out in just one guess!",
            "That second clue really clinched it for you!",
            "You got there in the end!"
        ]
        self.feedback = (f"{self.get_prefix('win')} {guess.title()} "
                        f"is correct. {responses[guesses_used-1]}")
        self.give_feedback()
        return self.feedback

    def give_choice(self, prompt: str):
        """Give a yes/no input choice and return 'True' 'False' or 'quit'."""
        options_yes = ["y", "yes", "1"]
        options_no = ["n", "no", "0", "quit"]
        user_input = ""
        while user_input not in options_yes and user_input not in options_no:
            user_input = input(f"{prompt} (y/n)? ")
        if user_input in options_yes:
            return True
        if user_input in options_no:
            if user_input != "quit":
                return False
            else:
                return "quit"

    def goodbye(self, games_played):
        """Print a goodbye message before quitting the game."""
        goodbye_prefix_options = [
            "Thanks for playing!",
            "Sorry to see you go!",
            "Play again soon!",
            "Adiós, amgio!",
            "It's been real!",
            "I hope you had fun!"
        ]
        if games_played > 0:
            goodbye_prefix = random.choice(goodbye_prefix_options)
            goodbye_suffix = "Here's how you did:"
        else:
            goodbye_prefix = "Thanks for checking out the application!"
            goodbye_suffix = "\nI hope you get a chance to play some time."
        self.feedback = f"{goodbye_prefix} {goodbye_suffix}"
        print(self.feedback)


gamehost = GameHost()
