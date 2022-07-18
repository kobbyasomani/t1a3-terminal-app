from os import system
from dataclasses import dataclass
from gamehost import gamehost
from player import player1
from secret import dict_secrets


@dataclass
class Menu():
    """A class for storing guessing game categories in a menu."""
    menu_items: list
    selected_category: str = ""

    def get_length(self):
        """Get the length of the menu (number of items)."""
        return len(self.menu_items)

    def print_menu(self):
        """Print the menu, with one option on each line (number and title)."""
        if self.get_length() > 0:
            for index, item in enumerate(self.menu_items):
                print(f"{index + 1}: {item.title()}")
        else:
            print("There are no menu items available.")

    def show_help(self):
        """Show in-game help."""
        system("clear")
        player1.show_player_stats()
        if player1.get("games_played") > 0:
            heading = "\nHow to play:"
        else:
            heading = "How to play:"
        print(f"{heading}"
            "\n- Select a category from the list of categories by typing its "
            "name or\n  number after the prompt and pressing 'return'."
            "\n- Follow the prompts from your friendly host to try and guess "
            "the secret word or number!"
            "\n- You can type 'yes', 'y', or '1', or 'no', 'n', or '0' to "
            "answer prompts."
            "\n- View your stats at the top of the terminal after "
            "every game round."
            "\n- Type 'quit' and hit 'return' during any prompt to end "
            "the game.\n")
        self.print_menu()
        return gamehost.intro_category(self.prompt_for_selection())

    def has_option(self, user_selection: str):
        """Check if user selection matches a menu item (index or string)"""
        # If there is a user selection
        if (user_selection):
            # If selection is numeric and matches a menu number
            if (user_selection.isnumeric()
                    and int(user_selection) in range(1, self.get_length()+1)):
                return [True, self.menu_items[int(user_selection)-1]]
            # Else if matches a menu name
            elif user_selection.lower() in self.menu_items:
                return [True, user_selection]
            else:
                # Partial match of at least 4 characters (e.g., 'numb')
                for item in self.menu_items:
                    if (len(user_selection) >= 4
                            and user_selection.lower() in item):
                        return [True, item]
                    # Else, option isn't in menu
                    else:
                        return [False, user_selection]
        # User selection was false (e.g., empty string)
        else:
            return [False, user_selection]

    def set_selection(self, user_selection: str):
        """If user selection is valid, set their selection as the category."""
        chosen_option = self.has_option(user_selection)
        if chosen_option[0] == True:
            # Check for quit
            if chosen_option[1] != "quit":
                system("clear")
            # If numeric, match with category number
            if user_selection.isnumeric():
                self.selected_category = (self.menu_items
                                        [int(user_selection)-1])
                print(
                    f"You have selected the category: "
                    f"{self.selected_category.title()}.")
                return self.selected_category
            # If string, match with category name
            else:
                self.selected_category = chosen_option[1]
                print(
                    f"You have selected the category: "
                    f"{self.selected_category.title()}.")
                return self.selected_category
        # If user input is empty, prompt for selection again
        elif user_selection == "":
            print(f"It looks like you didn't enter anything...")
            return self.prompt_for_selection()
        else:
            print(
                f"I'm sorry, '{user_selection}' is not an available option.")
            return self.prompt_for_selection()

    def get_selection(self):
        """Get the currently selected menu item (category)."""
        return self.selected_category

    def prompt_for_selection(self):
        """Prompt the user for menu item selection."""
        user_selection = input("\nSelect a category from the menu: ")
        if (user_selection == "help"
                or user_selection == str(self.menu_items.index("help")+1)):
            self.show_help()
        else:
            return self.set_selection(user_selection)

    def populate_menu(self, dictionary: dict):
        """Populate the menu with options using keys from a dictionary."""
        for key in dictionary:
            self.menu_items.append(key)


menu_categories = Menu([])
menu_categories.menu_items.append("numbers")
menu_categories.populate_menu(dict_secrets)
menu_categories.menu_items.append("help")
menu_categories.menu_items.append("quit")
