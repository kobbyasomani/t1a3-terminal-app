from dataclasses import dataclass
import unittest


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


class TestMenu(unittest.TestCase):
    def test_menu_has_no_options(self):
        menu = Menu([])
        self.assertEqual(menu.get_length(), 0)

    def test_menu_has_options(self):
        menu = Menu(["item1","item2","item3"])
        self.assertGreater(menu.get_length(), 0)


# menu = Menu(["item1","item2","item3"])
# menu.print_menu()

# menu = Menu([])
# menu.print_menu()
