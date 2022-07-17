from os import system
from dataclasses import dataclass
from secret import dict_secrets


@dataclass
class Menu():
    """A class for storing guessing game categories in a menu."""
    menu_items: list
    selected_category: str = ""

    # Get the length of the menu (number of items)
    def get_length(self):
        return len(self.menu_items)

    # Print the menu, with one option on each line (number and title).
    def print_menu(self):
        if self.get_length() > 0:
            for index, item in enumerate(self.menu_items):
                print(f"{index + 1}: {item.title()}")
        else:
            print("There are no menu items available.")

    # Check if the user selection matches a menu item (by index number or value)
    def has_option(self, user_selection: str):
        if (user_selection):
            if user_selection.isnumeric() and int(user_selection) in range(1, self.get_length()+1):
                return [True, self.menu_items[int(user_selection)-1]]
            elif user_selection.lower() in self.menu_items:
                return [True, user_selection]
            else:
                for item in self.menu_items:
                    if user_selection.lower() in item:
                        return [True, item]
        else:
            return [False, user_selection]

    # If the user selection is valid, set their selection as the selected category
    def set_selection(self, user_selection: str):
        chosen_option = self.has_option(user_selection)
        if chosen_option[0] == True:
            if user_selection.isnumeric():
                self.selected_category = self.menu_items[int(user_selection)-1]
                system("clear")
                print(
                    f"You have selected the category: {self.selected_category.title()}!")
                return self.selected_category
            else:
                self.selected_category = chosen_option[1]
                system("clear")
                print(
                    f"You have selected the category: {self.selected_category.title()}!")
                return self.selected_category
        elif user_selection == "":
            print(f"It looks like you didn't enter anything...")
        else:
            print(
                f"I'm sorry, '{user_selection}' is not one of the available options.")

    # Get the selected menu item (category)
    def get_selection(self):
        return self.selected_category

    # Prompt the user for menu item selection
    def prompt_for_selection(self):
        user_selection = input("\nSelect a category from the menu: ")
        return self.set_selection(user_selection)

    # Populate the menu with options using keys from a dictionary
    def populate_menu(self, dictionary: dict):
        for key, value in dictionary.items():
            self.menu_items.append(key)
            return self.menu_items


menu_categories = Menu([])
menu_categories.menu_items.append("numbers")
menu_categories.populate_menu(dict_secrets)
menu_categories.menu_items.append("quit")

# menu_categories = Menu([
#     "numbers",
#     "mythical creatures",
#     "famous monuments"
# ])
