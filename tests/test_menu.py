from menu import Menu
import unittest

class TestMenu(unittest.TestCase):
    def test_menu_has_no_options(self):
        menu = Menu([])
        self.assertEqual(menu.get_length(), 0)

    def test_menu_has_options(self):
        menu = Menu(["item1","item2","item3"])
        self.assertGreater(menu.get_length(), 0)


# Test printing method
# menu = Menu(["item1","item2","item3"])
# menu.print_menu()

# menu = Menu([])
# menu.print_menu()
