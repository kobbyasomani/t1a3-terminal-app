from menu import Menu
import unittest


class TestMenu(unittest.TestCase):
    # Test whether menu has items or not
    def test_menu_is_empty(self):
        menu = Menu([])
        self.assertEqual(menu.get_length(), 0)

    def test_menu_has_items(self):
        menu = Menu(["item1", "item2", "item3"])
        self.assertGreater(menu.get_length(), 0)

    # Test whether user-entered option is a valid menu item (either index number or name)
    # Test user input of category name
    def test_menu_has_selection(self):
        menu = Menu(["item1", "item2", "item3"])
        user_selection = "item1"
        self.assertTrue(menu.has_option(user_selection))

    # Test user input of category index number
    def test_menu_has_selection(self):
        menu = Menu(["item1", "item2", "item3"])
        user_selection = "1"
        self.assertTrue(menu.has_option(user_selection))

    # Test if user selection is not present in menu
    def test_menu_does_not_have_selection(self):
        menu = Menu(["item1", "item2", "item3"])
        user_selection = ""
        self.assertFalse(menu.has_option(user_selection))


# Test printing method
# menu = Menu(["item1","item2","item3"])
# menu.print_menu()

# menu = Menu([])
# menu.print_menu()
