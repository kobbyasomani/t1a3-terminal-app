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
    def test_menu_has_option_name(self):
        menu = Menu(["item1", "item2", "item3"])
        user_selection = "item1"
        self.assertTrue(menu.has_option(user_selection))

    # Test user input of category index number
    def test_menu_has_option_index(self):
        menu = Menu(["item1", "item2", "item3"])
        user_selection = "1"
        self.assertTrue(menu.has_option(user_selection))

    # Test if user input is not present in menu
    def test_menu_does_not_have_option(self):
        menu = Menu(["item1", "item2", "item3"])
        user_selection = ""
        self.assertFalse(menu.has_option(user_selection))

    # Test category selection and assignment by category name
    def test_set_selection(self):
        menu = Menu(["item1", "item2", "item3"])
        user_selection = "item1"
        self.assertEqual(user_selection.lower(), menu.set_selection(user_selection).lower())

    # Test getting the currently selected category
    def test_get_selection(self):
        menu = Menu(["item1", "item2", "item3"])
        user_selection = "item1"
        self.assertEqual(menu.set_selection(user_selection), menu.get_selection())


# Test printing method
# menu = Menu(["item1","item2","item3"])
# menu.print_menu()

# menu = Menu([])
# menu.print_menu()
