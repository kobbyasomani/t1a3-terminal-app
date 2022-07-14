from dataclasses import dataclass


@dataclass
class Menu():
    """A class for storing guessing game categories in a menu."""
    menu_items: list
    selected_category: str = ""

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
                if user_selection.isnumeric():
                    if int(user_selection) == index+1:
                        return True
                elif user_selection == name:
                    return True
                else:
                    return False

    # If the user selection is valid, set their selection as the game category
    def set_selection(self, user_selection):
        if self.has_option(user_selection):
            if user_selection.isnumeric():
                self.selected_category = self.menu_items[int(user_selection+1)]
                return self.selected_category
            else:
                self.selected_category = user_selection
                return self.selected_category
        print(f"You have selected the category: {self.selected_category}!")


menu_categories = Menu([
    "Numbers",
    "Mythical Creatures",
    "Famous Monuments"
])
