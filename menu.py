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
            print("There are no menu items available.")

    def has_option(self, user_selection):
        for index, name in enumerate(self.menu_items):
            if (user_selection):
                if int(user_selection) == index+1 or user_selection == name:
                    return True
                else:
                    return False


menu_categories = Menu([
    "Numbers",
    "Mythical Creatures",
    "Famous Monuments"
])