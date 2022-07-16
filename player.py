from dataclasses import dataclass


@dataclass
class Player():
    """A class for keeping track of player stats"""
    games_played = 0
    games_won = 0
    games_lost = 0
    guesses_total = 0
    avg_guesses_to_answer = 0.0

    # Get a player attribute by passing the attribute name as an argument
    def get(self, attr: str):
        try:
            return getattr(self, attr)
        except AttributeError:
            print(f"{attr} is not a Player attribute.")

    def increment(self, attr: str):
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
        try:
            self.avg_guesses_to_answer = self.guesses_total / self.games_played
            return self.avg_guesses_to_answer
        except ZeroDivisionError:
            print(
                "Unable to calculate avg_guesses_to_answer. There are no games played yet.")
            return 0

    def show_player_stats(self):
        if self.games_played > 0:
            player_stats = f"Games played: {self.games_played} | Won: {self.games_won} | Lost: {self.games_lost} | Avg. guesses to answer: {self.calc_avg_guesses()}"
            print(f"Your stats: {player_stats}")
            return player_stats
        else:
            #print(f"Your stats: No games played yet! Choose a category below.")
            return False


player1 = Player()
# print(player1.calc_avg_guesses())
