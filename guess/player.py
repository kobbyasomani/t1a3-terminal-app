from dataclasses import dataclass


@dataclass
class Player():
    """A class for keeping track of player stats"""
    games_played = 0
    games_won = 0
    games_lost = 0
    guesses_total = 0
    avg_guesses_to_answer = 0.0

    def get(self, attr: str):
        """Get player attribute using its name as an argument."""
        try:
            return getattr(self, attr)
        except AttributeError:
            print(f"{attr} is not a Player attribute.")

    def increment(self, attr: str):
        """Increment the passed player stat."""
        if attr != "avg_guesses_to_answer":
            try:
                match attr:
                    case "games_played":
                        self.games_played += 1
                    case "games_won":
                        self.games_won += 1
                    case "games_lost":
                        self.games_lost += 1
                    case "guesses_total":
                        self.guesses_total += 1
                    case _:
                        return False
                return True
            except AttributeError:
                print(f"{attr} is not a Player attribute.")
        else:
            print("avg_guesses_to_answer cannot be incremented.")

    def calc_avg_guesses(self):
        """Calculate the average number of guesses to get the secret."""
        try:
            self.avg_guesses_to_answer = (self.guesses_total
                                        / self.games_played)
            return round(self.avg_guesses_to_answer, 2)
        except ZeroDivisionError:
            print(
                "Unable to calculate avg_guesses_to_answer."
                "\nThere are no games played yet.")
            return 0

    def show_player_stats(self):
        """Print the player stats."""
        if self.games_played > 0:
            player_stats = (f"Games played: {self.games_played} | "
                            f"Won: {self.games_won} | "
                            f"Lost: {self.games_lost} | "
                            f"Avg. guesses to answer: "
                            f"{self.calc_avg_guesses()}")
            print(f"Your stats: {player_stats}")
            return player_stats
        else:
            return False


player1 = Player()
# print(player1.calc_avg_guesses())
