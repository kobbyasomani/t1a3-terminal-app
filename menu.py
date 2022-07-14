from dataclasses import dataclass

@dataclass
class Menu():
    """A class for storing guessing game categories in a menu."""
    menu_items: list

    def get_length(self):
        return len(self.menu_items)

    def print_menu(self):
        if self.get_length() > 0:
            for index, item in enumerate(self.menu_items):
                print(f"{index + 1}: {item}")
        else:
            print("There are no menu options available.")